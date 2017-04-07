# Programmed by Choyon Ahmed
# This program is intended to send proxified traffic to a specific url if needed
# facebook.com/TheChoyon
import urllib
import socket
socket.setdefaulttimeout(3)
proxies = open('proxies.txt','r').read().split('\n')
url = raw_input('Target url: ')
for i in proxies:
    try:
        if 'http://' not in i:
            i = 'http://' + i
        print urllib.urlopen(url, proxies={'http':i}).read()
    except IOError:
        continue
    except:
        continue
