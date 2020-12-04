from collections import Counter


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
        print(f'{ip_address}: {ip_count}')
