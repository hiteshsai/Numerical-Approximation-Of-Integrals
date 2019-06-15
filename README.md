# Numerical-Approximation-Of-Integrals

This program approximates numerical one dimensional integrals and find the area under the curve

# Task and approach

We were assigned the task to compute 1D integrals. We used many ways for integration
1. Riemann sum(left, right and centre) 
2. Trapezoidal rule 
3. Monte-carlo integration(1D and 2D) 
4. Simpson rule 
5. Boole’s rule

We plotted the Riemann left, right and centre rectangles, trapezoids and we also plotted random points for monte-carlo on the given curve to make it clear what is going on.


# References

We took reference from T.M.Apostol and the following websites:

- http://www.intmath.com/integration/6-simpsons-rule.php 
- http://en.wikipedia.org/wiki/Monte_Carlo_integration 
- http://en.wikipedia.org/wiki/Boole's_rule
- http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

# Working of each function:

1. *Riemann sum:* We define riemann_left, riemann_right and riemann_centre which takes 4 arguments: f (function), xmin, xmax and n (number of rectangles). The entire region is divided into n rectangles and the area of the rectangles are found and then summed up to find the value of the integral.

2. *Monte-Carlo integration:* We define the function monte_carlo which takes 4 arguments: f (function), xmin, xmax and n (number of random uniform points). In the function we define a rectangle_area= (xmax-xmin)*(ymax-ymin). The function then takes n random points in this rectangle and checks how many of them are above and below the curve. If there are k points below the curve then the function computes the integral as area of the rectangle* probability of getting a point below the curve.

3. *Boole’s rule:* We define the function boole which takes 4 arguments: f (function), a, b, k. It approximates the integral by using the value of f at 5 equally spaced points.

4. *Trapezoidal rule:* We define the function trapez which takes 4 arguments :( function), a, b and n (number of trapezoids). It approximates the region under the graph as a trapezoid and calculating its area.

5. *Simpson Rule:* We define the function simpson which takes 4 arguments: f (function), a, b, n (number of intervals). The function approximates the integral using a polynomial of degree 2.

6. *Monte-Carlo 2D integration:* We define the function monte_carlo_cuboid which takes 6 arguments: f (function), xmin, xmax,ymin,ymax and n (number of random uniform points). In the function we define a cuboid_volume= (xmax-xmin)*(ymax-ymin)*(zmax-zmin). The function then takes n random points in this cuboid and checks how many of them are above and below the curve. If there are k points below the curve then the function computes the integral as volume of the cuboid* probability of getting a point below the curve.

# Plotting makes use of inbuilt function pylab.

1. *Plotting Riemann rectangles:* We defined the functions plot_riemann_left, plot_riemann_right and plot_riemann_centre which take 5 arguments: f (function), xmin, xmax, name (name of the function) and n (no. of rectangles). The functions plot the Riemann left, right and centre rectangles on the curve of the function.

2. *Plotting Trapezoidal:* We define the function plot_trapezoid which takes 5 arguments: f (function), xmax, xmin, name (name of the function) and n (no. of trapezoids). The function plots the trapezoids under the curve which is used for the approximation of the integral.

3. *Plotting Monte-Carlo:* We define the function plot_monte_carlo which takes 5 arguments: f (function), xmax, xmin, name (name of the function) and n (no. of random points). The function plots the random points in the rectangle that we have defined around the function.

4.* Plotting Monte-Carlo 2_D:* We define the the function plot_monte_carlo_cuboid .We managed to make Monte carlo 2D graph by looking into website for plotting 3D curves.

# Difficulties faced:

We faced difficulty in Monte carlo 2D and the plotting of its curve was even more difficult but after doing a bit research in websites relating to plotting of 3D curves we finally succeded.

