import debug_module
from wrapper import FlaskWrapper

wrapper = FlaskWrapper()
wrapper.add_routes(debug_module, {
    '/': 'test'
})
wrapper.app.run()