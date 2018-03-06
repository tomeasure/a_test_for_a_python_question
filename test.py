log = open('access.log', 'r')
data = log.read()
log.close()

data = data.split('\n')
data = [data[i].split('\t') for i in range(len(data))]

def show_top_2(data):
    urls = [data[i][1] for i in range(len(data))]

    urls_set = set(urls)

    urls_dict = {item: urls.count(item) for item in urls_set}

    result = sorted(urls_dict.items(), key = lambda x:x[1], reverse=True)
    print("top2(url & times): ", result[0:2])

show_top_2(data)

def datetime_timestamp(dt):
    import time
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

start = datetime_timestamp('2018-03-06 03:00:00')
end = datetime_timestamp('2018-03-06 05:30:00')

# new_data = []
# for i in range(len(data)):
    # if int(data[i][2]) > start and int(data[i][2]) < end:
        # new_data.append(data[i])
new_data = [data[i] for i in range(len(data)) if int(data[i][2]) > start and int(data[i][2]) < end]
show_top_2(new_data)


for i in range(len(data)):
    ip_splitted = data[i][0].split('.')
    bina = ''
    for n in ip_splitted:
        tmp = bin(int(n))[2:]
        for j in range(0, 8-len(tmp)):
            bina += '0' 
        bina += tmp
    print(bina)
    data[i][0] = int(bina, 2)
print(data)