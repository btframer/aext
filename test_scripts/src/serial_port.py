import sys
import io
import serial
import serial.threaded

write_to_file = True
file_name = "input.bin"

class SerialReader(serial.threaded.Protocol):
    def __init__(self):
        self.ser = None
        self.serial_worker = None
        self.parser = None


    def __call__(self):
        return self

    def data_received(self, data):
        if write_to_file:
            f = io.open(file_name, "ab")
            f.write(bytearray(data))
            f.close()
        self.parser.data_received(data)

    def open(self, port, br, parser):
        self.parser = parser
        self.parser.set_port(self)
        self.ser = serial.serial_for_url(port, do_not_open=True, baudrate = br, parity = 'N', bytesize=8, timeout=0)
        self.ser.open()
        self.serial_worker = serial.threaded.ReaderThread(self.ser, self)
        self.serial_worker.start()
        print(f'Serial port opened port={port} baudrate={br}')

    def write(self, data):
        self.ser.write(data)

    def close(self):
        self.serial_worker.stop()
        self.ser.close()

PORTNAME = 'COM7'
BAUDRATE = 115200

def start_up():
    global PORTNAME
    if (len(sys.argv) < 2):
        print ("Required parameters: COM port")
        print ("python script.py COM3")
        sys.exit(0)

    if (len(sys.argv) >= 2):
        PORTNAME = sys.argv[1]
        print ("PORTNAME:" + PORTNAME)


def open(parser):
    port = SerialReader()
    port.open(PORTNAME, BAUDRATE, parser)
    return port
