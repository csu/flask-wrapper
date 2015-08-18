from flask import Flask

# Usage:
# wrapper = FlaskWrapper()
# wrapper.add_routes(module, {
#     '/route': 'method',
#     '/another': 'another_method'
# })
# wrapper.app.run()
class FlaskWrapper:
    def __init__(self, app=None):
        if app:
            self.app = app
        else:
            self.app = Flask(__name__)

    def add_routes(self, module, route_map):
        for r, m in route_map.iteritems():
            method = getattr(module, m)
            self.app.add_url_rule(r, method.__name__, method)