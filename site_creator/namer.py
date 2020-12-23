# Start Import Area

# End Import Area

class SiteName:
    def __init__(self, brand, country, site):
        self.brand = brand
        self.country = country
        self.site = site
    
    def create(self):
        name = (self.brand + '-' + self.country + '-' + self.site)
        print('\n' + name)
        return name
        

#site = site_name("FF","AUS","WYNNUM")
#site.site_name_create()