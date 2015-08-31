#!/usr/bin/python2

from Adafruit_PWM_Servo_Driver import PWM
import time
import subprocess

# ===========================================================================
# Example Code
# ===========================================================================

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

def moveServos():
  pwm.setPWM(0, 0, servoMin)
  pwm.setPWM(1, 0, servoMin)
  pwm.setPWM(15, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(0, 0, servoMax)
  pwm.setPWM(1, 0, servoMax)
  pwm.setPWM(15, 0, servoMax)
  time.sleep(1)

PATH = "/home/alarm/python/"

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 275  # Min pulse length out of 4096
servoMax = 550  # Max pulse length out of 4096

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

# Setup stty
subprocess.call(["stty", "-F", "/dev/ttyAMA0", "0:4:bac:a30:3:1c:7f:15:4:0:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0"])


while (True):
  #Initial Positions
  pwm.setPWM(0, 0, ((servoMax-servoMin)/2)+servoMin)
  pwm.setPWM(1, 0, ((servoMax-servoMin)/2)+servoMin)
  pwm.setPWM(15, 0, ((servoMax-servoMin)/2)+servoMin)

  #Wait for coin op
  serial = open('/dev/ttyAMA0', 'r')
  byte = serial.read(1)

  coinNum = soundFileNum(byte)
  if coinNum != "0":
    cmd = "mpg123 "+PATH+"sounds/"+coinNum+".mp3"
    p = subprocess.Popen(cmd, shell=True)
    while (p.poll() == None):
      moveServos()

