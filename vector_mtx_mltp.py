#conducts multiplication between a vector and a matrix
""""""

print("\nWelcome to vecor_and_matrix_multiplication.\nEnter any vector and matrix and see their product.")

#for the vector 
size = int(input("\nHow many components does your vector have?: "))

#creates a list for entering main values of that vector
vector = ["" for x in range(size)]

#populates the vector list with integers
for x in range(len(vector)):

    #??how to sort repeated input/error problem
    while True:
        val = int(input("Entry {n}: ".format(n = (x + 1))))
        if isinstance(val, int):
            break
    
    vector[x] = val

#print(vector)

""""""
#for the matrix
rows = int(input("\nHow many rows does your matrix have?: "))
columns = int(input("How many columns?: "))

#one list that contains all rows and columns with it
#currently all rows have no columns
matrix = [[] for x in range(rows)]

#adding the no of columns as given
#each row's length/entries will be in the same number as the columns
for x in range(rows):
    matrix[x] = ["" for y in range(columns)]



#filling in all the empty entries
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        matrix[x][y] = int(input("Value for entry in Row {r} Column {c}: ".format(r = x+1, c = y+1)))

#print(matrix)

#multipl between a vector and matrix is only valid
#if the no of columns in the matrix and
#the no of components in the vector
if (columns == size):
    print("Congratulations, multiplication is possible!\n")

    #the answer will always be a column vector with its number
    #of components being thee same as the number of rows of the 
    #original/parent matrix
    ans = ["" for x in range(rows)]


    #take each entry of each row (in matrix)
    #multiply it with corresponding component (in vector)
    for y in range(rows):
    #for each row:

        #renews the sum total for each row
        #clearing all previous calculations
        finalsum = 0

        #taking each entry in the row
        for k in range(columns):

            #sum stores the product of each entry with its corresponding vector component
            sum = (matrix[y][k]*vector[k])

            #finalsum var totals the sum of the entire row so far
            finalsum +=sum
        

        #after the final sum has been calculated, each corresponding
        #component of the final answer (a col vector) stores that sum
        ans[y] = finalsum


    print("Your final vector is: {}.".format(ans))

else:
    print("Sorry, multiplication isn't valid in this case.")