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
        print('Подключено устройство', device[0], device[1])
    except Exception as e:
        print(e)
        print('Не удалось подключиться')
else:
    print('Устройсто не найдено')
    exit()

print(get_co2(h), get_temp(h))
h.close()
