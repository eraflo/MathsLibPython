import math
from scipy import stats as Stats


# Calculate the seuil of the test
def seuil_test(ddl, alpha):
    """
    Calculate the seuil of the test
    If Chi2 > seuil, then we reject the null hypothesis
    Else we accept the null hypothesis and we reject the alternative hypothesis

    param ddl: degree of freedom
    param alpha: significance level (probability of rejecting the null hypothesis when it is true)

    return: the seuil of the test
    """
    return Stats.chi2.ppf(1 - alpha, ddl)

