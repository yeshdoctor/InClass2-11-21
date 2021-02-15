def plane(p1,p2,x_new):
    x1,y1 = p1
    x2,y2 = p2
    s = (y2-y1)/(x2-x1)
    return s*(x_new-x1)+y1

def on_line(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    s = (y2-y1)/(x2-x1)
    return s*(x3-x1)+y1 == y3
