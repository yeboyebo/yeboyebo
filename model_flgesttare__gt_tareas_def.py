
# @class_declaration yeboyebo #
from YBUTILS.viewREST import cacheController


class yeboyebo(gesttare):

    def yeboyebo_getFilters(self, model, name, template=None):
        filters = []

        return filters

    def yeboyebo_check_permissions(self, model, prefix, pk, template, acl, accion):
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def getFilters(self, model, name, template=None):
        return self.ctx.yeboyebo_getFilters(model, name, template)

    def check_permissions(self, model, prefix, pk, template, acl, accion=None):
        return self.ctx.yeboyebo_check_permissions(model, prefix, pk, template, acl, accion)

