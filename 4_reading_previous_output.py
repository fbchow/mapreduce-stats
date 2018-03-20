
path = 'statearea.txt'

with open(path,'r') as f:
    read_data = f.readlines()
    read_data = read_data.split(',')
    print(read_data)
