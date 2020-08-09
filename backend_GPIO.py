import RPi.GPIO as GPIO


class Relay(object):
    def __init__(self,pin,name):
        self.pin = pin
        self.name name

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin,GPIO.OUT, initial=GPIO.HIGH)

    def start(self):
        try:
            GPIO.output(self.pin,GPIO.LOW)
        except:
            return False
        return True
    def stop(self):
        try:
            GPIO.output(self.pin,GPIO.LOW)
        except:
            return False
        return True
class DHT_SENSOR (object):
    def __init__(self, pin):
        self.pin = pin
        self.temperature,self.humidity = DHT.read(DHT.DHT11,self.pin)
    def read(self):
        try :
            self.temperature, self.humidity = DHT.read(DHT.DHT11, self.pin)
        except:
            return False
        return (self.temperature, self.humidity)

class READ_CPU_TEMP (object):
    def __init__(self):
        self.cpu_temp = self.read_cpu_temp()

    def read_cpu_temp(self):
        tfile=open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(tfile.read())
        tempC= temp/1000
        tfile.close()
        return tempC