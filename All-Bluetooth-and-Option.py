import asyncio
from bleak import BleakScanner, BleakClient

async def scan():
    devices = await BleakScanner.discover()
    print(f"Found {len(devices)} devices.")
    for i, device in enumerate(devices):
        print(f"{i + 1}: Name={device.name}, "
              f"Address={device.address}, "
              f"Device Type: {device.metadata['uuids']}, "
              f"RSSI={device.rssi}, "
              f"Advertisement Data={device.metadata['manufacturer_data']}")
        print("\n")
    return devices

async def connect(address):
    async with BleakClient(address) as client:
        services = await client.get_services()
        print(f"Connected to {address}")
        for service in services:
            print(f"Service: {service.uuid}")
            for characteristic in service.characteristics:
                print(f"Characteristic: {characteristic.uuid}")

async def main():
    devices = await scan()
    while True:
        try:
            device_num = int(input("Choose a device number to connect to: "))
            if 1 <= device_num <= len(devices):
                address = devices[device_num - 1].address
                await connect(address)
                break
            else:
                print("Invalid device number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
