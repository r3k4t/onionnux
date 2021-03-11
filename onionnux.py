import os
import sys
import time
import socks
import requests
import pyfiglet
os.system("clear")
print (chr(27)+"[35m")
banner=pyfiglet.figlet_format("OnionNux", font = "standard")
print(banner)
print ("    Author : Rahat Khan Tusar(rkt)[BANGLADESH]")
print ("    Github : https://github.com/r3k4t ")
session=requests.session()
session.proxies={}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'
print
onionsite=raw_input("Enter a onion  site :")
start = time.time()
response=session.get(onionsite)
end = time.time()
t_time = end - start
if  response.headers["CONNECTION"]:                                                         
     print(chr(27)+"[32m"+"==[ACTIVE]==>"+chr(27)+"[35m"+response.url+chr(27)+"[32m"+"<==[SERVER]==>"+chr(27)+"[35m"+response.headers['Server'])
     print("Total Runing Time : " ,t_time,"seconds")

