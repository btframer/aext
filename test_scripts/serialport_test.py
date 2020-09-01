import sys
import time
import threading
import src.serial_port as sp


TESTDATA = b'123456789abcdABCD!@#$'

e = threading.Event()

class LoopBack:
    def __init__(self):
        self.port = None
        self.buffer = bytearray()
    def set_port(self, port):
        self.port = port
    def data_received(self, data):
        self.buffer += data
        if (len(self.buffer) == len(TESTDATA)):
            if (self.buffer == TESTDATA):
                print("OK. Test passed")
            else:
                print("Error.There were errors during the test.")
            e.set()

    def data_send(self, data):
        self.buffer.clear()
        port.write(data)
 


#sp.start_up()
parser = LoopBack() 
port = sp.open(parser)


parser.data_send(TESTDATA)

#wait for finished
e.wait(3)
if (not e.is_set()):
    print("Error. Timeout")    



