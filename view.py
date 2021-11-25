

def fibbonachi():
    a,b =1,1
    while True:
        yield a 
        a,b = b,a+b

for index,x in enumerate(fibbonachi()):
    if index ==100:
        break
    print("%s" % x)