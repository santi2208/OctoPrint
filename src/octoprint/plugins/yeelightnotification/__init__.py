import octoprint.plugin

class YeelightNotification(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin):
    
    def on_after_startup(self):
        self._logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self._logger.info("!!!!Yeelight Notifications Plugin Initialized!!!!")
        self._logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # try:
        #     service_done = octoprint.plugin.PrintDone()
        #     service_done.run() 
        #     service_error = octoprint.plugin.PrintError()
        #     service_error.run() 
        # except Exception as err:
        #     self._logger.info("*************************")
        #     self._logger.info("*************************")
        #     self._logger.info(err)
        #     self._logger.info("*************************")
        #     self._logger.info("*************************")
             
        return super().on_after_startup()
    
__plugin_pythoncompat__ = ">=3.7,<4"
def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = YeelightNotification()