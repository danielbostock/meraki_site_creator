#Start import area
from logging import error
from notifications import errors
from site_creator import brander
from menu.clear import clear

import site_creator
# Error handling text variables

def input_checker (serials):
    print('\nPlease confirm the following list of serial numbers are correct for the devices you wish to create the site with.')
    print('\nSerial Numbers: ', serials)
    checked = str(input('\nPress enter to confirm correct, press ctrl-c to abort.') or 'y')
    clear()
    return checked


def input_type ():
    selection = False
    while selection is False:
        try:
            clear()
            selection = int(input('\n\nCurrent list of accepted input types, refer to documentation for further detail on each input type.\n1. CSV\n2. Serial Numbers\n3. Order Numbers\n\nSelect Input: '))


            if selection == 1:
                selection = 'type_csv'
                return selection
            
            if selection == 2:
                selection = 'type_serial'
                return selection

            if selection == 3:
                selection = 'type_order'
                return selection
            
            elif selection >= 4 or selection <= 0:
                selection = False
                print(errors.SELECTION_ERROR)
                continue

            else:
                print(errors.GENERAL_ERROR)
                break

        except ValueError:
            print(errors.SELECTION_ERROR)

def input_selector(inputType):
    if inputType == 'type_csv':
        serials = type_csv()
        return serials
    if inputType == 'type_serial':
        serials = type_serial()
        return serials
    if inputType == 'type_order':
        serials = type_order()
        return serials

def type_csv ():
    selection = 1
    confirmation = 0
    while confirmation == 0:
        csvfile = input('\n\nEnter the full path location to the CSV file to be used for importing devices: ')

        if selection == 1 and confirmation == 0:
            print('\n\nFile selected for importing: ' + csvfile )
            confirmation = int(input('\n\nPress enter to confirm correct, press ctrl-c to abort...') or 1)
            clear()
            if confirmation == 1:
                csv_import = brander.CsvProc(csvfile,'Serial')
                serials = csv_import.read_input()
                return serials

            elif confirmation >= 1:
                selection = 1
                confirmation = 0
                print (errors.SELECTION_ERROR)

        else:
            print (errors.SELECTION_ERROR)
            break

def type_serial ():
    counted = 0
    while counted == 0:
        count = int(input("Number of devices to import: "))
        serials = []
        for x in range(count):
            while count >0:
                try:
                    serial_check = input("Device Serial: ").upper()
                    if len(serial_check) != 14:
                        count += 1
                        counted = 0
                        print('Serial number is not a valid Meraki serial number length, please try again.')
                        continue
                    elif len(serial_check) == 14:
                        count -= 1
                        counted = 1
                        serials.append(serial_check)
                    else:
                        print(errors.SERIAL_ERROR)

                except ValueError:
                    print(errors.SELECTION_ERROR)
                    continue

                else:
                    break
        return serials


def type_order ():
    confirmation = 0
    counted = 0
    while counted == 0:
        count = int(input("Order number to import: "))
        ordernum = []
        for x in range(count):
            while count >0:
                try:
                    ordernum_check = input("Meraki Order Number: ").upper()
                    if len(ordernum_check) != 9:
                        count += 1
                        counted = 0
                        print('Order number is not a valid Meraki order number length, please try again.')
                        continue
                    if len(ordernum_check) == 9:
                        count -= 1
                        counted = 1
                        ordernum.append(ordernum_check)
                        break

                except ValueError:
                    print('Please enter a valid order number')
                    continue
                

                else:
                    break
            
        if confirmation == 0 and counted == 1:
            input_checker(confirmation, counted, ordernum)
            return confirmation, counted, ordernum
