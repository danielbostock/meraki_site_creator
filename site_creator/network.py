# Start Import Area
import meraki, os
# End Import Area

class orgNetwork:
    def __init__(self, site_name, serials):
        self.site_name = site_name
        self.organization_id = ''
        #self.timeZone = 'Australia/Brisbane' #Optional - If not assigned Meraki will do their default which is LA time.
        #self.tags = ['TEST'] #Optional
        self.productTypes = ['appliance', 'switch', 'wireless'] #When one or more product type is entered, the network is changed to combined
        api_key =  os.environ.get('meraki_api_key')
        self.dashboard = meraki.DashboardAPI(api_key)
        self.serials = serials
        self.networkId = ''
        self.templateId =''
    def create(self):
        new_network = self.dashboard.organizations.createOrganizationNetwork(organizationId=(self.organization_id), name=(self.site_name), productTypes=(self.productTypes), tags=(self.tags), timeZone=(self.timeZone))
        network_id = new_network
        self.networkId = network_id['id']
        claim = self.dashboard.networks.claimNetworkDevices(networkId=(self.networkId), serials=(self.serials))
        bind = self.dashboard.networks.bindNetwork(networkId=(self.networkId), configTemplateId=(self.templateId))