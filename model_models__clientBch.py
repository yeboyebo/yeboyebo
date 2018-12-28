# @class_declaration interna #
from YBLEGACY import qsatype
from YBLEGACY.constantes import *


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration yeboyebo #
class yeboyebo(interna):

    def yeboyebo_gt_comentarios_tareas(self, fN, dict, prefix, pk):
        if fN == "recuentoHoras":
            from models.flgesttare.gt_comentarios import gt_comentarios
            total = gt_comentarios.calculaTotalHoras(dict["otros"]["gt_comentarios.fecha"], dict["otros"]["iduser"])
            dict["labels"]["totalHoras"] = total
            if(dict["otros"]["gt_comentarios.fecha"] != str(qsatype.Date())[:10]) or dict["otros"]["iduser"] != qsatype.FLUtil.nameUser():
                dict["drawIf"]["queryGrid_mastertareas"]["copiarTareaHoy"] = None
                dict["drawIf"]["queryGrid_mastertareas"]["startstop"] = "hidden"
            else:
                dict["drawIf"]["queryGrid_mastertareas"]["copiarTareaHoy"] = "hidden"
                dict["drawIf"]["queryGrid_mastertareas"]["startstop"] = None
        return dict

    def __init__(self, context=None):
        super().__init__(context)

    def gt_comentarios_tareas(self, fN, dict, prefix, pk):
        return self.yeboyebo_gt_comentarios_tareas(fN, dict, prefix, pk)


# @class_declaration head #
class head(yeboyebo):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
