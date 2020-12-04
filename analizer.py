from collections import Counter
import re


def save_ip(ip_adress, count):
    with open ('analysis.txt','w') as f:
        data = ip_adress + ' ' + str(count) + '\n'
        f.write(data)
        

with open ('/var/log/nginx/access.log', 'r') as f:
    list_ip = []
    while True:
        log = f.readline()
        if not log:
            break
        pattern = re.compile(r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})')
        match_ip = pattern.findall(log.strip())
        ip = '.'.join(match_ip[0])
        list_ip.append(ip)
    
    for ip in list_ip:
        counter = Counter(list_ip)
        ip_count = counter[ip]
        counter.most_common()
        save_ip(ip, ip_count)
    
    


        
        

