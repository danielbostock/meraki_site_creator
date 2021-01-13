import meraki, os

class deviceNamer:
    def __init__(self,site_name,serials):
        self.serials = serials
        self.site = site_name
        self.api = os.environ.get('meraki_api_key')
        self.dashboard = meraki.DashboardAPI(self.api)
        self_orgid = ""

    def update(self,name,serial,number):
        updated = False
        while updated == False:
            try:
                number = str(number)
                update_device = self.dashboard.devices.updateDevice(serial=(serial), name=(name + number))
                if self.serials == []:
                    print('Naming Complete')
                    updated = True
                    return updated, name
                else:
                    break
            except ValueError:
                break

    def name(self):
        complete = False
        #print(serials)
        ap = []
        sw = []
        mx = []
        while complete == False:
            for serial in (self.serials):
                get_device = self.dashboard.devices.getDevice(serial=(serial))
                get_type = get_device['model']
                if get_type in ('MR36'):
                    ap.append(serial)
                    for number, serial in enumerate(ap, start=1):
                        name = (self.site + '-AP')
                        self.update(name,serial,number)
                elif get_type in ('MS120-24P'):
                    sw.append(serial)
                    for number, serial in enumerate(sw, start=1):
                        name = (self.site + '-SW')
                        self.update(name,serial,number)
                elif get_type in ('MX67C-WW'):
                    mx.append(serial)
                    print(mx)
                    for number, serial in enumerate(mx, start=1):
                        name = (self.site + '-MX')
                        self.update(name,serial,number)
                
            complete = True