def read_file(file_name):
	f_handle = open(file_name)
	data = f_handle.read()
	f_handle.close()
	return data
	
def print_file(max_avg_speed_string,file_name):
	f_handle = open(file_name+".txt","w")
	f_handle.write(max_avg_speed_string)
	f_handle.close()

log_file = "log.txt"
functions_list = ['read_data', 'write_data', 'toggle_data', 'send_data', 'recv_data']

func_el_list = []

avg_speed = []
log_data = read_file(log_file)
log_data = log_data.rstrip('\n')
log_data = log_data.split('\n')

for idx,val in enumerate(functions_list):
	func_el_list.append([])
	avg = 0
	for functions in log_data:
		if val == functions.split(' ')[6]:
			func_el_list[idx].append(int(functions.split(' ')[8]))
	maximum = max(func_el_list[idx])
	avg = sum(func_el_list[idx])/len(func_el_list[idx])
	print_str= "{}:maximum:{},avg:{}".format(val,maximum,avg)
	print(print_str)
	print_file(print_str,val)
