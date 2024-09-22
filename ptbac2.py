import math

a = float(input())
b = float(input())
c = float(input())

print("Phương trình bậc 2 có dạng ax^2 + bx + c = 0:")
if b > 0:
    if c >= 0:
        print(f"\t\t\t{a}x^2 + {b}x + {c} = 0")
    else:
        print(f"\t\t\t{a}x^2 + {b}x + ({c}) = 0")
else: 
    if c >= 0:
        print(f"\t\t\t{a}x^2 + ({b})x + {c} = 0")
    else:
        print(f"\t\t\t{a}x^2 + ({b})x + ({c}) = 0")

delta = b ** 2 - (4 * a * c)
if a == 0:
    if b == 0:
        if c == 0:
            print("=>Phương trình có vô số nghiệm")
            sono = -1
        else:
            print("=>Phương trình vô nghiệm")
            sono = 0
    else:
        x = -c / b
        print(f"=> Phương trình có nghiệm kép: x = {x}")
        sono = 1
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        if x1 > x2:
            a = x1
            x1 = x2
            x2 = a
        print("=> Phương trình có 2 nghiệm phân biệt:")
        print(f"\tx1 = {x1}")
        print(f"\tx2 = {x2}")
        sono = 2
    elif delta == 0:
        x = -b / (2 * a)
        print("=>Phương trình có nghiệm kép:")
        print(f"\tx1 = x2 = {x}")
        sono = 1
    else:
        print("=>Phương trình vô nghiệm")
        sono = 0
