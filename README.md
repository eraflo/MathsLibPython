# MathsLibPython
 
All the maths functions I made in python during my maths courses

## To import in project

To import in your project, download this file : [Download](https://github.com/eraflo/MathsLibPython/blob/0e1e929dfa3838c43730f4b73359b6df44d1563c/dist/maths-lib-0.0.1.tar.gz)

## To contribute

Add your new modules in the libmath repo. Then, update the __ __init__ __ function to add your module. Don't forget to update setup.py for the version and to change the __tar.gz file__ in the __dist repo__.
Also, precise your change in the __Read.me__

Command to make the distrib : python setup.py sdist

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

- A module for Test Stat
  - __seuil_test__ : return the seuil of a test, when Chi2 is superior to the seuil, your hypothesis is null
  - __calculate_ddl__ : return the ddl of the matrix
  - __generate_excel__ : take a matrix with 1st line = row headers and 2st line = column headers, a matrix with observed values and alpha the value of the critics zone. Generate an excel file with the observed values array, the theorical values array, the number of ddl, the chi2 observed, the chi2 theorical and if we accept the hypothesis or not
