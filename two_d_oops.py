class Point:
    def __init__(self,x,y):   # can write anything instead of self, not a keyword
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self):
        return '({},{})'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    def dist_from_origin(self):
        # return (self.x_cod**2 + self.y_cod**2)**0.5
        return self.euclidean_distance(Point(0,0))
    #check whether point lies on a line or not.
    
class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    
    def __str__(self):
        return '{}x+{}y+{}'.format(self.A,self.B,self.C)
    
    def lies_on_line(line,point):
        if line.A * point.x_cod + line.B*point.y_cod + line.C == 0:
            return "True the point lies on the line."
        else: 
            return "The point does not lie on the line."


p1 = Point(1,1)
print(p1)
p2 = Point(3,4)
print(p2)
print(p1.euclidean_distance(p2))  # distance 
print(p1.dist_from_origin())      # distance from the origin.
l1 = Line(1,1,2)
print(l1)
print(l1.lies_on_line(p1))  #todo:  this should return true right? but it is not

l3 = Line(0,0,0)
p3 = Point(0,0)
print(l3.lies_on_line(p3))




#writing a lambda function
l2 = lambda x,y,z: print(x+y+z)
l2(1,23,3)

