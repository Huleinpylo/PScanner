#!usr/bin/evn python
import optparse
import colorama
from colorama import Fore, Back, Style
from optparse import Option
from numpy import argsort, int64
import pandas as pd
import socket
import time
from queue import Queue
import threading
from datetime import datetime
from socket import getservbyport
#Initialize colorama
colorama.init(autoreset=True)
#https://linuxhint.com/colorama-python/
df = pd.read_csv('tcp.csv')
queue = Queue()
# Pour le multithreading
Sesame = []  
# Sesame sont les ports ouverts
Target=socket.gethostbyname(input("Votre ip ou domain: "))
portallb = 1
portalle = 65535

my_time = datetime.now()
my_time_read = my_time.strftime("%H:%M:%S")

def PortScan(port):
    s = socket.socket()
    s.settimeout(5)
    result = s.connect_ex((Target, port))
    if result == 0:
        print(Fore.GREEN +"port open", port)
        port_str=str(port)
        try:
            print(Fore.GREEN + getservbyport(port,"tcp"))
        except:
            print(Fore.RED + "unable to determine")
        #print(Fore.GREEN +(df.loc[df["port"]  == port_str]))
    s.close()

def worker():
    while not queue.empty():
        port = queue.get()
        if PortScan(port):
            Sesame.append(port)



def run_scanner(threads):
    for port in range(portallb, portalle+1):
        queue.put(port)
    
    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
def main():
    
    print(Back.RED + Fore.BLUE +"-"*50)
    print(Style.RESET_ALL)
    print(Fore.CYAN +'''
    SSSSSSSSSSSSSSS                                                                                                                   
    SS:::::::::::::::S                                                                                                                  
    S:::::SSSSSS::::::S                                                                                                                  
    S:::::S     SSSSSSS                                                                                                                  
    S:::::S                cccccccccccccccc  aaaaaaaaaaaaa   nnnn  nnnnnnnn    nnnn  nnnnnnnn        eeeeeeeeeeee    rrrrr   rrrrrrrrr   
    S:::::S              cc:::::::::::::::c  a::::::::::::a  n:::nn::::::::nn  n:::nn::::::::nn    ee::::::::::::ee  r::::rrr:::::::::r  
    S::::SSSS          c:::::::::::::::::c  aaaaaaaaa:::::a n::::::::::::::nn n::::::::::::::nn  e::::::eeeee:::::eer:::::::::::::::::r 
    SS::::::SSSSS    c:::::::cccccc:::::c           a::::a nn:::::::::::::::nnn:::::::::::::::ne::::::e     e:::::err::::::rrrrr::::::r
        SSS::::::::SS  c::::::c     ccccccc    aaaaaaa:::::a   n:::::nnnn:::::n  n:::::nnnn:::::ne:::::::eeeee::::::e r:::::r     r:::::r
        SSSSSS::::S c:::::c               aa::::::::::::a   n::::n    n::::n  n::::n    n::::ne:::::::::::::::::e  r:::::r     rrrrrrr
                S:::::Sc:::::c              a::::aaaa::::::a   n::::n    n::::n  n::::n    n::::ne::::::eeeeeeeeeee   r:::::r            
                S:::::Sc::::::c     ccccccca::::a    a:::::a   n::::n    n::::n  n::::n    n::::ne:::::::e            r:::::r            
    SSSSSSS     S:::::Sc:::::::cccccc:::::ca::::a    a:::::a   n::::n    n::::n  n::::n    n::::ne::::::::e           r:::::r            
    S::::::SSSSSS:::::S c:::::::::::::::::ca:::::aaaa::::::a   n::::n    n::::n  n::::n    n::::n e::::::::eeeeeeee   r:::::r            
    S:::::::::::::::SS   cc:::::::::::::::c a::::::::::aa:::a  n::::n    n::::n  n::::n    n::::n  ee:::::::::::::e   r:::::r            
    SSSSSSSSSSSSSSS       cccccccccccccccc  aaaaaaaaaa  aaaa  nnnnnn    nnnnnn  nnnnnn    nnnnnn    eeeeeeeeeeeeee   rrrrrrr            
    ''')  
    print(Style.RESET_ALL)                                                                                                                              
    print(Back.RED + Fore.BLUE +"-"*50)
    print(Style.RESET_ALL)

    """ parser = optparse.OptionParser('Script Usage:'+'-H <target host> -p <target port>')
    
    parser.add_option('-H', dest='tgt_Host', type='string',  help='specify target host')

    parser.add_option('-L', dest='PortRapdb', type='int',   help='specify Low port')
    
    parser.add_option('-P', dest='PortRapde', type='int',    help='specify High Port')
    
    (options,argsort) = parser.parse_args()
    tgtHost = options.tgtHost
    PortRapdb = options.PortRapdb
    PortRapde = options.PortRapde
    #if (tgtHost == None) | (PortRapde == None) | (PortRapdb == None):
    #    print parser.usage
    #    exit(0)
    
    ports = tgtPorts.strip("'").split(',')
    """
    st = time.time()
    my_time = datetime.now()
    my_time_read = my_time.strftime("%H:%M:%S")
    print(Fore.RED + Style.BRIGHT+f"Scan commence a : ",my_time_read)
    print(Style.RESET_ALL)
    run_scanner(45)
    print(Style.RESET_ALL)

    my_time_end = datetime.now()
    my_time_end_read = my_time_end.strftime("%H:%M:%S")
    print(Fore.RED + Style.BRIGHT + f"Scan fini a : ",my_time_end_read)
    et = time.time()
    elapsed_time = et - st
    # https://pynative.com/python-get-execution-time-of-program/
    print(f"Scan  a  pris : ",elapsed_time,' seconds')

if __name__ == '__main__':
        main()