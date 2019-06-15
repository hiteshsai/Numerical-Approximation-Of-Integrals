"""
@author: Project D Section B3
"""

def riemann_left(f, xmin, xmax, n=100000):
    """Integrates between xmin and xmax using Riemann left rectangles"""
    assert n > 0
    h = 0
    w = (xmax - xmin)/float(n)
    for k in xrange(n):
        xk = xmin + w*k
        h += f(xk)
    result = w*h
    return result

def riemann_right(f, xmin, xmax, n=100000):
    """Integrates between xmin and xmax using Riemann right rectangles"""
    assert n > 0
    h = 0
    w = (xmax - xmin)/float(n)
    for k in xrange(n):
        xk = xmin + w*(k+1)
        h += f(xk)
    result = w*h
    return result

def riemann_center(f, xmin, xmax, n=100000):
    """Integrates between xmin and xmax using Riemann center rectangles"""
    assert n > 0
    h = 0
    w = (xmax - xmin)/float(n)
    for k in xrange(n):
        xk = (xmin + w/2.0) + w*k
        h += f(xk)
    result = w*h
    return result

def trapezoid(f,xmin,xmax,n=10000):
    """Integrates between xmin and xmax using Trapezoid rule"""
    assert n > 0
    k=float(xmax-xmin)/n
    s=0
    for i in range(1,n):
        s+=f(xmin+i*k)
    s+= (f(xmax)/2.0+ f(xmin)/2.0)
    return s*k

def monte_carlo(f, xmin, xmax, n):
    """Integrates between xmin and xmax using Mote Carlo method """
    assert n > 0
    assert xmin <= xmax
    from random import uniform 
    fvalues=[]
    h=-1
    X=xmin
    while (X<xmax):
        h+=1
        X = xmin + h/10.0
        fvalues.append(f(X))
    #the complete list of f(x) values is created as fvalues
    ymin=min(fvalues)
    ymax=max(fvalues) 
    xvalues = [ uniform(xmin,xmax) for i in xrange(n) ]
    yvalues = [ uniform(ymin,ymax) for j in xrange(n) ]
    k=0
    for i in xrange(n):
        if ((f(xvalues[i]) >= 0) and (yvalues[i] > 0) ):
            if ( yvalues[i] <= f(xvalues[i]) ):
                k+=1
        elif ((f(xvalues[i]) < 0) and (yvalues[i] < 0) ):
            if ( yvalues[i] > f(xvalues[i]) ):
                k-=1
    #k=number of points below the curve
    rectangle_area = (xmax-xmin)*(ymax-ymin)
    area = ( float(k)/n )*rectangle_area
    return area


import pylab
def monte_carlo_cuboid(f, xmin, xmax, ymin, ymax, n):
    """Integrates between xmin, xmax and ymin,ymax using Mote Carlo method"""
    
    assert n > 0
    assert xmin <= xmax
    assert ymin <= ymax
    from random import uniform 
    X=pylab.linspace(xmin,xmax,n)
    Y=pylab.linspace(ymin,ymax,n)
    fvalues=f(X,Y)
    zmin=min(fvalues)
    zmax=max(fvalues)
    
    
    # zmin-zmax gives us the height of the rectangular cuboid
    xvalues = [ uniform(xmin,xmax) for i in xrange(n) ]
    yvalues = [ uniform(ymin,ymax) for j in xrange(n) ]
    zvalues = [ uniform(zmin,zmax) for l in xrange(n) ]
    
    k=0
    for i in xrange(n):
        if (zmin < f(xvalues[i],yvalues[i]) < zmax):
            if ((f(xvalues[i],yvalues[i]) >= 0) and (zvalues[i] > 0) ):
                if ( zvalues[i] <= f(xvalues[i],yvalues[i]) ):
                    k+=1
            elif ((f(xvalues[i],yvalues[i]) < 0) and (zvalues[i] < 0) ):
                if ( zvalues[i] > f(xvalues[i],yvalues[i]) ):
                    k-=1
    #k=number of points below the curve
    cuboid_volume = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)
    
    area = ( float(k)/n )*cuboid_volume
    return area


def boole(f, xmin, xmax, k=100000):
    """Integrates between xmin and xmax using Boole's rule """
    assert k > 0
    n=k*4
    h = (xmax-xmin)/float(n)#to divide the intervel into certain(multiple of 4) sub interves
    terms=0
    N=n+1
    for i in xrange(4, N, 4):
        terms+=( (7*f( xmin+(i-4)*h )) + (32*f( xmin+(i-3)*h )) + (12*f( xmin+(i-2)*h )) + (32*f( xmin+(i-1)*h )) + (7*f( xmin+i*h )) )
    ans=((2*h)/45.0)*terms
    return ans



def simpson(f,xmin,xmax,n=10000):
    """Integrates between xmin and xmax using Simpsons rule"""
    assert n > 0
    assert n % 2 == 0
    h=float(xmax-xmin)/n
    s=0
    for i in range(1,n,2):
        s+= 4*f(xmin+i*h)
    for j in range(2,n,2):
        s+= 2*f(xmin+j*h)
    s+= f(xmin)+f(xmax)
    return s*h/3




