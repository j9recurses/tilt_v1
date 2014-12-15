import bluetooth
import sys
bd_addr = "00:06:66:67:E1:66" #itade address

port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print 'Connected'
sock.settimeout(1.0)
sock.send("x")
print 'Sent data'

data = sock.recv(1)
print 'received [%s]'%data

sock.close()
