#List
#Tuple

li = [1,2,3,4,5,6,7,8,9,10]
tu = (1,2,3,4,5,6,7,8,9,10) #tuple is immutable and list is mutable
carList = ["BMW","Audi","Maruti","Hyundai","Tata"]
#for i in carList:
 #   print(i.upper())
#print(sorted(carList))
#print(sorted(carList, reverse=True))
#print(sorted(carList, key=len, reverse=True))
carList[-1][-1]
def last_lettter(x):
    return x[-1][-1]
carList.sort(key=last_lettter)


