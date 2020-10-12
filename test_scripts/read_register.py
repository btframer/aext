import time
import sys
import threading
import src.serial_port as sp
import src.registers as reg
import src.frame as fr



class ReadRegister:
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
                print("value:"+hex(self.input_frame.get_value()))
                self.e.set()
        
    def send(self, frame):
        port.write(frame.get_frame())
        self.e.wait(2)
        if not self.e.is_set():
            print("Error. Timeout")    
 



REGISTER = 'HRD_VER'
def start_up():
    global REGISTER    

    if (len(sys.argv) < 3):
        print ("Required parameters: COM_port register_name")
        print ("python read_register.py COM3 HRD_VER")
        print ("Register List:")
        print (reg.registers)
        sys.exit(0)
    REGISTER = sys.argv[2]    

start_up()
sp.start_up()

parser = ReadRegister() 
port = sp.open(parser)

output_frame =  fr.Frame()
output_frame.read_reg(REGISTER)

parser.send(output_frame)

