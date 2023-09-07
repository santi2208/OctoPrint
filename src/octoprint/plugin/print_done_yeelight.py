from Yeelight import * 
from yeelight import Bulb
import time

class PrintDone(object):
    def __init__(self):
        self.Service = Yeelight()
        self.Service.SetDevice("192.168.0.4", "Bed bulb", 1)
        self.Service.SetDevice("192.168.0.7", "Kitchen bulb", 2)
    
    def run(self):
        sleepTime = 2
        self.Service.GetProperties()

        self.Service.TurnOnEverything()
        time.sleep(sleepTime)

        self.Service.SetBrightness(100, id = 1)
        self.Service.SetBrightness(100, id = 2)
        time.sleep(sleepTime)

        self.Service.StartFlow(flowId = 5, id = 2)
        self.Service.StartFlow(flowId = 5, id = 1)
        time.sleep(sleepTime * 5)

        self.Service.StopFlowEverything()
        time.sleep(sleepTime)

        self.Service.WhiteAll()

#PrintDone().run()