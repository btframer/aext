import time
import sys
import threading
import src.serial_port as sp
import src.registers as reg
import src.frame as fr



class WriteRegister:
    def __init__(self):
        self.port = None
        self.input_frame = fr.Frame()
        self.e = threading.Event()

    def set_port(self, port):
        self.port = port

    def data_received(self, data):
        for i in data:
            if (self.input_frame.parse_frame(i)):
                print("Frame received:"+str(self.input_frame))    
                self.e.set()
        
    def send(self, frame):
        port.write(frame.get_frame())
        self.e.wait(2)
        if not self.e.is_set():
            print("Error. Timeout")    
 



PORTNAME = 'COM7'
REGISTER = 'NOTIF_ACK'
VALUE = 0

def start_up():
    global PORTNAME
    global REGISTER    
    global VALUE        

    if (len(sys.argv) < 4):
        print ("Required parameters: COM_port register_name value")
        print ("python read_register.py COM3 NOTIF_ACK 0")
        print ("Register List:")
        print (reg.registers)
        sys.exit(0)
    PORTNAME = sys.argv[1]
    REGISTER = sys.argv[2]    
    VALUE = int(sys.argv[3], 0)

start_up()

parser = WriteRegister() 
port = sp.open(parser, PORTNAME)

output_frame =  fr.Frame()
output_frame.write_reg(REGISTER, VALUE)

parser.send(output_frame)

