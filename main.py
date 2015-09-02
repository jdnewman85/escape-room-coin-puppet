#!/usr/bin/python2

from Adafruit_PWM_Servo_Driver import PWM
import time
import subprocess
from Animation import *

#FUNCTIONS
def soundFileNum(x):
    return {
            chr(1): "1",
            chr(2): "2",
            chr(3): "3",
            chr(4): "4",
            chr(5): "5",
            chr(6): "6",
    }.get(x, "0")

#CLASSES
class Servo:
    def __init__(self, channel, minAngle, maxAngle, minPulseLen, maxPulseLen):
        self.channel = channel
        self.minAngle = minAngle
        self.maxAngle = maxAngle
        self.minPulseLen = minPulseLen
        self.maxPulseLen = maxPulseLen
        self.converter = Converter(maxAngle, minAngle, minPulseLen, maxPulseLen)

    def setAngle(self, angle)
        pwm.setPWM(self.channel, 0, int(self.converter.convert(angle))




#MAIN
PATH = "/home/alarm/python/"

pwm = PWM(0x40)

#servoMin = 275  # Min pulse length out of 4096
#servoMax = 550  # Max pulse length out of 4096

#Big Servo
#servoMin = 130 #90
#servoMax = 630 #-90

#Small Servo
#servoMin = 200  #-73
#servoMax = 600  #73

armServo = Servo(15, 90, -90, 130, 630)
mouthServo = Servo(1, 73, -73, 200, 600)
eyeServo = Servo(0, 73, -73, 200, 600)

pwm.setPWMFreq(60)  # Set frequency to 60 Hz

# Setup stty
subprocess.call(["stty", "-F", "/dev/ttyAMA0",
    "0:4:bac:a30:3:1c:7f:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0"])

while (True):
  #Initial Positions
  armServo.setAngle(0)
  mouthServo.setAngle(0)
  eyeServo.setAngle(0)

  #Wait for coin op
  serial = open('/dev/ttyAMA0', 'r')
  byte = serial.read(1)

  coinNum = soundFileNum(byte)
  if coinNum != "0":
    cmd = "mpg123 "+PATH+"sounds/"+coinNum+".mp3"
    p = subprocess.Popen(cmd, shell=True)
    while (p.poll() == None):
      moveServos()

