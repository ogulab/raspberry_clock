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


#辞書
books={"小説":"a","料理":"b","辞書":"c"}
print(books["料理"])    
#辞書タプ
print(sorted(books.items()))

#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
originalstr='stressed'
newstrlist=list(reversed(originalstr))
print(newstrlist)


