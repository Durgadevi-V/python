def notes(num):
    count=0
    while num>=500:
        num=num-500
        count=count+1
    while num>=200:
        num=num-200
        count=count+1
    while num>=100:
        num=num-100
        count=count+1
    while num>=50:
        num=num-50
        count=count+1
    while num>=20:
        num=num-20
        count=count+1
    while num>=10:
        num=num-10
        count=count+1
    return count
notes(1000)
print("count")
