a = int(input())
b = int(input())
c = int(input())
if a == b and a == c:
    print('3')
elif (b == a and b != c) or (a == c and a != b) or (c == b and c != a):
    print('2')
else:
    print('0')