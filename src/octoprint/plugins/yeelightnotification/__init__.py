# from octoprint.plugin import TemplatePlugin, StartupPlugin
import octoprint.events
from octoprint.plugin import SettingsPlugin
from octoprint.events import Events, eventManager
from octoprint.plugin import PrintDone, PrintError

class YeelightNotification(SettingsPlugin):

    def __init__(self):
        eventManager().subscribe(Events.PRINT_STARTED, self.on_print_change_state)
        eventManager().subscribe(Events.PRINT_DONE, self.on_print_change_state)
        eventManager().subscribe(Events.PRINT_FAILED, self.on_print_change_state)
        eventManager().subscribe(Events.STARTUP, self.on_print_change_state)
        super(SettingsPlugin, self).__init__()
    
    def on_print_change_state(self, event, payload):
        self.runNotification(event, event)
    
    def runNotification(self, event, payload):
        self._logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self._logger.info("!!!!Yeelight Notifications Plugin Initialized!!!!")
        self._logger.info(event)
        self._logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
        try:
            if(event == Events.PRINT_DONE):
                service = PrintDone()
            elif(event == Events.PRINT_FAILED):
                service = PrintError()
            elif(event == Events.PRINT_STARTED):
                service = PrintDone()
            elif(event == Events.STARTUP):
                service = PrintDone()
                 
            if 'service' in locals():
                service.run()
        except Exception as err:
            self._logger.info("*************************")
            self._logger.info("*************************")
            self._logger.info(err)
            self._logger.info("*************************")
            self._logger.info("*************************")
    
__plugin_pythoncompat__ = ">=3.7,<4"
def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = YeelightNotification()