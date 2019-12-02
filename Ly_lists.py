from math import hypot

#List of Shapes
polygon = [[1,1],[4,6],[7,0],[4,1],[0,0]]
square = [[2,2], [4,4], [4,2], [2,4]]
octagon = [[2,4], [4,2], [6,2], [8,4], [8,6], [6,8], [4,8], [2,6]]
rectangle = [[2,2], [2,4], [6,2], [6,4]]
hexagon = [[2,4], [4,2], [6,2], [8,4], [6,6], [4,6]]

def perimeter (shape):
    #returns the perimeter of a shape given a list of vertices
    p = 0
    
    for i in range(len(shape)):
        x, y = shape[i]
        x2, y2 = shape[i-1]
        pAdd = hypot(x2-x, y2-y)

        p += pAdd
        
    return(p)

print(perimeter(rectangle))