
# @class_declaration yeboyebo_gt_proyectos #
class yeboyebo_gt_proyectos(gesttare_gt_proyectos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def field_colorRow(self):
        return form.iface.field_colorRow(self)

    @helpers.decoradores.accion(aqparam=["cursor"])
    def cambiarEstado(self, cursor):
        return form.iface.cambiarEstado(self, cursor)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def visibility(self, oParam):
        return form.iface.visibility(self, oParam)

