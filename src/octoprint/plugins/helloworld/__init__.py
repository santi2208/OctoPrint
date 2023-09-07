import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
    
    def on_after_startup(self):
        self._logger.info("Hola Santi!!! (more: %s)" % self._settings.get(["url"]))
        return super().on_after_startup()
    
    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")
    
    def get_template_vars(self):
        #return dict(url=self._settings.get(["url"]))
        return {"url":"https://en.wikipedia.org/wiki/Hello_world"}
    
    def get_assets(self):
        return {
            "js": ["js/helloworld.js"]
        }

    def get_template_configs(self):
	    return [
		{
			"type": "navbar",
			"template": "helloworld_navbar.jinja2",
			"suffix": "_wikipedia_link",
            "custom_bindings":"false"
		},{
			"type": "settings",
			"template": "helloworld_settings.jinja2",
			"suffix": "_settings",
               "custom_bindings":"false"
		}]

__plugin_pythoncompat__ = ">=3.7,<4"
# __plugin_implementation__ = HelloWorldPlugin()
def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = HelloWorldPlugin()