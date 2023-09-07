from yeelight import *
from yeelight.transitions import *
from yeelight import Flow
from yeelight import Bulb
import time

class Device(object):
    def __init__(self, ip, name, id):
        self.Id = id
        self.Name = name
        self.Ip = ip
        self.Instance = Bulb(ip)

class YeelightFlow(object):
    def __init__(self, name, flow):
        self.Name = name
        self.Flow = flow

class Yeelight(object):
    def __init__(self):
        self.Devices = []
        self.ColorDictionary = {
            'red': [255, 0, 0],
            'green': [0, 255, 0],
            'blue': [0, 0, 255],
            'white': [255, 255, 255],
            'cian': [0, 255, 255]
        }
        
        self.FlowDictionary = {
            1: YeelightFlow('Slowdown', slowdown()) , 
            2: YeelightFlow('Temp', temp()), 
            3: YeelightFlow('LSD',lsd()), 
            4: YeelightFlow('Police', police()), 
            5: YeelightFlow('Strobe', strobe()), 
            6: YeelightFlow('Strobe Color',strobe_color())
        }

    def SetDevice(self, ip, name, id):
        self.Devices.append(Device(ip, name, id))        

    def TurnOnEverything(self):
        for disp in self.Devices:
            disp.Instance.turn_on()

    def TurnOffEverything(self):
        for disp in self.Devices:
            disp.Instance.turn_off()

    def ToogleEverything(self):
        for disp in self.Devices:
            disp.Instance.toggle()            
    
    def TurnOn(self, name = None, id = None, ip = None):
        disp = self.GetDeviceBy(name, id, ip)
        if disp is not None:
            disp.Instance.turn_on()
        return disp.Name

    def TurnOff(self, name = None, id = None, ip = None):
        disp = self.GetDeviceBy(name, id, ip)
        if disp is not None:
            disp.Instance.turn_off()
        return disp.Name
    
    ##----------------------Brightness----------------------------------
    def SetBrightness(self, brightness, name = None, id = None, ip = None):
        disp = self.GetDeviceBy(name, id, ip)
        if disp is not None:
            disp.Instance.set_brightness(brightness)
        return disp.Name

    def SetBrightnessEverything(self, brightness):
        for disp in self.Devices:
            disp.Instance.set_brightness(brightness)            

    ##----------------------Color----------------------------------
    def SetColorByCustomName(self, color, name = None, id = None, ip = None):
        disp = self.GetDeviceBy(name, id, ip)
        if disp is not None:
            rgb = self.ColorDictionary[color]
            disp.Instance.set_rgb(rgb[0],rgb[1],rgb[2])
        return disp.Name

    def SetColorByCustomNameEverything(self, color):
        for disp in self.Devices:
            rgb = self.ColorDictionary[color]
            disp.Instance.set_rgb(rgb[0],rgb[1],rgb[2])
    
    def ListCustomColors(self):
        return self.ListDictionary(self.ColorDictionary)
    
    def WhiteAll(self):
        for disp in self.Devices:
            disp.Instance.send_command("set_ct_abx", params=[4000, "smooth", 500])

    def SetColorByRgb(self, rgb, name = None, id = None, ip = None):
        disp = self.GetDeviceBy(name, id, ip)
        if disp is not None:
            disp.Instance.set_rgb(rgb[0],rgb[1],rgb[2])
        return disp.Name            
    
    def SetColorByRgbEverything(self, rgb):
        for disp in self.Devices:
            disp.Instance.set_rgb(rgb[0],rgb[1],rgb[2])

    ###---------------------Flows---------------------
    def StartFlow(self, flowId, name = None, id = None, ip = None):
        disp = self.GetDeviceBy(name, id, ip)
        if disp is not None:
            flow = self.FlowDictionary[flowId]
            if flow is not None:
                disp.Instance.start_flow(Flow(count=0, transitions = flow.Flow))
                return disp.Name

    def StartFlowEverything(self, flowId):
        flow = self.FlowDictionary[flowId]
        if flow is not None:
            for disp in self.Devices:
                disp.Instance.start_flow(Flow(count=0, transitions=flow.Flow))

    def StopFlow(self, name = None, id = None, ip = None):
        disp = self.GetDeviceBy(name, id, ip)
        if disp is not None:
            disp.Instance.stop_flow()
            return disp.Name

    def StopFlowEverything(self):
        for disp in self.Devices:
            disp.Instance.stop_flow()
    
    def ListFlows(self):
        return self.ListDictionary(self.FlowDictionary, 'Name')

    ###---------------------End Flows---------------------

    ##----------------------Utils-------------------------
    def GetDeviceBy(self, name = None, id = None, ip = None):
        if name is not None:
            return next((x for x in self.Devices if x.Name == name), None)

        if id is not None:
            return next((x for x in self.Devices if x.Id == id), None)

        if ip is not None:
            return next((x for x in self.Devices if x.Ip == ip), None)
        
        return None
    
    def ListDictionary(self, dictionary, propToShow = None):
        res = ''
        for x in dictionary:
            res += str(x) + ':' +  str(dictionary[x].__getattribute__(propToShow) if propToShow else dictionary[x])  + "\n"
        return res

    def GetProperties(self):
        for disp in self.Devices:
            print(disp.Instance.get_properties())
    
    def GetPropByName(self, name):
        for disp in self.Devices:
            print(disp.Instance.send_command("get_prop", params=[name]))

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

class PrintError(object):
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

        self.Service.StartFlow(flowId = 4, id = 2)
        self.Service.StartFlow(flowId = 4, id = 1)
        time.sleep(sleepTime * 5)

        self.Service.StopFlowEverything()
        time.sleep(sleepTime)

        self.Service.WhiteAll()