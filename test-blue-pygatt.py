import asyncio
from bleak import BleakScanner

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

loop = asyncio.get_event_loop()
loop.run_until_complete(scan())