num=int(input("enter the number..."))
n=num
product=1
while n!=0:
    rem=n%10
    product=product*rem
    n=n//10
    print(product)
    
# list1=[11,23,45,23,64,22,11,24]
# for num in list1:
#     if num %2!=0:
#         print(num,end="odd num")

