import time
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
def Main():
        PageUpdate()
        time.sleep(1)


def PageUpdate():
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
        
        file=open("/var/www/html/webpage.html","w")
	      file.write("<!DOCTYPE html>")
	      file.write("<hmtl>")
	      file.write("<head>Seridor de pagina we de Python</head>")
	      file.write("<title>Updatable Page</title>")
	      file.write("<p>La temperatura es de: 18 C")
	      file.write("<p>Bit 0="+str(stat0)+"</p>")
	      file.write("<p>Bit 1="+str(stat1)+"</p>")
	      file.write("<p>Bit 2="+str(stat2)+"</p>")
	      file.write("<p>Bit 3="+str(stat3)+"</p>")
	      file.write("<p>Bit 4="+str(stat4)+"</p>")
	      file.write("<p>Bit 5="+str(stat5)+"</p>")
	      file.write("<p>Bit 6="+str(stat6)+"</p>")
	      file.write("</body>")
	      file.write("</html>")
	      file.close()
	
    
        
while(1):
        Main()
	
