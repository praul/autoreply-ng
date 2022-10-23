import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "lib/plugins"))

import json
import plugin_loader

settings_json = open('../config.json')
settings = json.load(settings_json)
settings = settings['backend']
print(settings['plugins'])


def plugins_before():
    for plugin in settings['plugins']:
        out = plugin_loader.call_plugin_before_send(plugin, 1234)
        print(out)


plugins_before()