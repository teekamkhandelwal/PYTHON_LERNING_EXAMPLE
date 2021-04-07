from math import pi
radius =eval(input('enter radius of circle'))
if radius>0:
    area=radius*radius*pi
    print('area of circle :',format(area,'.2f'))
    c=2*pi*radius
    print('circum of circle is:',format(c,'.2f'))
                   
