from flask import Blueprint

# Usage:
# wrapper = FlaskBlueprintWrapper()
# wrapper.add_routes(module, {
#     '/route': 'method',
#     '/another': 'another_method'
# })
# app.register_blueprint(wrapper)
class FlaskBlueprintWrapper:
    def __init__(self, blueprint=None, *args, **kwargs):
        if type(blueprint) is Blueprint:
            self.blueprint = blueprint
        elif isinstance(blueprint, basestring):
            self.blueprint = Blueprint(blueprint,
                __name__, *args, **kwargs)
        else:
            self.blueprint = Blueprint('wrapped_blueprint',
                __name__, *args, **kwargs)

    def add_routes(self, module, route_map):
        for r, m in route_map.iteritems():
            method = getattr(module, m)
            self.blueprint.add_url_rule(r, method.__name__, method)