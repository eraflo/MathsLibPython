def pgcd(a, b):
    """
    Calcul of the PGCD of a and b by the Euclidean algorithm
    
    """
    while a % b != 0:
        a, b = b, a % b
    return b