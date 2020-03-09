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
print('終了')

def getTime():
    n=time.strftime('%I')+time.strftime('%M')
    timeList=list(n)
    return timeList

def setAmPm
    ap =time.strftime('%p')
    if ap =='AM':
        turnlight(20,1)
        turnLight(21,0)
    else:
        turnLigut(20,0)
        turnLight(21,1)

def switchLight(gpio,number):
    GPIO.setup(gpio,GPIO.OUUT)
    if number == 0 :
        GPIO.output(gpio,GPIO.HIGH)
    else:
        GPIO.output(gpio,GPIO.LOW)

def lightNumber(number,cnt):
    