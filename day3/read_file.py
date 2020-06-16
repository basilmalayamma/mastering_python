def read_file(file_name):
    hndl = open(file_name)
    data = hndl.read()
    hndl.close()
    return data

file_names = ["Alix.txt", "Mario.txt", "Hanna.txt"]
avg_speed = []

for item in file_names:
    data = read_file(item).rstrip()
    speed_list = data.split('\n')
    speed_list = list(map(float, speed_list))
    print(speed_list, " Minimum time: ", min(speed_list))
    avg_speed.append(sum(speed_list)/len(speed_list))

print(avg_speed)

result = "{0}: {1:.2f}\n{2}: {3:.2f}\n{4}: {5:.2f}\n".format(
        file_names[0].split('.')[0],avg_speed[0],
        file_names[1].split('.')[0],avg_speed[1],
        file_names[2].split('.')[0],avg_speed[2]
        )

print(result)

file_w = open("result","w")
file_w.write(result)
file_w.close()
