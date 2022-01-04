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

h = hid.Device(0x04d9, 0xa052)
print(get_co2(h), get_temp(h))
h.close()
