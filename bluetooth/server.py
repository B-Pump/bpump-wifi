from bluedot.btcomm import BluetoothServer
from signal import pause

def data_received(data):
    print(data)
    server.send(data)

server = BluetoothServer(data_received)

pause()