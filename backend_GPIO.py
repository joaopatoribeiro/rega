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
