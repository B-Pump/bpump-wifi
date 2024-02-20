from bluedot.btcomm import BluetoothClient
from signal import pause

def data_received(data):
    print(data)

client = BluetoothClient("name_of_your_server", data_received)
client.send("helloworld")

pause()