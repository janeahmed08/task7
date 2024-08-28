num=int(input("enter num"))
def nth(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return nth(a-2)+nth(a-1)
for i in range(num):
    print(nth(i))