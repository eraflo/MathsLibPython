import matplotlib.pyplot as plt

# Calcul de a et b par la méthode des moindres carrés
def S(a, b, X, Y):
    """Calcul of S(a, b) = sum of the squares of the differences between the values of Y and the values of the regression line"""

    # Vérification de la taille des listes
    if len(X) != len(Y):
        print("Lists must have the same size")
        return None

    # Calcul de la somme des carrés des écarts
    S = 0
    for i in range(len(X)):
        S += (Y[i] - a * X[i] - b) ** 2
    return S

# Calcul de la covariance
def cov(X, Y):
    """
    Calcul of the covariance of X and Y
    
    X and Y are lists of values of the same size
    """

    # Vérification de la taille des listes
    if len(X) != len(Y):
        print("Lists must have the same size")
        return None

    # Calcul de la moyenne de X et de Y
    moyX = sum(X) / len(X)
    moyY = sum(Y) / len(Y)

    # Calcul de la covariance
    cov = 0
    for i in range(len(X)):
        cov += (X[i] - moyX) * (Y[i] - moyY)
    return cov / len(X)

# Calcul de la variance
def var(X):
    """
        Calcul of the variance of X
    """

    # Calcul de la moyenne de X
    moyX = sum(X) / len(X)

    # Calcul de la variance
    var = 0
    for i in range(len(X)):
        var += (X[i] - moyX) ** 2
    return var / len(X)

# Calcul de a
def a(X, Y):
    """Calcul of a = cov(X, Y) / var(X)"""
    return cov(X, Y) / var(X)

# Calcul de b
def b(X, Y):
    """Calcul of b = moyY - a * moyX"""
    moyX = sum(X) / len(X)
    moyY = sum(Y) / len(Y)
    return moyY - a(X, Y) * moyX

# Calcul de la droite de régression
def droite(X, Y):
    """
    Calcul of the regression line of X and Y
    
    Return the list of y values
    """
    return [a(X, Y) * x + b(X, Y) for x in X]

# Calcul du coefficient de corrélation
def r(X, Y):
    """
    Calcul of r = cov(X, Y) / (var(X) * var(Y)) ** 0.5
    
    r is the coefficient of correlation of X and Y
    """
    return cov(X, Y) / ((var(X) * var(Y)) ** 0.5)

# Calcul du coefficient de détermination
def r2(X, Y):
    """
    Calcul of r2 = r(X, Y) ** 2

    r2 is the coefficient of determination of X and Y

    """
    return r(X, Y) ** 2

# Affichage des points et de la droite de régression
def display(X, Y):
    """
    Display the points and the regression line of X and Y

    X and Y are lists of values of the same size
    """
    if len(X) != len(Y):
        print("Lists must have the same size")
        return None
    
    print("a =", a(X, Y))
    print("b =", b(X, Y))
    print("r =", r(X, Y))
    print("r2 =", r2(X, Y))
    print("S =", S(a(X, Y), b(X, Y), X, Y))
    print("expression : ", "y =", a(X, Y), "* x ", ( "+" if b(X, Y) >= 0 else "-"), abs(b(X, Y)))
    print("values =", droite(X, Y))
    plt.plot(X, Y, "o")
    plt.plot(X, droite(X, Y))
    plt.show()

# Valeur de Y pour une valeur de X
def valY(X, Y, x):
    """
    Calcul of the value of Y for the value x of X

    X and Y are lists of values of the same size
    """
    if len(X) != len(Y):
        print("Lists must have the same size")
        return None
    return a(X, Y) * x + b(X, Y)



