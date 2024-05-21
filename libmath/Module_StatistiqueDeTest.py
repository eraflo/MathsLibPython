import math
from scipy import stats as Stats
import numpy as np
import xlsxwriter


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


def calculate_ddl(matrix):
    """
    Calculate the degree of freedom for the Chi2 test

    param matrice: the matrix of the data
    return: the degree of freedom
    """
    # Check if matrix as same number of column every time
    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[i - 1]):
            raise ValueError("Matrix as not the same number of column every time")
    
    return (len(matrix) - 1) * (len(matrix[0]) - 1)

def generate_excel(matrix_headers, matrix, alpha):
    """
    Generate the excel file with the results of the test

    param matrix: the matrix of the data
    param alpha: significance level (probability of rejecting the null hypothesis when it is true)
    """
    ddl = calculate_ddl(matrix)
    seuil = seuil_test(ddl, alpha)

    # Check matrix_headers is compatible with the matrix
    if len(matrix_headers[0]) != len(matrix):
        raise ValueError("Matrix headers is not compatible with the matrix")
    
    if len(matrix_headers[1]) != len(matrix[0]):
        raise ValueError("Matrix headers is not compatible with the matrix")
    
    matrix_headers[0].append("Total")
    matrix_headers[1].append("Total")

    # Create the excel file
    workbook = xlsxwriter.Workbook('result_test.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    for row in range(1, len(matrix_headers[0]) + 1):
        worksheet.write(row, 0,  matrix_headers[0][row-1], bold)

    for column in range(1, len(matrix_headers[1]) + 1):
        worksheet.write(0, column,  matrix_headers[1][column-1], bold)
    
    # # Write some matrix data in the array
    for i in range(1, len(matrix) + 1):
        for j in range(1, len(matrix[i-1]) + 1):
            worksheet.write(i, j, matrix[i-1][j-1])
    
    # Totals
    for i in range(1, len(matrix) + 1):
        worksheet.write(i, len(matrix[0]) + 1, matrix[i-1].sum())
    
    for j in range(1, len(matrix[0]) + 1):
        worksheet.write(len(matrix) + 1, j, matrix[:, j-1].sum())
    
    worksheet.write(len(matrix) + 1, len(matrix[0]) + 1, matrix.sum())
    
    # Write some data headers.
    i_finale = len(matrix) + 4

    # Calculate the theoretical values of the matrix
    matrix_theoretical = np.zeros((len(matrix), len(matrix[0])))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_theoretical[i][j] = matrix[i].sum() * matrix[:, j].sum() / matrix.sum()
    
    # Write the theoretical values of the matrix
    for row in range(1, len(matrix_headers[0])):
        worksheet.write(i_finale + row, 0,  matrix_headers[0][row-1], bold)

    for column in range(1, len(matrix_headers[1])):
        worksheet.write(i_finale, column,  matrix_headers[1][column-1], bold)

    for i in range(1, len(matrix_theoretical) + 1):
        for j in range(1, len(matrix_theoretical[i-1]) + 1):
            worksheet.write(i_finale + i, j, matrix_theoretical[i-1][j-1])
    
    i_finale = i_finale + len(matrix_theoretical) + 3
    chi2_theoric = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            chi2_theoric += (matrix[i][j] - matrix_theoretical[i][j])**2 / matrix_theoretical[i][j]


    worksheet.write(i_finale, 0, "Degree of freedom", bold)
    worksheet.write(i_finale, 1, ddl)

    worksheet.write(i_finale + 1, 0, "Seuil théorique (chi2)", bold)
    worksheet.write(i_finale + 1, 1, chi2_theoric)

    worksheet.write(i_finale + 2, 0, "Seuil observé (chi2 alpha)", bold)
    worksheet.write(i_finale + 2, 1, seuil)

    worksheet.write(i_finale + 3, 0, "Result", bold)
    if chi2_theoric > seuil:
        worksheet.write(i_finale + 3, 1, "H0 is rejected")
    else:
        worksheet.write(i_finale + 3, 1, "H0 is accepted")

    workbook.close()