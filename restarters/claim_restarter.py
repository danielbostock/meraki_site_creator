# Import area
from os import abort
from notifications import messages, errors
import time

def restart():
    restartConfirm = False
    while restartConfirm == False:
        try:
            print('\nYou have indicated that the entered information is incorrect. Would you like to abort or restart?')
            restartConfirmed = input('[a]bort or [r]estart: ').lower()
            if restartConfirmed in ('a', 'abort'):
                return restartConfirmed
            elif restartConfirmed in ('r', 'restart'):
                print(messages.RESTART_MESSAGE)
                time.sleep(3)
                restartConfirm = True
                return restartConfirm
            else:
                continue
        except ValueError:
            print(errors.SELECTION_ERROR)
            continue
