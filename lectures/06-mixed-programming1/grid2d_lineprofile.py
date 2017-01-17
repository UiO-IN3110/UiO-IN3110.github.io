from numpy import *

class Grid2D(object):
    def __init__(self,
                 xmin=0, xmax=1, dx=0.5,
                 ymin=0, ymax=1, dy=0.5):

        self.xcoor = r_[xmin:xmax+dx:dx]
        self.ycoor = r_[ymin:ymax+dy:dy]

    @profile
    def gridloop(self, f):
        lx = size(self.xcoor)
        ly = size(self.ycoor)
        a = zeros((lx,ly))

        for i in range(lx):
            x = self.xcoor[i]
            for j in range(ly):
                y = self.ycoor[j]
                a[i,j] = f(x, y)
        return a

g = Grid2D(dx=0.001, dy=0.001)

def myfunc(x, y):
        return sin(x*y) + y

g.gridloop(myfunc)
