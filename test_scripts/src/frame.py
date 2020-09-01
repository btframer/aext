from enum import Enum
import src.registers as reg
from cobs import cobs

class FrameType(Enum):
    Read = 0
    Response = 1
    Write = 2
    Ack = 3
    NoAck = 4
    Event = 5
    Undef = 99
    



class Frame:

    def __init__(self):
        self.frame_size = 0
        self.frame_type = FrameType.Undef
        self.opt = 0
        self.addr = 0        
        self.payload_size = 0                
        self.payload = bytearray()
        self.rec_buff = bytearray()
        self.read_info = None

    def __str__(self):
        return f'Frame[frame_size={self.frame_size},frame_type={self.frame_type},opt={hex(self.opt)},addr={hex(self.addr)},payload_size={self.payload_size},payload={self.payload}]'

    # setting type, address, payload  of the frame and calculate size 
    def set_type(self, frame_type, addr, payload_size = 0, payload = None):
        self.frame_type = frame_type
        self.addr = addr
        self.payload_size = payload_size
        self.payload.clear()
        if payload:
            self.payload += payload
        self.frame_size = 8 + len(self.payload)


    def read_reg(self, name):
        r = reg.get_register_by_name(name)
        self.set_type(FrameType.Read, r[1])

    def read_buffer(self, name, size):
        r = reg.get_register_by_name(name)
        if (r[2] != reg.DYN_SIZE):
            raise Exception("Only buffer or FIFO can be read")
        self.set_type(FrameType.Read, r[1], size)
        pass

    def write_reg(self, name, value, opt=1):
        self.opt = opt
        r = reg.get_register_by_name(name)
        if (r[2] > 4):
            raise Exception("Register size to long. Use write_reg_array function.")

        v = (value).to_bytes(r[2], byteorder='little')
        self.set_type(FrameType.Write, r[1], 0, v)

    def write_reg_array(self, name, value, opt=1):
        self.opt = opt        
        r = reg.get_register_by_name(name)
        if (r[2] > len(value)):
            raise Exception("Value size incorrect. Expected size " + str(r[2]) + " bytes")

        self.set_type(FrameType.Write, r[1], 0, bytearray(value))



    def write_buffer(self, name, value, opt=1):
        self.opt = opt        
        r = reg.get_register_by_name(name)
        if (r[2] != reg.DYN_SIZE):
            raise Exception("Only buffer or FIFO can be write")

        self.set_type(FrameType.Write, r[1], len(value), bytearray(value))


    def get_payload(self):
        return bytes(self.payload)

    def get_value(self):
        if not self.read_info:
            return 0
        result = 0
        if self.read_info[2] > 4:
            raise Exception("Register size to long. Use get_payload function.")
        else:
            result = int.from_bytes(self.payload[0:self.read_info[2]], "little")        
        return result


    # getting a frame ready for sending to port
    def get_frame(self):
        result =[0] * self.frame_size
        b = self.frame_size.to_bytes(2, byteorder="little")
        result[0] = b[0]
        result[1] = b[1]
        result[2] = self.frame_type.value
        result[3] = self.opt
        b = self.addr.to_bytes(2, byteorder="little")
        result[4] = b[0]
        result[5] = b[1]
        b = self.payload_size.to_bytes(2, byteorder="little")
        result[6] = b[0]
        result[7] = b[1]
        index = 8
        for i  in self.payload:
            result[index] = i
            index += 1
        #cobs encoded ----- 
        encoded = cobs.encode(bytearray(result))
        return [*encoded, *[0]]


    def parse_frame(self, byte):
        if byte != 0: 
            self.rec_buff.append(byte)
            return False
        #cobs decoded ----
        result = cobs.decode(self.rec_buff)
  
        self.frame_size = (result[1] << 8) or result[0]
        self.frame_type = FrameType(result[2])
        self.opt = result[3]
        self.addr = (result[5] << 8) or result[4]
        self.payload_size = (result[7] << 8) or result[6]
        self.payload.clear()
        self.payload += result[8:]
        self.rec_buff.clear()
        self.read_info = reg.get_register_by_addr(self.addr)
        return True

    def parse_buffer_frame(self, buffer):
        for i in buffer:
            self.parse_frame(i)
