import sys

def sort_and_count(A):
    n = len(A)
    if len(A) <= 1:
        return A, 0
    center = int( len(A) / 2 )
    B, m1 = sort_and_count(A[:center])
    C, m2 = sort_and_count(A[center:])
    A, m3 = merge_and_count(B, C)
    return A, (m1 + m2 + m3)

def merge_and_count(B, C):
    A = []
    count = 0
    i = j = 0
    
    n1 = len(B)
    n2 = len(C)
    
    while i < n1 and j < n2:
        #if j > n2 or (i <=n1 and B[i] <= C[j]):
        if B[i] <= C[j]:
            A.append(B[i])
            i += 1
            #count += j-1
        else:
            A.append(C[j])
            count += n1 - i
            j += 1
    A += B[i:]
    A += C[j:]
    return A, count


def main():
    
    # Read the input data.
    #A = [3,8,12,20,32,48,5,7,9,25,29]
    
    for x in range (1):
        n = int(input("Enter the value of n:\n"))
        if 'Exit' == n:
            break
        print(f'*****Taking input for n = {n}*****')
    
    A = []    
    for y in range (n):
        z = int(input("Enter the element:"))
        A.append(z)
        if 'Exit' == z:
            break
    
    #print(A)
    inversions = str(sort_and_count(A)[1])

    print("Number of inversions:")
    print(inversions)


if __name__ == '__main__':
    main()
            