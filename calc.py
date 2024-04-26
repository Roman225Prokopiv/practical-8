first = 0
second = 1

def calc(a,b):
    res = a/b
    if res==0:
        return 'error'
    else:
        print(res)


calc(first, second)
