import src.frame as fr

def test_read_frame():
    f =  fr.Frame()
    f.read_reg('HRD_VER')
    print("Frame to send :"+str(f))


    b1 = f.get_frame()
    print("Buffer to send :"+str(b1))    

    f_out =  fr.Frame()
    for i in b1:
        f_out.parse_frame(i)

    print("Frame received :"+str(f_out))    

def test_write_frame():
    f =  fr.Frame()
    f.write_reg('HRD_VER', 0x55aa)
    print("Frame to send :"+str(f))

    b1 = f.get_frame()
    print("Buffer to send :"+str(b1))    

    f_out =  fr.Frame()
    for i in b1:
        f_out.parse_frame(i)

    print("Frame received :"+str(f_out))    

def test_write_array_frame():

    f =  fr.Frame()
    f.write_reg_array('HRD_VER', [1]*32)
    print("Frame to send :"+str(f))

    b1 = f.get_frame()
    print("Buffer to send :"+str(b1))    

    f_out =  fr.Frame()
    for i in b1:
        f_out.parse_frame(i)

    print("Frame received :"+str(f_out))    


def test_read_buffer_frame():
    f =  fr.Frame()
    f.read_buffer('USART1_RX_FIFO', 64)
    print("Frame to send :"+str(f))

    b1 = f.get_frame()
    print("Buffer to send :"+str(b1))    

    f =  fr.Frame()
    f.write_buffer('USART1_TX_FIFO', [0]*64)
    print("Frame to send :"+str(f))

    b1 = f.get_frame()
    print("Buffer to send :"+str(b1))    


def test_frame():
    print("--------test_read_frame-----------")
    test_read_frame()
    print("--------test_write_frame-----------")    
    test_write_frame()
    print("--------test_write_array_frame-----------")    
    test_write_array_frame()
    print("--------test_read_buffer_frame-----------")    
    test_read_buffer_frame()
