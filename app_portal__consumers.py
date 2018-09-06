from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.security.websockets import allowed_hosts_only
from models.flsisppal.models import mtd_chatmessages as ChatMessage
from models.flsisppal.models import mtd_chatstatus as chatStatus
from datetime import datetime
import json
# from channels.asgi import get_channel_layer
from django.contrib.auth.models import User
from YBUTILS import notifications


# Connected to chat-messages
def msg_consumer(message):
    # Actualizamos tiempo ultima conexion de usuario
    status = chatStatus.objects.get(room=message.content['user'])
    status.ultcon = datetime.now()
    status.save()

    # Analizamos mensaje recibido, si es para un usuario del sistema lo enviamos
    msg = json.loads(message.content['message'])
    if "notification" in msg:
        print("________________")
        print("esto es una notificacion no hay que enviarla")
        print(msg)
        notifications.sendNotification(msg['notification']['sender'].capitalize(), msg['notification']['msg'], msg['notification']['user'])
    else:
        for m in msg:
            room = m
            mensaje = msg[m]
        sisuser = User.objects.get(username=m)

        if sisuser.is_authenticated():
            # Almacenamos mensaje enviado
            ChatMessage.objects.create(
                room=message.content['room'],
                message=mensaje,
                sender=message.content['user'],
                receiver=room,
                fechahora=datetime.now()
            )
            try:
                # Comprobamos ultima conexion del usuario
                roomstatus = chatStatus.objects.get(room=room)
                ultcon = datetime.now() - roomstatus.ultcon
                sendtext = {"sender": message.content["user"], "message": mensaje}
                print(sendtext)
                if (ultcon.total_seconds() / 3600) < 2:
                    Group("ws-%s" % room).send({
                        "text": json.dumps({
                            "sender": message.content["user"],
                            "message": mensaje
                        }),
                    })
                else:
                    print("ultima conexion hace ", ultcon)
                    notifications.sendNotification(message.content["user"].capitalize(), mensaje, room)
            except Exception as e:
                print(e)
                # notifications.sendNotification(message.content["user"].capitalize(), mensaje, room)
                pass
        else:
            # TODO
            print("Se intento utilizar un usuario que no es del sistema")


@allowed_hosts_only
@channel_session_user_from_http
def ws_connect(message):
    # room = message.content['path'].strip("/")
    message.channel_session['room'] = message.content['path'].strip("/")
    print("conectado a " + message.user.username)
    Group("ws-%s" % message.user.username).add(message.reply_channel)
    try:
        status = chatStatus.objects.get(room=message.user.username)
        status.ultcon = datetime.now()
        status.save()
    except Exception as e:
        print("__entra__", e)
        chatStatus.objects.create(
            room=message.user.username,
            ultcon=datetime.now()
        )
    message.reply_channel.send({"accept": True})


@channel_session_user
def ws_message(message):
    try:
        print(message.user.is_authenticated())
        print(message.user.username)
        Channel("ws-messages").send({
            "room": message.channel_session['room'],
            "message": message['text'],
            "user": message.user.username
        })
    except:
        print("errro")


@channel_session_user
def ws_disconnect(message):
    Group("ws-%s" % message.user.username).discard(message.reply_channel)
