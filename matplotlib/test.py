import matplotlib.pyplot as plt

class FileHanndler:
    def __init__(self, file_name):
        self.file_name = file_name
    def read_file(self):
        f_handle = open(self.file_name)
        data = f_handle.read()
        return data
    def write_file(self, data):
        f_handle = open(self.file_name, 'w')
        f-f_handle.write(data)
        f_handle.close()

atheletes = ['alix', 'mario', 'hanna']
speed = []

for athelete in atheletes:
    file_hanndler = FileHanndler(athelete + ".txt")
    print(file_hanndler.read_file())
    try:
        speed = float(map(float, file_hanndler.read_file().rstrip().spli('\n')))
    except:
        print("Error in parsing file")
    else:
        print(speed)
