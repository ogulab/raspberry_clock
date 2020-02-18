import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
for x in xrange(5):
    GPIO.output(4,True)
    print('点灯')
    time.sleep(2)
    GPIO.output(4,False)
    print('消灯')
    time.sleep(2)
GPIO.cleanup()


def getTime():
    n=time.strftime('%I')+time.strftime('%M')
    timeList=list(n)
    return timeList

def setAmPm
    ap =time.strftime('%p')
    