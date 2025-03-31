# L6.E1

# changes to True if an error when entering a matrix is detected
hasErrors = False

# matrices
matrixA = []
matrixB = []

# Read in the elements of a matrix and returns 2D list
def inputMatrix(row, column, name):
    global matrixA
    global matrixB
    print(f'Enter Matrix {name}:')
    matrix = []
    global hasErrors

    # executes until all rows are entered without any errors
    for eachRow in range(row):
        try:
            matrixRow = list(map(int, input().split()))
            if len(matrixRow) != column:
                # executes if matrix does not comply with the given dimensions
                print('\nInvalid Matrix')
                hasErrors = True
                break
            matrix.append(matrixRow)
        except ValueError:
            # executes if non-numerical char is input
            print('\nError')
            hasErrors = True
            break

    if name == 'A':
        matrixA = matrix
    else:
        matrixB = matrix
    return None


# convert a matrix to its transpose and returns
def transposeMatrix():
    global matrixB
    tranposeMatrix = list(zip(*matrixB))
    return tranposeMatrix


# returns the product of two matrices
def productOfMatrices(matrix1, matrix2):
    productMatrix = []

    # iterates all elements to get each individual element of the product
    for i in range(len(matrix1)):
        productRow = []
        for j in range(len(matrix1)):
            element = 0
            for k in range(len(matrix1[0])):
                element += matrix1[i][k] * matrix2[k][j]
            productRow.append(element)
        productMatrix.append(productRow)
    
    return productMatrix


def printMatrix(matrix):
    # iterates all rows to print
    for row in matrix:
        # prints elements in a row
        for element in row:
            print(element, end=' ')
        print('')
    return None

# input the dimensions and matrices   
row, column = map(int, input('Enter the dimension: ').split(','))
inputMatrix(row, column, 'A')

# executes if no errors are detected when entering matrices
if hasErrors == False:
    print('')
    inputMatrix(row, column, 'B')
    transposeB = transposeMatrix()
    productMatrix = productOfMatrices(matrixA, transposeB)
    print('\nMatrix A X Transpose(B):')
    printMatrix(productMatrix)
