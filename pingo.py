#!/usr/bin/python
from ipaddress import ip_network
from os import system
from threading import Thread 
threads = []
hosts = []
results = {}

NetworkHosts = ip_network(input('Enter The Network IP: ')).hosts()


def ping(host):
    result = system(f'ping -c 2 {host} >/dev/null 2>&1')
    results[host] = result 
    

def CreateThread(host):
    t = Thread(target=lambda: ping(host))
    t.start()
    threads.append(t)


for host in NetworkHosts:
    hosts.append(str(host))
    CreateThread(host)
    

# Join all the threads
for thread in threads:
    thread.join()


for key, value in results.items():
    if value == 0: 
        print(f'{key} is UP')