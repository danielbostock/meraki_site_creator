## Import Area
from restarters.claim_restarter import restart
from meraki_importer import device_serials, device_importer
from notifications import messages, errors

def importer():
    claim_complete = False

    while claim_complete == False:

        # Determine how the SD WAN Devices will be deployed

        # Define file type and create serial list with file type
        serials_complete = False
        while serials_complete == False:
            input_type = device_serials.input_type()
            if input_type == 'type_csv':
                serials = device_serials.type_csv()
                check = False
                while check == False:
                    checked = device_serials.input_checker(serials)
                    if checked in ('y' or 'yes'):
                        check = True
                        claimed = False
                        if claimed == False:
                            print(messages.DEVICES_ADDED_MESSAGE)
                            claim = device_importer.claim_serials(serials)
                            identified = device_importer.claim_identify(serials)
                            if identified == False:
                                restart_confirmed = ()
                                print (restart_confirmed)
                                if restart_confirmed == True:
                                    claim_complete = True
                                    break
                                elif restart_confirmed in ('a', 'abort'):
                                    claim_complete = True
                            elif identified == True:
                                claim_complete = True
                                return serials
                        elif claimed == True:
                            check = True
                        
                        else:
                            restart_confirmed = restart()
                            claim_complete = True          
                        break
                    elif checked in ('n' or 'no'):
                        check = True
                        break
                else:
                    print(errors.GENERAL_ERROR)
                    break
            if input_type == 'type_serial':
                    serials = device_serials.type_serial()
                    check = False
                    while check == False:
                        checked = device_serials.input_checker(serials)
                        if checked in ('y' or 'yes'):
                            check = True
                            claimed = False
                            if claimed == False:
                                print(messages.DEVICES_ADDED_MESSAGE)
                                claim = device_importer.claim_serials(serials)
                                identified = device_importer.claim_identify(serials)
                                if identified == False:
                                    restart_confirmed = restart()
                                    print (restart_confirmed)
                                    if restart_confirmed == True:
                                        claim_complete = True
                                        return serials
                                        
                                    elif restart_confirmed in ('a', 'abort'):
                                        claim_complete = True

                                elif identified == True:
                                    claimed = True
                                    return serials
                            elif claimed == True:
                                check = True
                                return serials
                        
                            else:
                                restart_confirmed = restart()
                                claim_complete = True

                        if check == True:
                            print(messages.IMPORT_CHECKS_COMPLETE)
                            serials_complete = True
                            claim_complete = True
                            return serials

                        elif checked in ('n' or 'no'):
                            check = True
                            restart_confirmed = restart()
                            claim_complete = True
                    return serials
                
                    #else:
                    #    print(errors.GENERAL_ERROR)
                    #    break

            elif input_type == 'type_order':
                serials = device_serials.type_order()
                check = False
                while check == False:
                    checked = device_serials.input_checker(serials)
                    if checked in ('y' or 'yes'):
                        type_completed = True
                        check = True
                        break
                    elif checked in ('n' or 'no'):
                        check = True
                        break
                else:
                    print(errors.GENERAL_ERROR)
                    break