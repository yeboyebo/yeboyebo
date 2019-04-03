
# @class_declaration yeboyebo #
from YBUTILS.viewREST import cacheController


class yeboyebo(gesttare):

    def yeboyebo_bChCursor(self, fN, cursor):
        if fN == "idusuario":
            costehora = qsatype.FLUtil.sqlSelect(u"gt_usuarios", u"costehora", ustr(u"idusuario = '", cursor.valueBuffer("idusuario"), u"'"))
            cursor.setValueBuffer("costehora", costehora)
        elif fN == "totaltiempo":
            totaltiempo = self.iface.time_to_seconds(cursor.valueBuffer("totaltiempo"))
            costehora = cursor.valueBuffer("costehora") or 0
            coste = (totaltiempo / 3600) * costehora
            cursor.setValueBuffer("coste", coste)
        else:
            super(yeboyebo, self.iface).bChCursor(fN, cursor)

    def __init__(self, context=None):
        super().__init__(context)

    def bChCursor(self, fN, cursor):
        return self.ctx.yeboyebo_bChCursor(fN, cursor)

