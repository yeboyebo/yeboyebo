
# @class_declaration yeboyebo #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController


class yeboyebo(gesttare):

    def yeboyebo_getFilters(self, model, name, template=None):
        filters = []
        return filters

    def yeboyebo_getForeignFields(self, model, template=None):
        fields = []
        if template == 'master':
            return [
                {'verbose_name': 'rowColor', 'func': 'field_colorRow'}
            ]
        return fields

    def yeboyebo_field_colorRow(self, model):
        if model.estado == "Terminado":
            return "cSuccess"
        else:
            return None
        return None

    def yeboyebo_cambiarEstado(self, model, cursor):
        print(cursor.valueBuffer("estado"))
        estado = "Terminado"
        fechaterminado = qsatype.Date()
        if cursor.valueBuffer("estado") == "Terminado":
            estado = "Abierto"
            fechaterminado = None
        cursor.setValueBuffer("estado", estado)
        cursor.setValueBuffer("fechaterminado", fechaterminado)
        if not cursor.commitBuffer():
            return False
        return True

    def yeboyebo_visibility(self, model, oParam):
        visible = cacheController.getSessionVariable(ustr(u"visibePT_", qsatype.FLUtil.nameUser()))
        if not visible:
            cacheController.setSessionVariable(ustr(u"visibePT_", qsatype.FLUtil.nameUser()), True)
        elif visible:
            cacheController.setSessionVariable(ustr(u"visibePT_", qsatype.FLUtil.nameUser()), False)
        return True

    def yeboyebo_check_permissions(self, model, prefix, pk, template, acl, accion):
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def check_permissions(self, model, prefix, pk, template, acl, accion=None):
        return self.ctx.yeboyebo_check_permissions(model, prefix, pk, template, acl, accion)

    def getFilters(self, model, name, template=None):
        return self.ctx.yeboyebo_getFilters(model, name, template)

    def getForeignFields(self, model, template=None):
        return self.ctx.yeboyebo_getForeignFields(model, template)

    def field_colorRow(self, model):
        return self.ctx.yeboyebo_field_colorRow(model)

    def cambiarEstado(self, model, cursor):
        return self.ctx.yeboyebo_cambiarEstado(model, cursor)

    def visibility(self, model, oParam):
        return self.ctx.yeboyebo_visibility(model, oParam)

