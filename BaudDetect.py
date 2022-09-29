import asyncio
import canopen
import can
import pyttsx3
import time

def sayText(words):
    engine = pyttsx3.init()
    engine.setProperty('rate',200)
    engine.setProperty('volume',1.0)
    engine.setProperty('voice','com.apple.speech.synthesis.voice.tingting')
    engine.say(words)
    engine.runAndWait()
    engine.stop()

async def findDevice(baud):
    isFindDevice = False
    network = canopen.Network()
    BusScanner = canopen.network.NodeScanner(network)
    network.connect(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=baud)
    network.nmt.send_command(0x01)
    await asyncio.gather(search(network),receiveDate(250000))

async def search(network):
    limit = 127
    sdo_req = b"\x40\x00\x10\x00\x00\x00\x00\x00"
    for node_id in range(1, limit + 1):
            network.send_message(0x600 + node_id, sdo_req)
            time.sleep(0.3)

async def receiveDate(baud):
    bus = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=baud)
    msg = bus.recv(1)
    while(True):
        if msg is not None:
            print(msg) 
    

def searchBaud():
    baudList = {100000,500000,250000,1000000,250000,50000,20000,125000}
    for baud in baudList:
        isFindDevice = findDevice(baud)
        if(isFindDevice == True):
            if(baud == 10000):
                print("baud num is 1")
                sayText(f"波特率ID为1")
            elif(baud == 20000):
                print("baud num is 2")
                sayText(f"波特率ID为2")
            elif(baud == 50000):
                print("baud num is 3")
                sayText(f"波特率ID为3")
            elif(baud == 100000):
                print("baud num is 4")
                sayText(f"波特率ID为4")
            elif(baud == 125000):
                print("baud num is 5")
                sayText(f"波特率ID为5")
            elif(baud == 250000):
                print("baud num is 6")
                sayText(f"波特率ID为6")
            elif(baud == 500000):
                print("baud num is 7")
                sayText(f"波特率ID为7")
            elif(baud == 1000000):
                print("baud num is 8 or 0 other number ")
                sayText(f"波特率ID为8或者0或者其他")

if __name__ == "__main__":
    asyncio.run(findDevice(250000))