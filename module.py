import math

def sq_footage():
    feet_wall1 = input("what is the legnth of wall #1")
    feet_wall2 = input("what is the legnth of wall #2")
    square_footage= int(feet_wall1)*int(feet_wall2)
    return  square_footage  

def circ():
    r_circle = int(input("what is the radius"))
    c=math.pi*2*r_circle
    return c