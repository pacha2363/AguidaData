import asyncio
from bleak import BleakClient

async def connect(address):
    async with BleakClient(address) as client:
        services = await client.get_services()
        print(f"Connected to {address}")
        for service in services:
            print(f"Service: {service.uuid}")
            for characteristic in service.characteristics:
                print(f"Characteristic: {characteristic.uuid}")

async def main():
    address = "C0:99:0D:83:95:8C"  # Replace with the address of your device
    await connect(address)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
