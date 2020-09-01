
DYN_SIZE = 255
registers = [
('SW_VER' , 0x00, 2),
('HRD_VER' , 0x01, 2),
('INSTANCES' , 0x02, 1),
('USB_RX_BUFF_SIZE' , 0x03, 2),
('USB_TX_BUFF_SIZE' , 0x04, 2),
('USB_RX_BYTES' , 0x05, 4),
('USB_TX_BYTES' , 0x06, 4),
('USB_TX_OVERRIDE' , 0x07, 1),
('USB_RX_OVERRIDE' , 0x08, 1),
('BT_BUFF_SIZE' , 0x09, 2),
('BT_COMM' , 0x0a, 1),
('BT_BUFFER' , 0x0b, DYN_SIZE),
('BT_ADDR' , 0x0c, 4),
('NOTIF_STATUS' , 0x10, 4),
('NOTIF_MASK' , 0x11, 4),
('NOTIF_ACK' , 0x12, 4),
('USART1_RXFIFO_SIZE' , 0x13, 2),
('USART1_TXFIFO_SIZE' , 0x14, 2),
('USART1_MODE' , 0x15, 1),
('USART1_BR' , 0x16, 1),
('USART1_DATA_BITS' , 0x17, 1),
('USART1_STOP_BITS' , 0x18, 1),
('USART1_PARITY' , 0x19, 1),
('USART1_CTRL' , 0x1a, 1),
('USART1_RX_NOTIF' , 0x1b, 2),
('USART1_TX_NOTIF' , 0x1c, 2),
('USART1_RX_TIMEOUT' , 0x1d, 2),
('USART1_RX_BYTES' , 0x1e, 4),
('USART1_TX_BYTES' , 0x1f, 4),
('USART1_RX_FIFO_BYTES' , 0x20, 2),
('USART1_TX_FIFO_BYTES' , 0x21, 2),
('USART1_RX_ERROR' , 0x22, 4),
('USART1_RX_OVERRIDE' , 0x23, 1),
('USART1_RX_FIFO' , 0x24, DYN_SIZE),
('USART1_TX_FIFO' , 0x25, DYN_SIZE),
('USART2_RXFIFO_SIZE' , 0x26, 2),
('USART2_TXFIFO_SIZE' , 0x27, 2),
('USART2_MODE' , 0x28, 1),
('USART2_BR' , 0x29, 1),
('USART2_DATA_BITS' , 0x2a, 1),
('USART2_STOP_BITS' , 0x2b, 1),
('USART2_PARITY' , 0x2c, 1),
('USART2_CTRL' , 0x2d, 1),
('USART2_RX_NOTIF' , 0x2e, 2),
('USART2_TX_NOTIF' , 0x2f, 2),
('USART2_RX_TIMEOUT' , 0x30, 2),
('USART2_RX_BYTES' , 0x31, 4),
('USART2_TX_BYTES' , 0x32, 4),
('USART2_RX_FIFO_BYTES' , 0x33, 2),
('USART2_TX_FIFO_BYTES' , 0x34, 2),
('USART2_RX_ERROR' , 0x35, 4),
('USART2_RX_OVERRIDE' , 0x36, 1),
('USART2_RX_FIFO' , 0x37, DYN_SIZE),
('USART2_TX_FIFO' , 0x38, DYN_SIZE),
('SPI_BUFF_SIZE' , 0x39,  2),
('SPI_SPEED' , 0x3a,  1),
('SPI_CTRL' , 0x3b,  1),
('SPI_COMPLETED' , 0x3c,  1),
('SPI_BUFFER' , 0x3d,  DYN_SIZE),
('SPI_QUAN' , 0x3e,  2),
('I2C_BUFF_SIZE' , 0x3f,  2),
('I2C_SPEED' , 0x40, 1),
('I2C_CTRL' , 0x41,  1),
('I2C_COMPLETED' , 0x42,  1),
('I2C_BUFFER' , 0x43, DYN_SIZE),
('I2C_QUAN' , 0x44,  2),
('I2C_SLAVE_ADDR' , 0x45,  1),
('I2C_REG_ADDR' , 0x46,  1),
('IO_CONFIG' , 0x47,  32),
('IO_NOTIF' , 0x48,  4),
('IO_INPUT' , 0x49, 32),
('IO_OUTPUT' , 0x4a, 32),
('IO_LATCH_RES' , 0x4b, 32),
('IO_COUNTER1' , 0x4c, 4),
('IO_COUNTER2' , 0x4d, 4),
('IO_COUNTER3' , 0x4e, 4),
('IO_COUNTER4' , 0x4f, 4)
]


def get_register_by_name(name):
    for i in registers:
        if i[0] == name:
            return i
    raise Exception("There is no such register:"+name)
    
def get_register_by_addr(addr):
    for i in registers:
        if i[1] == addr:
            return i
    raise Exception("There is no such register:"+addr)
