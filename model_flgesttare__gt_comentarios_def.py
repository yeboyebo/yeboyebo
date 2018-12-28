
# @class_declaration yeboyebo #
from YBLEGACY.constantes import *
from models.flgesttare import flgesttare_def
import math
import datetime

class yeboyebo(gesttare):

    def yeboyebo_calculaTotalHoras(self, date, user):
        # usr = qsatype.FLUtil.nameUser()
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"gt_comentarios, gt_usuarios")
        q.setSelect(u" SUM(gt_comentarios.hdedicadas)")
        q.setFrom(u"gt_comentarios LEFT JOIN gt_usuarios ON gt_comentarios.idusuario = gt_usuarios.iduser")
        q.setWhere("gt_usuarios.iduser = '" + str(user) + "' AND gt_comentarios.fecha = '" + str(date) + "'")
        if q.exec_():
            if q.next():
                if q.value(0):
                    return flgesttare_def.iface.getTimefromHours(q.value(0))
                else:
                    return "00:00:00"

    def yeboyebo_queryGrid_mastertareas_initFilter(self):
        usr = qsatype.FLUtil.nameUser()
        initFilter = {}
        initFilter['filter'] = {"gr_t": "mastertareas", "s_gt_comentarios.fecha__exact": str(qsatype.Date())[:10], "s_gt_usuarios.iduser__exact": usr}
        initFilter['where'] = u" AND gt_usuarios.iduser = '" + str(usr) + "' AND gt_comentarios.fecha = '" + str(qsatype.Date()) + "'"
        initFilter['otros'] = {"gt_comentarios.fecha": str(qsatype.Date())[:10], "iduser": usr}
        return initFilter

    def yeboyebo_iniciaValoresLabel(self, model=None, template=None, cursor=None, data=None):
        # print(model, template, cursor, data)
        usr = qsatype.FLUtil.nameUser()
        labels = {}
        if template == "sprint" or template == "tareas":
            fecha = str(qsatype.Date())[:10]
            if data:
                fecha = data['otros']['gt_comentarios.fecha']
                usr = data['otros']['iduser']
            labels[u"totalHoras"] = self.iface.calculaTotalHoras(fecha, usr)
        return labels

    def yeboyebo_getForeignFields(self, model, template=None):
        fields = []
        fields = fields + super(yeboyebo, self.iface).getForeignFields(model, template)
        if template == 'mistareas' or template == 'mastertareas':
            return [
                {'verbose_name': 'rowColor', 'func': 'field_colorRow'},
                {'verbose_name': 'comboTarea', 'func': 'field_comboTarea'},
                {'verbose_name': 'horasDedicadas', 'func': 'field_horasDedicadas'},
                {'verbose_name': 'horaInicio', 'func': 'field_horaInicio'}
            ]
        return fields

    def yeboyebo_getIdusuario(self):
        return qsatype.FLUtil.nameUser()
        # q = qsatype.FLSqlQuery()
        # q.setTablesList(u"gt_usuarios")
        # q.setSelect(u"iduser")
        # q.setFrom(u"gt_usuarios")
        # q.setWhere("iduser = '" + qsatype.FLUtil.nameUser() + "'")
        # if q.exec_():
        #     if q.next():
        #         return q.value("idusuario")
        # return None

    def yeboyebo_field_colorRow(self, model):
        if model["gt_comentarios.hinicio"]:
            return "cSuccess"
        else:
            return None

    def yeboyebo_field_comboTarea(self, model):
        comboTarea = "#" + model["gt_tareas.codproyecto"] + " " + model["gt_tareas.descripcion"]
        return comboTarea

    def yeboyebo_field_horasDedicadas(self, model):
        return flgesttare_def.iface.getTimefromHours(model["gt_comentarios.hdedicadas"])

    def yeboyebo_field_horaInicio(self, model):
        horaInicio = model["gt_comentarios.hinicio"]
        if not horaInicio:
            return "00:00:00"
        else:
            horaInicio = flgesttare_def.iface.getTimefromHours((horaInicio / (1000 * 60 * 60)) % 24)
        return horaInicio

    def yeboyebo_filtraTareas(self, model, oParam):
        print(oParam)
        return True

    def yeboyebo_queryGrid_mistareas(self):
        usr = qsatype.FLUtil.nameUser()
        query = {}
        query["tablesList"] = u"gt_comentarios, gt_tareas, gt_proyectos, gt_usuarios"
        # query["select"] = u"gt_tareas.codproyecto, SUM(gt_comentarios.hdedicadas), gt_tareas.descripcion, gt_proyectos.refcliente, gt_proyectos.codcliente, gt_proyectos.descripcion, gt_usuarios.iduser"
        query["select"] = u"gt_comentarios.idcomentario ,gt_tareas.codproyecto, gt_comentarios.hdedicadas, gt_tareas.descripcion, gt_proyectos.refcliente, gt_proyectos.codcliente, gt_proyectos.descripcion, gt_usuarios.iduser, gt_comentarios.hinicio, gt_comentarios.fecha"
        query["from"] = u"gt_comentarios LEFT JOIN gt_tareas ON gt_comentarios.idtarea = gt_tareas.idtarea LEFT JOIN gt_usuarios ON gt_comentarios.idusuario = gt_usuarios.iduser LEFT JOIN gt_proyectos ON gt_proyectos.codproyecto = gt_tareas.codproyecto"
        query["where"] = u"gt_usuarios.iduser = '" + str(usr) + "'"
        # query["where"] += u" AND gt_comentarios.fecha = '2017-04-26'"
        query["where"] += u" AND gt_comentarios.fecha = '" + str(qsatype.Date()) + "'"
        # query["groupby"] = "gt_tareas.codproyecto, gt_tareas.idtarea, gt_tareas.descripcion, gt_proyectos.refcliente, gt_proyectos.codcliente, gt_proyectos.descripcion, gt_usuarios.iduser"
        query["orderby"] = "gt_comentarios.hinicio, gt_tareas.codproyecto"
        return query

    def yeboyebo_queryGrid_mastertareas(self):
        query = {}
        query["tablesList"] = u"gt_comentarios, gt_tareas, gt_proyectos, gt_usuarios"
        query["select"] = u"gt_comentarios.idcomentario ,gt_tareas.codproyecto, gt_comentarios.hdedicadas, gt_tareas.descripcion, gt_proyectos.refcliente, gt_proyectos.codcliente, gt_proyectos.descripcion, gt_usuarios.iduser, gt_comentarios.hinicio, gt_comentarios.fecha, gt_comentarios.comentario"
        query["from"] = u"gt_comentarios LEFT JOIN gt_tareas ON gt_comentarios.idtarea = gt_tareas.idtarea LEFT JOIN gt_usuarios ON gt_comentarios.idusuario = gt_usuarios.iduser LEFT JOIN gt_proyectos ON gt_proyectos.codproyecto = gt_tareas.codproyecto"
        query["where"] = u"1=1"
        query["orderby"] = "gt_comentarios.hinicio, gt_tareas.codproyecto"
        return query

    def yeboyebo_nuevaTarea(self, model, oParam):
        # #GAN #H460 Pedidos desde PDA
        arrTarea = oParam["ntarea"].split(" ")
        fecha = oParam["gt_comentarios.fecha"]
        nombreTarea = ""
        hashtag = None
        especial = False
        for pos in arrTarea:
            if pos.startswith("#"):
                # Quitamos el #
                pos = pos[1:]
                if pos[0] == "T":
                    pass
                elif pos[0] == "H":
                    if len(pos) != 5:
                        hashtag = flgesttare_def.iface.obtenerHashtag(pos)
                    else:
                        hashtag = pos
                    especial = True
                elif pos[0] == "X" or pos[0] == "M":
                    if not especial:
                        hashtag = pos
                else:
                    print("Cliente", pos)
                    # cliente = pos
            else:
                nombreTarea = nombreTarea + pos + " "
        # print("nombre tarea ", nombreTarea)
        # print("Hashtag ", hashtag)
        if not qsatype.FLUtil.sqlSelect(u"gt_proyectos", u"estado", ustr(u"codproyecto = '", hashtag, "'")):
            resul = {}
            resul['status'] = -3
            if hashtag:
                resul['msg'] = "No existe proyecto con hashtag " + hashtag
            else:
                resul['msg'] = "No se incluyo ningun hashtag valido"
            resul['param'] = hashtag
            return resul
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"gt_tareas")
        q.setSelect(u"idtarea")
        q.setFrom(u"gt_tareas")
        q.setWhere("UPPER(descripcion) like '%" + nombreTarea.strip().upper() + "%' AND codproyecto = '" + hashtag + "'")

        if q.exec_():
            if q.next():
                idtarea = q.value("idtarea")
                # print("insertar comentario", idtarea)
                # q = qsatype.FLSqlQuery()
                # q.setTablesList(u"gt_comentarios, gt_usuarios")
                # q.setSelect(u"gt_comentarios.idtarea")
                # q.setFrom(u"gt_comentarios LEFT JOIN gt_usuarios ON gt_comentarios.idusuario = gt_usuarios.idusuario")
                # q.setWhere("gt_comentarios.idtarea = '" + str(idtarea) + "' AND gt_usuarios.iduser = '" + qsatype.FLUtil.nameUser() + "' AND gt_comentarios.fecha = '" + str(qsatype.Date()) + "'")
                # if q.exec_():
                #     if q.next():
                #         print("ya existen comentarios")
                #     else:
                self.iface.insertarComentario(idtarea, fecha)
            else:
                print("insertar tarea")
                self.iface.insertarTarea(nombreTarea, hashtag, fecha)
        return True

    def yeboyebo_insertarTarea(self, descripcion, codproyecto, fecha):
        curTarea = qsatype.FLSqlCursor(u"gt_tareas")
        curTarea.setModeAccess(curTarea.Insert)
        curTarea.refreshBuffer()
        curTarea.setValueBuffer("nombre", descripcion)
        curTarea.setValueBuffer("descripcion", descripcion)
        curTarea.setValueBuffer("codproyecto", codproyecto)
        curTarea.setValueBuffer("codestado", "Abierta")
        if not curTarea.commitBuffer():
            return False
        else:
            self.iface.insertarComentario(curTarea.valueBuffer("idtarea"), fecha)
        return True

    def yeboyebo_insertarComentario(self, idtarea, fecha):
        print(qsatype.FLUtil.nameUser())
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"gt_usuarios")
        q.setSelect(u"iduser, costehora")
        q.setFrom(u"gt_usuarios")
        q.setWhere("iduser = '" + qsatype.FLUtil.nameUser() + "'")
        if not fecha:
            fecha = datetime.datetime.today().date()
        if q.exec_():
            if q.next():
                usuario = q.value("iduser")
                coste = q.value("costehora")
                print("______________")
                print(usuario, coste)
                curComentario = qsatype.FLSqlCursor(u"gt_comentarios")
                curComentario.setModeAccess(curComentario.Insert)
                curComentario.refreshBuffer()
                curComentario.setValueBuffer("idtarea", idtarea)
                curComentario.setValueBuffer("idusuario", usuario)
                curComentario.setValueBuffer("fecha", fecha)
                curComentario.setValueBuffer("hora", datetime.datetime.today().time())
                curComentario.setValueBuffer("hdedicadas", 0)
                curComentario.setValueBuffer("costehora", coste)
                curComentario.setValueBuffer("coste", 0)
                if not curComentario.commitBuffer():
                    return False
                return curComentario
        else:
            print("no se encuentra el usuario ")
        return False

    def yeboyebo_startstop(self, model, cursor):
        # print(cursor.valueBuffer("idcomentario"))
        comentarioactivo = qsatype.FLUtil.sqlSelect(u"gt_comentarios", u"idcomentario", ustr(u"idusuario = '", self.iface.getIdusuario(), "' AND hinicio is not null  and hinicio <> 0"))
        # print(comentarioactivo)
        # if(not comentarioactivo or cursor.valueBuffer("idcomentario") == comentarioactivo):
        if not comentarioactivo and not cursor.valueBuffer('hinicio'):
            cursor.setValueBuffer("hinicio", qsatype.Date().getTime())
        elif cursor.valueBuffer("idcomentario") == comentarioactivo:
            time = qsatype.Date().getTime() - cursor.valueBuffer('hinicio')
            time = (time / (1000 * 60 * 60)) % 24
            cursor.setValueBuffer("hdedicadas", cursor.valueBuffer('hdedicadas') + time)
            qsatype.FactoriaModulos.get('formRecordgt_comentarios').iface.bChCursor("hdedicadas", cursor)
            cursor.setValueBuffer("hinicio", None)
        else:
            cursor.setValueBuffer("hinicio", qsatype.Date().getTime())
            curComentario = qsatype.FLSqlCursor("gt_comentarios")
            curComentario.select(ustr("idcomentario = '", comentarioactivo, "'"))
            curComentario.setModeAccess(curComentario.Edit)
            curComentario.refreshBuffer()
            if curComentario.first():
                time = qsatype.Date().getTime() - curComentario.valueBuffer('hinicio')
                time = (time / (1000 * 60 * 60)) % 24
                curComentario.setValueBuffer("hdedicadas", curComentario.valueBuffer('hdedicadas') + time)
                qsatype.FactoriaModulos.get('formRecordgt_comentarios').iface.bChCursor("hdedicadas", curComentario)
                curComentario.setValueBuffer("hinicio", None)
                if not curComentario.commitBuffer():
                    return False
        if not cursor.commitBuffer():
            return False
        return True

    def yeboyebo_editarHoras(self, model, oParam, cursor):
        horasDedicadas = oParam["hdedicadas"]
        comentario = oParam["comentario"]
        if horasDedicadas:
            if horasDedicadas.find(".") > 0:
                cursor.setValueBuffer("hdedicadas", horasDedicadas)
            elif horasDedicadas.find(":") > 0:
                horasDedicadas = horasDedicadas.split(":")
                horas = horasDedicadas[0]
                minutes = math.ceil(float(horasDedicadas[1]) / 60 * 10000) / 10000.0
                cursor.setValueBuffer("hdedicadas", float(horas) + minutes)
            else:
                cursor.setValueBuffer("hdedicadas", horasDedicadas)
            qsatype.FactoriaModulos.get('formRecordgt_comentarios').iface.bChCursor("hdedicadas", cursor)
        if comentario:
            cursor.setValueBuffer("comentario", comentario)
        if comentario or horasDedicadas:
            if not cursor.commitBuffer():
                return False
        return True

    def yeboyebo_copiarTareaHoy(self, model, cursor):
        self.iface.insertarComentario(cursor.valueBuffer("idtarea"), None)
        return True

    def yeboyebo_eliminarTarea(self, model, oParam):
        if 'selecteds' in oParam:
            selecteds = oParam['selecteds'].split(u",")
            for i in selecteds:
                curComentario = qsatype.FLSqlCursor("gt_comentarios")
                curComentario.select(ustr("idcomentario = '", i, "'"))
                curComentario.setModeAccess(curComentario.Del)
                curComentario.refreshBuffer()
                curComentario.first()
                if not curComentario.commitBuffer():
                    return False
        return True

    def yeboyebo_copiarTareas(self, model, oParam):
        if 'selecteds' in oParam:
            selecteds = oParam['selecteds'].split(u",")
            for i in selecteds:
                cursor = qsatype.FLSqlCursor("gt_comentarios")
                cursor.select(ustr("idcomentario = '", i, "'"))
                cursor.setModeAccess(cursor.Browse)
                cursor.refreshBuffer()
                if cursor.first():
                    self.iface.copiarTareaHoy(None, cursor)
        return True

    def yeboyebo_dameTemplateTarea(self, model):
        url = '/gesttare/gt_tareas/' + str(model.idtarea.idtarea)
        return url

    def __init__(self, context=None):
        super().__init__(context)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None, data=None):
        return self.ctx.yeboyebo_iniciaValoresLabel(model, template, cursor, data)

    def getForeignFields(self, model, template=None):
        return self.ctx.yeboyebo_getForeignFields(model, template)

    def getIdusuario(self):
        return self.ctx.yeboyebo_getIdusuario()

    def queryGrid_mistareas(self):
        return self.ctx.yeboyebo_queryGrid_mistareas()

    def queryGrid_mastertareas(self):
        return self.ctx.yeboyebo_queryGrid_mastertareas()

    def queryGrid_mastertareas_initFilter(self):
        return self.ctx.yeboyebo_queryGrid_mastertareas_initFilter()

    def nuevaTarea(self, model, oParam):
        return self.ctx.yeboyebo_nuevaTarea(model, oParam)

    def editarHoras(self, model, oParam, cursor):
        return self.ctx.yeboyebo_editarHoras(model, oParam, cursor)

    def filtraTareas(self, model, oParam):
        return self.ctx.yeboyebo_filtraTareas(model, oParam)

    def eliminarTarea(self, model, oParam):
        return self.ctx.yeboyebo_eliminarTarea(model, oParam)

    def copiarTareas(self, model, oParam):
        return self.ctx.yeboyebo_copiarTareas(model, oParam)

    def startstop(self, model, cursor):
        return self.ctx.yeboyebo_startstop(model, cursor)

    def copiarTareaHoy(self, model, cursor):
        return self.ctx.yeboyebo_copiarTareaHoy(model, cursor)

    def field_colorRow(self, model):
        return self.ctx.yeboyebo_field_colorRow(model)

    def field_comboTarea(self, model):
        return self.ctx.yeboyebo_field_comboTarea(model)

    def field_horasDedicadas(self, model):
        return self.ctx.yeboyebo_field_horasDedicadas(model)

    def field_horaInicio(self, model):
        return self.ctx.yeboyebo_field_horaInicio(model)

    def insertarTarea(self, descripcion, codproyecto, fecha):
        return self.ctx.yeboyebo_insertarTarea(descripcion, codproyecto, fecha)

    def insertarComentario(self, idtarea, fecha):
        return self.ctx.yeboyebo_insertarComentario(idtarea, fecha)

    def calculaTotalHoras(self, date, user):
        return self.ctx.yeboyebo_calculaTotalHoras(date, user)

    def dameTemplateTarea(self, model):
        return self.ctx.yeboyebo_dameTemplateTarea(model)

