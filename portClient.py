import serial
# connect
port = serial.Serial('COM21')
if port.isOpen:
    #step: start
    port.write(bytearray([9]))
    #step 1
    ack=port.read()
    if ord(ack)==1:
        w=port.read();
        port.write(bytearray([2*ord(w)]))
    #step 2
    ack=port.read()
    if ord(ack)==1:
        m=port.read();
        port.write(bytearray([ord(m)+2]))
    #step 3
    ack=port.read()
    if ord(ack)==1:
        n=port.read();
        port.write(bytearray([2*ord(n)+10]))
