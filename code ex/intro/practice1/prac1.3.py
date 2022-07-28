distance = float(input())
speed = float(input())
if distance <= 2:
    f = 6000*distance
    print(f)
if distance > 2:
    f = 12000 + 3500*(distance-2) + 350*((distance-2)/speed)*60
    print(f)
