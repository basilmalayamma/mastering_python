def generate_result(fn_names, data):
    read_data = []
    write_data = []
    toggle_data = []
    send_data = []
    recv_data = []
    for line in data:
        l = line.split()
        print(type(line))
        #print(line.rstrip().split())
        #read_data.append(line.split()[-2])
        #write_data.append(line.split()[-2])
        #toggle_data.append(line.split()[-2])
        #toggle_data.append(line.split()[-2])
        #send_data.append(line.split()[-2])
        #recv_data.append(line.split()[-2])
    print(read_data)
    print(write_data)

def main():
    fn_names = ['read_data', 'write_data', 'toggle_data', 'send_data', 'recv_data']
    file_handle = open("log.txt")
    data = file_handle.read()
    file_handle.close()
    generate_result(fn_names, data)

if __name__ == "__main__":
    main()
