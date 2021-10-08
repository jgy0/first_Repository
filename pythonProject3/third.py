import csv
import sys
data=[]
try:
    with open(r'D:\新建浏览器下载\软件\PythonDataVisualizationCookbookSE_Code\Chapter 02\ch02-data.csv') as f:
        reader=csv.reader(f)
        headers=next(reader)
        data=[row for row in reader]
except csv.Error as e:
    print("error reading csv file at line %s:%s" %(reader.line_num,e))
    sys.exit(-1)
if headers:
    print (headers)
    print('=================')
for datarow in data:
    print(datarow)



