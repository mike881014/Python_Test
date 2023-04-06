import csv

file = open('地址資料.csv')
reader = csv.reader(file)
for r in reader:
    if r[1][0] == '台':
        a = r[1][1:]
        t = "臺" + a
        r[1] = t
    print(r)
file.close()