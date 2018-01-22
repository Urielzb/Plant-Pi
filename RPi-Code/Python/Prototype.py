import time
import datetime
import RPi.GPIO as GPIO
#Pin 11,13,15,16,18,22,29
bit0=11
bit1=13
bit2=15
bit3=16
bit4=18
bit5=22
bit6=29
GPIO.setmode(GPIO.BOARD)
#Setting GPIOs to input
GPIO.setup(bit0,GPIO.IN)
GPIO.setup(bit1,GPIO.IN)
import time
import datetime
import RPi.GPIO as GPIO
#Pin 11,13,15,16,18,22,29
bit0=11
bit1=13
bit2=15
bit3=16
bit4=18
bit5=22
bit6=29
GPIO.setmode(GPIO.BOARD)
#Setting GPIOs to input
GPIO.setup(bit0,GPIO.IN)
GPIO.setup(bit1,GPIO.IN)
GPIO.setup(bit2,GPIO.IN)
GPIO.setup(bit3,GPIO.IN)
GPIO.setup(bit4,GPIO.IN)
GPIO.setup(bit5,GPIO.IN)
GPIO.setup(bit6,GPIO.IN)
########################
def Main():
        Byte=[True,True,True,True,True,True,True]
        Byte=ReadInput(Byte)
        print(Byte)
        PageUpdate(Byte)
        time.sleep(1)
def PageUpdate(Byte):
        time=datetime.datetime.now()
        file=open("/var/www/html/webpage.html","w")
        file.write("<!DOCTYPE html>")
        file.write("<hmtl>")
        file.write("<head>")
        file.write("    <title>Pi-Plant</title>")
        file.write("</head>")
        file.write("<body>")
        file.write("    <h2>Python server with html</h2>")
        file.write("    <p>La temperatura es de: 18 C")
        file.write("    <p>Bit 0="+str(Byte[0])+"</p>")
        file.write("    <p>Bit 1="+str(Byte[1])+"</p>")
        file.write("    <p>Bit 2="+str(Byte[2])+"</p>")
        file.write("    <p>Bit 3="+str(Byte[3])+"</p>")
        file.write("    <p>Bit 4="+str(Byte[4])+"</p>")
        file.write("    <p>Bit 5="+str(Byte[5])+"</p>")
        file.write("    <p>Bit 6="+str(Byte[6])+"</p>")
        file.write("    <p>Last update time: "+str(time.hour)+":"+str(time.minute)+":"+str(time.second)+" </p>")
        file.write("</body>")
        file.write("</html>")
        file.close()

def ReadInput(Byte):
        stat0=GPIO.input(bit0)
        stat1=GPIO.input(bit1)
        stat2=GPIO.input(bit2)
        stat3=GPIO.input(bit3)
        stat4=GPIO.input(bit4)
        stat5=GPIO.input(bit5)
        stat6=GPIO.input(bit6)

        stat0= not stat0
        stat1= not stat1
        stat2= not stat2
        stat3= not stat3
        stat4= not stat4
        stat5= not stat5
        stat6= not stat6

        Byte[0]=stat0
        Byte[1]=stat1
        Byte[2]=stat2
        Byte[3]=stat3
        Byte[4]=stat4
        Byte[5]=stat5
        Byte[6]=stat6
        return Byte



while(1):
        Main()


