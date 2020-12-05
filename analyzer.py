from collections import Counter

def save_ip(data):
    with open ('analysis.txt','w') as f:
        for i in data:
            register = i[0] + ' ' + str(i[1]) + '\n'
            f.write(register)
        
with open ('/var/log/nginx/access.log', 'r') as f:
    c = Counter()
    while True:
        log = f.readline()
        if not log:
            break
        ip = log.split(' ')[0]
        ip_count = c.update({ip: 1})
    sorted_c = {}
    sorted_ip_c = sorted(c, key=c.get, reverse=True)
    for addr in sorted_ip_c:
        sorted_c[addr] = c[addr]
    data = [(ip_address, ip_count) for ip_address, ip_count in sorted_c.items()]
    save_ip(data)


        
        

