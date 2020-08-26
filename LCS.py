def lcs(A, B, m, n):
    #As explained in class, maintaining a table of dimensions (A X B) length, initializing all elements to 0 as of now
    #https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
    #Using List Comprehensions - https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    
    opt = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            #Filling 0 in first row and first column 
            if i == 0 or j == 0:
                opt[i][j] = 0
            #Condition 1: when A[i] == B[j]
            elif A[i-1] == B[j-1]:
                opt[i][j] = opt[i-1][j-1] + 1
                pi = "arrow_corner"
            #Condition 2: when A[i]!= B[j]
            else:
                opt[i][j] = max(opt[i-1][j], opt[i][j-1])
                if opt[i-1][j] > opt[i][j-1]:
                    pi = "arrow_up"
                else:
                    pi = "arrow_left"

    length = opt[m][n]
    print(length)

    i = m
    j = n
    S = [""] * (length)
    while i > 0 and j > 0:
        if pi == "arrow_corner":
            S[length-1] = A[i-1]
            i -= 1
            j -= 1
            length -= 1

        elif pi == "arrow_up":
            i -= 1
        else:
            j -= 1
            
    print("".join(S))



def main():
    
    # Read the input data.
    #A = "bacdca"
    #B = "adbcda"  
    for x in range (1):
        A = str(input("Enter the first string:"))
        if 'Exit' == A:
            break

    for y in range (1):
        B = str(input("Enter the second string:"))
        if 'Exit' == B:
            break
            
    m = len(A)
    n = len(B)
    lcs(A, B, m, n)
   

if __name__ == '__main__':
    main()