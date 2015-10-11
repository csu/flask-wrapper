import debug_module
from flask_wrapper import FlaskAppWrapper

wrapper = FlaskAppWrapper()
wrapper.add_routes(debug_module, {
    '/': 'test'
})
wrapper.run()