import csv
import struct
file_name = 'D:\\440hz_0db_2ch_iis.csv'

data = []

with open(file_name) as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        data.append(row[2])
     
data = data[1:]



for i in range(len(data)):
    data[i] = int(data[i],16)


with open('hexBin.bin', 'wb') as fp:
    for x in data:
        a = struct.pack('H',x)
        fp.write(a)

print('done')