'''
This is the core file of functions for the framework

'''
import random
from modules_repo.ascii_banners import import_banner
grap_version = "0.0.0"


def show_help_menu():
    """This is the function to show the main commands availible"""
    print("""
    
    What is Caracas.
    Caracas is a build up framework of modules to gather information 
    With Caracas you can do OSINT on your souls:
    \t*Search information on individual personal breached accounts (SOULS)
    \t*Gather information on IP addresses 
    \t*Gather information on Domain Name Service 
    \t*Gather information on Other

    Bonus information:
    \tThe name Caracas comes from the name of the Venezuelan city. One of the worlds most dangerous cities
    \tWith a high yearly kill rate
    
    How to use Caracas      
   """)

def banner():
    # verbose initalize the module
    b = import_banner
    # show random ascii art as header
    print(b.art[random.randint(0, len(b.art) - 1)])