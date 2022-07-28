ax, ay, bx, by, cx, cy = [float(i) for i in input().split()]
ab = ((ax-bx)**2+(ay-by)**2)**(1/2)
ac = ((ax-cx)**2+(ay-cy)**2)**(1/2)
bc = ((cx-bx)**2+(cy-by)**2)**(1/2)
def type_triangle(ax, ay, bx, by, cx, cy):
    if ab + bc == ac or ac + bc == ab or ac + ab == bc:
        print("staight line")
    elif ab**2+bc**2==ac**2 or ac**2+bc**2==ab**2 or ac**2+ab**2==bc**2:
        print("right triangle")
    elif (ab**2+bc**2-ac**2)/(2*ab*bc) > 0 and (ac**2+bc**2-ab**2)/(2*ac*bc) > 0 and (ac**2+ab**2-bc**2)/(2*ac*ab) > 0:
        print("acute triangle")
    else: 
        print("obtuse triangle")
type_triangle(ax, ay, bx, by, cx, cy)