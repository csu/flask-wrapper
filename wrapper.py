import flask

# Usage:
# wrapper = FlaskWrapper()
# wrapper.add_routes(module, {
#     '/route': 'method',
#     '/another': 'another_method'
# })
# wrapper.app.run()
class FlaskWrapper:
    def __init__(self):
        self.app = Flask(__name__)

    def add_routes(module, route_map):
        