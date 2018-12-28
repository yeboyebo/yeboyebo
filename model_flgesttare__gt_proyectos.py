
# @class_declaration yeboyebo_gt_proyectos #
class yeboyebo_gt_proyectos(gesttare_gt_proyectos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def field_colorRow(self):
        return form.iface.field_colorRow(self)

    @helpers.decoradores.accion(aqparam=["cursor"])
    def cambiarEstado(self, cursor):
        return form.iface.cambiarEstado(self, cursor)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def visibility(self, oParam):
        return form.iface.visibility(self, oParam)

