list=[10,20,30,11,12,22,33,21,54]
for i in range(len(list)-1):
    if list[i] <list[i+1]:
        large=list[i+1]
print("largest no in list is ",large)
