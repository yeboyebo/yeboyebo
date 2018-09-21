
# @class_declaration yeboyebo #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController
import math


class yeboyebo(gesttare):

    def yeboyebo_obtenerHashtag(self, hashtag):
        if len(hashtag) < 5:
            idh = hashtag[1:]
            faltan = 5 - len(hashtag)
            while faltan != 0:
                faltan = faltan - 1
                idh = "0" + idh
            hashtag = "H" + idh
            return hashtag
        elif len(hashtag) > 5:
            print("hashtag demasiado largo")
            return None
        else:
            print("Error inesperado al obtener hashtag")
            return None
        return hashtag

    def yeboyebo_getTimefromHours(self, hours):
        horas = hours
        hours = int(hours)
        resto = horas - hours
        minutes = int(resto * 60)
        seconds = int(((resto * 60) - minutes) * 60)
        hours = "0" + str(hours) if hours < 10 else str(hours)
        minutes = "0" + str(minutes) if minutes < 10 else str(minutes)
        seconds = "0" + str(seconds) if seconds < 10 else str(seconds)
        time = hours + ":" + minutes + ":" + seconds
        return time

    def __init__(self, context=None):
        super(yeboyebo, self).__init__(context)

    def obtenerHashtag(self, hashtag):
        return self.ctx.yeboyebo_obtenerHashtag(hashtag)

    def getTimefromHours(self, hours):
        return self.ctx.yeboyebo_getTimefromHours(hours)

