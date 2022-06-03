
count=0
num=int(input("enter the number.."))
for i in range(1,1+num):
        if num%i==0:
            count=count+1
        if count==2:
            print("prime number")
            break
        else:
            print("not prime number")
            break
            

# num=int(input("enter the number.."))
# if num>1:
#     for i in range (2,num):
#         if num%i==0:
#             print(num,"is not  a prime number")
#             print("i,times",num//i,"is",num)
#             break
#     else:
#         print(num,"is  a prime number")





#