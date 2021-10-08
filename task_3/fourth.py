import json
with open('txt.txt','w+') as f:
    json.dump({'a':1,'b':2,'c':3},f)
with open('txt.txt','r') as fp:
    print(json.load(fp))