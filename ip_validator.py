import os, ipaddress 
 
os.system('cls')
 
while True:
    ip = input('Enter IP Address: ')
    try: 
        print(ipaddress.ip_address(ip))
        print('IP Valid')
    except: 
        print('-' *50)
        print('IP is not valid')
    finally: 
        if ip =='q':
           print('Script Finished')
           break