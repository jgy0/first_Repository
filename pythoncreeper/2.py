# coding:utf-8
def tell(s):
    num_digit,num_a=0,0
    for i in s:
        if ord(i)>=ord('0') and ord(i)<=ord('9'):
            num_digit+=1
        elif ((ord(i)>=65 and ord(i)<=90 ) or (ord(i)>=97 and ord(i)<=122)):
            num_a+=1
    return num_a,num_digit
def check(li):
    list_1=[]
    l=len(li)
    for i in range(l):
        if i%2==0:
            list_1.append(li[i])
        else:
            pass
    return list_1
def judge(n):
    if len(n)>5:
        return 'TRUE'
    else:
        return 'FALSE'
def check_dict(n):
    values=list(n.values())
    values=list(map(str,values))
    values=tuple(map(len,values))
    return values
def value_input(*args):
    l=len(args)
    key_0=[ i for i in range(1,l)]
    dict_0=dict(zip(key_0,args))
    return dict_0
def dict_value(**kwargs):
    v=list(kwargs.values())
    return v
def last(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return last(n-1)+last(n-2)

if __name__=='__main__':
    a,b=tell('kgjfhd5678')
    print(a,b)
    c=check([1,2,3,4,5,6])
    print(c)
    d=judge((1,2,3,4,5,6))
    print(d)
    e=check_dict({'a':1,'b':2,'c':3,'d':4,'e':5})
    print(e)
    f=value_input(1,2,3,4,5,6,7)
    print(f)
    g=dict_value(zhangsan=87,lisi=88,wangwu=99)
    print(g)
    h=last(10)
    print(h)
