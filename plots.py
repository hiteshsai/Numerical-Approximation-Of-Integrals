"""
@author: Project D Section B3
"""

import pylab

def plot_riemann_left(f, xmin, xmax, name, n):
    pylab.figure()
    pylab.title("Riemann left rectangles for "+name+" with "+str(n)+" rectangles" )
    xvalues = pylab.linspace(xmin,xmax,1000)
    yvalues = [ f(x) for x in xvalues ]
    pylab.plot(xvalues,yvalues,'r-')#plots the function f(X) between limits
    h = (xmax - xmin)/float(n)
    xi = [ xmin + i*h for i in xrange(n) ]
    yi = [ f(x) for x in xi ]
    #the below code plots the rectangles
    for x,y in zip(xi,yi):
        pylab.plot([x, x, x+h, x+h, x], [0, y, y, 0, 0], 'b-')
        

def plot_riemann_right(f, xmin, xmax, name, n):
    pylab.figure()
    pylab.title("Riemann right rectangles for "+name+" with "+str(n)+" rectangles")
    xvalues = pylab.linspace(xmin,xmax,1000)
    yvalues = [ f(x) for x in xvalues ]
    pylab.plot(xvalues,yvalues,'r-')#plots the function f(X) between limits
    h = (xmax - xmin)/float(n)
    xi = [ xmin + i*h for i in xrange(n) ]
    yi = [ f(x+h) for x in xi ]
    #the below code plots the rectangles
    for x,y in zip(xi,yi):
        pylab.plot([x, x, x+h, x+h, x], [0, y, y, 0, 0], 'b-')

def plot_riemann_center(f, xmin, xmax, name, n):
    pylab.figure()
    pylab.title("Riemann center rectangles for "+name+" with "+str(n)+" rectangles")
    xvalues = pylab.linspace(xmin,xmax,1000)
    yvalues = [ f(x) for x in xvalues ]
    pylab.plot(xvalues,yvalues,'r-')#plots the function f(X) between limits
    h = (xmax - xmin)/float(n)
    xi = [ xmin + i*h for i in xrange(n) ]
    yi = [ f(x+(h/2.0)) for x in xi ]
    #the below code plots the rectangles
    for x,y in zip(xi,yi):
        pylab.plot([x, x, x+h, x+h, x], [0, y, y, 0, 0], 'b-')

def plot_trapezoid(f, xmin, xmax, name, n):
    pylab.figure()
    pylab.title("Trapezoid method for "+name+" with "+str(n)+" trapeziums")
    xvalues = pylab.linspace(xmin,xmax,1000)
    yvalues = [ f(x) for x in xvalues ]
    pylab.plot(xvalues,yvalues,'r-')#plots the function f(X) between limits
    h = (xmax - xmin)/float(n)
    xi = [ xmin + i*h for i in xrange(n) ]
    yi = [ f(x) for x in xi ]
    #the below code plots the trapeziums
    for x,y in zip(xi,yi):
        pylab.plot([x, x, x+h, x+h, x], [0, y, f(x+h), 0, 0], 'b-', linewidth=0.5)

def plot_monte_carlo(f, xmin, xmax, name, n):
    assert n > 0
    assert xmin < xmax
    from random import uniform
    fvaluesat=[]
    fvalues=[]
    h=-1
    X=xmin
    while (X<xmax):
        h+=1
        X = xmin + h/10.0
        fvaluesat.append(X)
        fvalues.append(f(X))
    #the complete list of f(x) values is created as fvalues
    pylab.figure()
    pylab.plot(fvaluesat,fvalues,'-g')
    ymin=min(fvalues)
    ymax=max(fvalues)
    xvalues = [ uniform(xmin,xmax) for i in xrange(n) ]
    yvalues = [ uniform(ymin,ymax) for j in xrange(n) ]
    pylab.plot(xvalues,yvalues,'.')
    k=0
    pxval=[]
    pyval=[]
    for i in xrange(n):
        if ((f(xvalues[i]) >= 0) and (yvalues[i] > 0) ):
            if ( yvalues[i] <= f(xvalues[i]) ):
                pxval.append(xvalues[i])
                pyval.append(yvalues[i])
                k+=1
        elif ((f(xvalues[i]) < 0) and (yvalues[i] < 0) ):
            if ( yvalues[i] > f(xvalues[i]) ):
                pxval.append(xvalues[i])
                pyval.append(yvalues[i])
                k-=1
    pylab.plot(pxval,pyval,'r.')
    #k=number of points below the curve
    rectangle_area = (xmax-xmin)*(ymax-ymin)
    area = ( float(k)/n )*rectangle_area
    pylab.title("Monte Carlo method for "+str(name)+" with "+str(n)+" points, area = "+str(area))


import scipy


from mpl_toolkits.mplot3d import Axes3D
def plot_monte_carlo_cuboid(f, xmin, xmax, ymin, ymax, name, n=100):
    assert n > 0
    assert xmin < xmax
    assert ymin <= ymax
    from random import uniform
    fvaluesx=[]
    fvaluesy=[]
    fvalues_for_limits=[]
    fvalues=[]
    X=pylab.linspace(xmin,xmax,n)
    Y=pylab.linspace(ymin,ymax,n)
    fvalues_for_limits=f(X,Y)
    fig = pylab.figure()
    ax = Axes3D(fig)
    [fvaluesx,fvaluesy] = scipy.meshgrid(X,Y)
    fvalues = f(fvaluesx,fvaluesy)
    ax.plot_surface(fvaluesx,fvaluesy,fvalues)
    zmin=min(fvalues_for_limits)
    zmax=max(fvalues_for_limits)
    xvalues = [ uniform(xmin,xmax) for i in xrange(n) ]
    yvalues = [ uniform(ymin,ymax) for j in xrange(n) ]
    zvalues = [ uniform(zmin,zmax) for l in xrange(n) ]
    k=0
    pxval=[]
    pyval=[]
    pzval=[]
    pxval_u=[]
    pyval_u=[]
    pzval_u=[]
    for i in xrange(n):
        if ((f(xvalues[i],yvalues[i]) >= 0) and (zvalues[i] > 0) ):
            if ( zvalues[i] <= f(xvalues[i],yvalues[i]) ):
                pxval.append(xvalues[i])
                pyval.append(yvalues[i])
                pzval.append(zvalues[i])
                k+=1
            else:
                pxval_u.append(xvalues[i])
                pyval_u.append(yvalues[i])
                pzval_u.append(zvalues[i])
        elif ((f(xvalues[i],yvalues[i]) < 0) and (zvalues[i] < 0) ):
            if ( zvalues[i] > f(xvalues[i],yvalues[i]) ):
                pxval.append(xvalues[i])
                pyval.append(yvalues[i])
                pzval.append(zvalues[i])
                k-=1
            else:
                pxval_u.append(xvalues[i])
                pyval_u.append(yvalues[i])
                pzval_u.append(zvalues[i])
    ax.scatter(pxval_u,pyval_u,pzval_u,c='y')
    ax.scatter(pxval,pyval,pzval,c='r')
    rectangle_area = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)
    area = ( float(k)/n )*rectangle_area
    pylab.title("Monte Carlo method for "+str(name)+" with "+str(n)+" points, area = "+str(area))
    
    return area



def f1(x): 
    return x**2 +2

plot_riemann_left(f1, 0, 5, "x**2", n=20)
plot_riemann_right(f1, 0, 5, "x**2", n=20)
plot_riemann_center(f1, 0, 5, "x**2", n=20)
plot_trapezoid(f1, 0, 5, "x**2", n=20)
plot_monte_carlo(f1, 0, 5, "x**2",576)


def f2(x,y):
    return x**2+y**2


print plot_monte_carlo_cuboid(f2, 0, 1, -1, 2, 'Function', 1000)

