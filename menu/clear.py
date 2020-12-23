#Start Import Area
from os import system, name 
from time import sleep 
#End Import Area
  
# define our clear function 
def clear(): 
  
    # Windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # Unix Distros (Including MacOS)
    else: 
        _ = system('clear') 