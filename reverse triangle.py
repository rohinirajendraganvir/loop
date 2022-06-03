# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end="")
#     print()

# n=4
# i=1
# while n>0:
#     b=1
#     while b<i:
#         print("",end="")
#         b=b+1
#     j=1
#     while j<=(n*2-1):
#         print("*",end="")
#         j=j+1
#     print()
#     n=n-1
    # i=i+1

num=int(input("enter the number of rows..."))
for row in range(num+1,0,-1):
    for column in range(1,row+1):
        print(row,end="")
    print()

n=9
for i in range(n-2+1):
    for col in range(1,i+1):
        print(i,end="")
    print()

