# Start Module Import area
from menu.clear import clear
from restarters.claim_restarter import restart
import requests, meraki, os
from notifications import errors
from meraki.config import API_KEY_ENVIRONMENT_VARIABLE
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# End Module Import area

#Meraki Environment Variables
# These are host specific, follow documentation to ensure these variables can be used
api_key =  os.environ.get('meraki_api_key')
dashboard = meraki.DashboardAPI(api_key)
my_orgs = dashboard.organizations.getOrganizations()
org_id = 000000

def claim_serials(serials):
    print('Claiming Serials:',serials)
    response = dashboard.organizations.claimIntoOrganization(org_id, serials=(serials))

def claim_identify(serials):
    devices = []
    identified = False
    for serial in serials:
        response = dashboard.organizations.getOrganizationInventoryDevice(org_id, serial)
        added_device = response['model']
        devices.append(added_device)
    clear()
    print('\nConfirm all the models of hardware that will be imported.\n')
    print('\nDevice Models to be added:', devices)
    while identified == False:
        try:
            identified = str(input('\n\nPress enter to confirm correct, press ctrl-c to abort.') or 'y').lower()
            clear()
            if identified in ('y', 'yes'):
                identified = True
                return identified
            else:
                print(errors.SELECTION_ERROR)
                claimed = False
                return claimed
        except ValueError:
            print(errors.GENERAL_ERROR)