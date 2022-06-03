n=int(input("enter the number of rows..."))
for i in range(n):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end="")
        k=k+1
    print()

i=0
while i<5:
    j=0
    while j-1<i:
        print(chr(65+j+i),end="")
        j=j+1
    print()
    i=i+1

#     i=65
# while i<=69:
#     j=65
#     while j<=i:
#         print(chr(j),end="")
#         j=j+1
#     print()
#     i=i+1