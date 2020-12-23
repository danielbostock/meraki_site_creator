# Start Import Area
from notifications.errors import SELECTION_ERROR
from menu.text import BRAND, COUNTRY, CREATE_SITE_TEXT, TOP_SELECT_TEXT, SITE_NAME, SITE_NAME_CONFIRM, RESTART, COMPLETE,STANDARD_ENTER, TOP_TEXT
from meraki_importer.importer import importer
import site_creator.brander, site_creator.namer, site_creator.network
from menu.clear import clear

# Temp test text
temp_text1 = 'You have made a selection thats not ready yet'
brandscsv = 'config/site_data/brands.csv'


def text_menu():
    def selector():
        selection = int(input(STANDARD_ENTER) or "1")
        return selection
    def country_selector(brand): #This selected needs to be refind to obtain a list of the countries available to that brand rather than displaying all possible countries
        clear()
        country_selection = int(input((brand) + ' is in the following countries.\n1. COUNTRY1 \n2. COUNTRY 2\n3. COUNTRY3\n4. COUNTRY4\n' + (COUNTRY)))
        if country_selection == 1:
            country = 'C1'
            return country
        elif country_selection == 2:
            country = 'C2'
            return country
        elif country_selection == 3:
            country = 'C3'
            return country
        elif country_selection == 4:
            country = 'C4'
            return country
        else:
            print(SELECTION_ERROR)

    l1_selected = False
    while l1_selected == False:
        clear()
        print(TOP_TEXT)
        print(TOP_SELECT_TEXT)
        selection = selector()
        clear()
        if selection == 1:
            serials = importer()
            l1_selected = True
            l2_selected = False
            while l2_selected == False:
                print(CREATE_SITE_TEXT)
                brands_list = site_creator.brander.CsvProc(brandscsv,'Brand')
                brands_list.read()
                brand = int(input(BRAND))
                if brand == 1:
                    l2_selected = True
                    complete = False
                    brand = 'B1'
                    country = 'C1'
                    clear()
                    site = input(SITE_NAME).upper()
                    while complete == False:
                        name = site_creator.namer.SiteName(brand,country,site)
                        site_name = name.create()
                        confirm = int(input(SITE_NAME_CONFIRM) or 1)
                        if confirm == 1:
                            create_site = site_creator.network.orgNetwork(site_name,serials)
                            create_site.create()
                            complete = True
                            clear()
                            print(COMPLETE)
                            return complete
                        elif confirm != 1:
                            print(RESTART)

                        else:
                            break
                
                elif brand == 2:
                    l2_selected = True
                    complete = False
                    brand = 'B2'
                    country = 'C1'
                    clear()
                    site = input(SITE_NAME).upper()
                    while complete == False:
                        name = site_creator.namer.SiteName(brand,country,site)
                        site_name = name.create()
                        confirm = int(input(SITE_NAME_CONFIRM) or 1)
                        if confirm == 1:
                            create_site = site_creator.network.orgNetwork(site_name, serials)
                            create_site.create()
                            complete = True
                            clear()
                            print(COMPLETE)
                            return complete
                        elif confirm != 1:
                            print(RESTART)

                        else:
                            break
                
                elif brand == 3:
                    l2_selected = True
                    complete = False
                    brand = 'B3'
                    site = input(SITE_NAME).upper()
                    while complete == False:
                        country = country_selector(brand)
                        clear()
                        name = site_creator.namer.SiteName(brand,country,site)
                        site_name = name.create()
                        confirm = int(input(SITE_NAME_CONFIRM) or 1)
                        if confirm == 1:
                            create_site = site_creator.network.orgNetwork(site_name, serials)
                            create_site.create()
                            clear()
                            print(COMPLETE)
                            complete = True
                            return complete
                        elif confirm != 1:
                            print(RESTART)

                    else:
                        break
                

        else:
            break
#    return top_select_complete,selection

    
    