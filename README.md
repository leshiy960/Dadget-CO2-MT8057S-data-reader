# Dadget-CO2-MT8057S-data-reader
Very simple script for reading data from MT8057S without decryption data.

Tested on Raspberry pi 3B+ (armv7l) and Manjaro Linux (x86) with MT8057S revision 03.2021.

## Requirements:

```bash
sudo apt install libusb-1.0-0-dev libudev-dev
sudo pip3 install hidapi
```

## Example:

```python
import hid

def get_co2(device):
    while True:
        data = device.read(8)
        if data[0] == 0x50:
            return (data[1] << 8) + data[2]

def get_temp(device):
    while True:
        data = device.read(8)
        if data[0] == 0x42:
            return ((data[1] << 8) + data[2]) * 0.0625 - 273.15


devices = [(x['vendor_id'], x['product_id'], x['product_string']) for x in hid.enumerate() if x['product_string'] == 'USB-zyTemp']
if devices:
    device = devices[0]
    try:
        print(device)
        h = hid.device()
        h.open(vendor_id=device[0], product_id=device[1])
        h.send_feature_report([0,0,0,0,0,0,0,0])
        print('Device connected', device[0], device[1])
    except Exception as e:
        print('Error', e)
else:
    print('Device not found')
    exit()

print(get_co2(h), get_temp(h))
h.close()
```

## Output

```bash
pi@malina3:~ $ sudo python3 main.py 
835 22.037500000000023
pi@malina3:~ $ 
```

