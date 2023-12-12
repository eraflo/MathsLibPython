# MathsLibPython
 
All the maths functions I made in python during my maths courses

## To import in project

To import in your project, download this file : [Download](https://github.com/eraflo/MathsLibPython/blob/0e1e929dfa3838c43730f4b73359b6df44d1563c/dist/maths-lib-0.0.1.tar.gz)

## To contribute

Add your new modules in the libmath repo. Then, update the __ __init__ __ function to add your module. Don't forget to update setup.py for the version and to change the __tar.gz file__ in the __dist repo__.
Also, precise your change in the __Read.me__

Commande to make the distrib : python setup.py sdist

Then, pip install the tar.gz file

## Actually
- Beginning of the Arithmetic module :
  - __pgcd(a, b)__ : give the pgcd of a and b using the Euclidean Algorithm

- The module for the chapter Statistic of 2 variables. The functions available are :
  - __S(a, b, X, Y)__ : to calcul the sum of the squares of the differences between the values of X and Y variables
  - __cov(X, Y)__ : to calcul the covariance of the X and Y variables
  - __a(X, Y)__ : is the value of the coefficient a, which is the leading coefficient of the linear function
  - __b(X, Y)__ : is the value of b, the ordinate at the origin
  - __droite(X, Y)__ : give an array of the Y values calculated at each point in X with the linear function determined
  - __r(X, Y)__ : give the correlation coefficient
  - __r2(X, Y)__ : give the determination coefficient
  - __display(X, Y)__ : display the values above in the console and display the dot clouds with the initial values and the regression line
  - __valY(X, Y, x)__ : give the Y value for a x given based on the regression line determined
