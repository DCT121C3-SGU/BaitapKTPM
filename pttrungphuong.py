import math

a = float(input())
b = float(input())
c = float(input())

print("Phương trình trùng phương có dạng ax^4 + bx^2 + c = 0:")
if b >= 0:
    if c >= 0:
        print(f"\t\t\t{a}x^4 + {b}x^2 + {c} = 0")
    else:
        print(f"\t\t\t{a}x^4 + {b}x^2 + ({c}) = 0")
else: 
    if c >= 0:
        print(f"\t\t\t{a}x^4 + ({b})x^2 + {c} = 0")
    else:
        print(f"\t\t\t{a}x^4 + ({b})x^2 + ({c}) = 0")

if a == 0:
        if b == 0:
            if c == 0:
                print("=>Phương trình có vô số nghiệm")
                sono = -1
            else:
                print("=>Phương trình vô nghiệm")
                sono = 0
        else:
            if -c / b < 0:
                print("=>Phương trình vô nghiệm")
                sono = 0
            else:
                if -c / b == 0:
                    print(f"=> Phương trình có nghiệm kép: x = 0")
                    sono = 1
                else:
                    x1 = -math.sqrt(-c/b)
                    x2 = math.sqrt(-c/b)
                    print("=> Phương trình có 2 nghiệm phân biệt:")
                    print(f"\tx1 = {x1}")
                    print(f"\tx2 = {x2}")
                    sono = 2
else:
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        print("=>Phương trình vô nghiệm")
        sono = 0
    else:
        if delta == 0:
            t = -b / (2 * a)
            if t < 0:
                print("=>Phương trình vô nghiệm")
                sono = 0
            else:
                x1 = -math.sqrt(t)
                x2 = math.sqrt(t)
                print("=> Phương trình có 2 nghiệm phân biệt:")
                print(f"\tx1 = {x1}")
                print(f"\tx2 = {x2}")
                sono = 2
        else: 
            t1 = (-b - math.sqrt(delta)) / (2 * a)
            t2 = (-b + math.sqrt(delta)) / (2 * a)
            if t2 < 0 and t1 < 0:
                print("=>Phương trình vô nghiệm")
                sono = 0
            if t1 < 0 and t2 > 0:
                x1 = -math.sqrt(t2)
                x2 = math.sqrt(t2)
                print("=> Phương trình có 2 nghiệm phân biệt:")
                print(f"\tx1 = {x1}")
                print(f"\tx2 = {x2}")
                sono = 2
            if t1 > 0 and t2 < 0:
                x1 = -math.sqrt(t1)
                x2 = math.sqrt(t1)
                print("=> Phương trình có 2 nghiệm phân biệt:")
                print(f"\tx1 = {x1}")
                print(f"\tx2 = {x2}")
                sono = 2
            if t1 > 0 and t2 > 0:
                x1 = -math.sqrt(t2)
                x2 = math.sqrt(t2)
                x3 = -math.sqrt(t1)
                x4 = math.sqrt(t1)
                print("=> Phương trình có 4 nghiệm phân biệt:")
                print(f"\tx1 = {x1}")
                print(f"\tx2 = {x2}")
                print(f"\tx3 = {x3}")
                print(f"\tx4 = {x4}")
                sono = 4
            if t1 == 0 or t2 == 0:
                print("=> Phương trình có 1 nghiệm:")
                print(f"\tx1 = 0")
                sono = 1
            if t1 == 0 and t2 < 0:
                print("=> Phương trình có 1 nghiệm:")
                print(f"\tx1 = 0")
                sono = 1 
            if t1 < 0 and t2 == 0:
                print("=> Phương trình có 1 nghiệm:")
                print(f"\tx1 = 0")
                sono = 1
            if t1 == 0 and t2 > 0:
                x1 = -math.sqrt(t2)
                x2 = math.sqrt(t2)
                print("=> Phương trình có 3 nghiệm phân biệt:")
                print(f"\tx1 = {x1}")
                print(f"\tx2 = {x2}")
                print(f"\tx3 = 0")
                sono = 3
            if t1 > 0 and t2 == 0:
                x1 = -math.sqrt(t1)
                x2 = math.sqrt(t1)
                print("=> Phương trình có 3 nghiệm phân biệt:")
                print(f"\tx1 = {x1}")
                print(f"\tx2 = {x2}")
                print(f"\tx3 = 0")
                sono = 3
