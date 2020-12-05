from collections import Counter

def save_ip(ip_adress, ip_count):
    with open ('analysis.txt','w') as f:
        data = ip_adress + ' ' + str(ip_count)
        f.write(data)
        
with open ('/var/log/nginx/access.log', 'r') as f:
    c = Counter()
    while True:
        log = f.readline()
        if not log:
            break
        ip = log.split(' ')[0]
        ip_count = c.update({ip: 1})
        c.most_common()
        
    for ip_address, ip_count in c.items():
        save_ip(ip_address, ip_count)


        
        

