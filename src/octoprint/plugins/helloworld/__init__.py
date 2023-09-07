import octoprint.plugin
# from print_done_yeelight import PrintDone
# import octoprint.plugins.helloworld.libs


class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
    
    def on_after_startup(self):
        self._logger.info("!!!!!!!!!!!!!!!!!! (more: %s)" % self._settings.get(["url"]))
        self._logger.info("!!!!!!!!!!!!!!!!!! (more: %s)" % self._settings.get(["url"]))
        try:
            self._logger.info("-----------------------------")
            self._logger.info("-----------------------------")
            service = octoprint.plugin.PrintDone()
            service.run() 
            self._logger.info(service)
            self._logger.info("-----------------------------")
            self._logger.info("-----------------------------")
            # self.run()
        except Exception as err:
            self._logger.info("*************************")
            self._logger.info("*************************")
            self._logger.info(err)
            self._logger.info("*************************")
            self._logger.info("*************************")
             
        # print_done = PrintDone() # PrintDone().run()
        #octoprint.plugins.helloworld.libs
        #self._logger.info("!!!!!!PrintDone!!!")
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