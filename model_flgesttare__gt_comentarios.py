
# @class_declaration yeboyebo_gt_comentarios #
class yeboyebo_gt_comentarios(gesttare_gt_comentarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor, data)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getDesc():
        return form.iface.getDesc()

    def getIdusuario(self):
        return form.iface.getIdusuario()

    def queryGrid_mistareas():
        return form.iface.queryGrid_mistareas()

    def queryGrid_mastertareas():
        return form.iface.queryGrid_mastertareas()

    def queryGrid_mastertareas_initFilter(model=None):
        return form.iface.queryGrid_mastertareas_initFilter()

    @helpers.decoradores.accion(aqparam=["oParam"])
    def nuevaTarea(self, oParam):
        return form.iface.nuevaTarea(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def filtraTareas(self, oParam):
        return form.iface.filtraTareas(self, oParam)

    @helpers.decoradores.accion(aqparam=["cursor"])
    def startstop(self, cursor):
        return form.iface.startstop(self, cursor)

    def field_colorRow(self):
        return form.iface.field_colorRow(self)

    def field_comboTarea(self):
        return form.iface.field_comboTarea(self)

    def field_horasDedicadas(self):
        return form.iface.field_horasDedicadas(self)

    def field_horaInicio(self):
        return form.iface.field_horaInicio(self)

    def calculaTotalHoras(date, user):
        return form.iface.calculaTotalHoras(date, user)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def editarHoras(self, oParam, cursor):
        return form.iface.editarHoras(self, oParam, cursor)

    @helpers.decoradores.accion(aqparam=["cursor"])
    def copiarTareaHoy(self, cursor):
        return form.iface.copiarTareaHoy(self, cursor)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def eliminarTarea(self, oParam):
        return form.iface.eliminarTarea(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def copiarTareas(self, oParam):
        return form.iface.copiarTareas(self, oParam)

    @helpers.decoradores.accion()
    def dameTemplateTarea(self):
        return form.iface.dameTemplateTarea(self)

