# a=int(input())
# b=int(input())
# if b != 0:
#     print(a*(b%10))
#     print(a*(b%100))
#     print(a*(b%1000))
# else:
#     print(a*b)

# a,b = map(int, input().split())
# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))

# a = int(input())
# b = int(input())

# print(a * (b%10))
# print(a * ((b%100)//10))
# print(a * (b//100))
# print(a * b)

a,b=map(int,input().split())

print(a * (b%10))
print(a * ((b%100)//10))
print(a * (b//100))
print(a * b)