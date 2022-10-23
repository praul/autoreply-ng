def load_plugin(name):
    mod = __import__("plugin_%s" % name, globals(), locals(  ))
    return mod

def call_plugin_before_send(name, *args, **kwargs):
    plugin = load_plugin(name)
    return plugin.before_send(*args, **kwargs)

def call_plugin_after_send(name, *args, **kwargs):
    plugin = load_plugin(name)
    return plugin.after_send(*args, **kwargs)

def call_plugin_frontend_json(name, *args, **kwargs):
    plugin = load_plugin(name)
    return plugin.frontend_json(*args, **kwargs)