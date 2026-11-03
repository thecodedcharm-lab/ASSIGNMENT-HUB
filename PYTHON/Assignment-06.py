# # # Level 1 — Basic Patterns


# # Q1. Solid Square

# N = int(input("Enter Number : "))
# for i in range (1,N+1):
#     for j in range (1,N+1):
#         print("*",end=" ")
#     print()

# # Q2. Solid Rectangle

# row = int(input("Enter Number of rows : "))
# columns = int(input("Enter number of columns : "))
# for i in range(row):
#     for j in range (columns):
#         print("*",end="")
#     print()

# # Q3. Increasing Star Triangle

# N = int(input("Enter Number: "))
# for i in range(1, N + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

# # Q4. Increasing Number Triangle

# N = int(input("Enter N : "))
# for i in range (1,N+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# # Q5. Repeated Number Triangle

N = int(input("Enter N : "))
for i in range (1,N+1):
    for j in range (1,i+1):
        print(i ,end=" ")
    print()

# # Q6. Repeated Alphabet Triangle

# N = int(input("Enter N : "))
# for i in range(1,N+1):
#     for j in range (1,1+i):
#         print(chr(64+ i),end=" ")
#     print()

# # Q7. Alphabet Triangle

# N = int(input("Enter N : "))
# for i in range (1,N+1):
#     for j in range (1,i+1):
#         print(chr(64+j),end=" ")
#     print()

# # Q8. Continuous Number Triangle

# N = int(input("Enter N : "))
# num=1
# for i in range (1,N+1):
#     for j in range (i):
#         print(num,end=" ")
#         num=num+1
#     print()

# # Q9. Alternating 0–1 Triangle

# N = int (input("Enter N : "))
# for i in range(1,1+N):
#     for j in range(i):
#         if (i+j) % 2 == 0:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()

# # Q10. Decreasing Star Triangle

# N = int ( input ("Enter N : "))
# for i in range (N,0,-1):
#     for j in range (i):
#         print("*",end=" ")
#     print()

# # Q11. Decreasing Number Triangle

# n = int(input("Enter N : "))
# for i in range (n,0,-1):
#     for j in range (1,1+i):
#         print(j, end=" ")
#     print()

# # Q12. Decreasing Alphabet Triangle

# n = int(input("Enter N : "))
# for i in range (n,0,-1):
#     for j in range(1,1+i):
#         print(chr(64+j),end=" ")
#     print()



# # # Level 2 — Spaces and Alignment



# # Q13. Right-Aligned Half Pyramid

# N = int(input("Enter N : "))
# for i in range(1,N+1):
#     for j in range (N-i):
#         print(" ",end = " ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# # Q14. Inverted Right-Aligned Half Pyramid

# N = int(input("Enter N : "))
# for i in range(N,0,-1):
#     for j in range (N-i):
#         print(" ",end = " ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# # Q15. Star Pyramid

# N = int(input("Enter N : "))
# for i in range(1,N+1):
#     for j in range(N - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()  

# #Q16. Inverted Star Pyramid

# N = int(input("Enter N : "))
# for i in range(N,0,-1):
#     for j in range(N - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()  

# # Q17. Solid Diamond

# N = int(input("Enter N : "))
# for i in range(1,N+1):
#     for j in range(N - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()
# for a in range(N-1,0,-1):
#     for b in range(N - a):
#         print(" ", end=" ")
#     for c in range(1, 2 * a):
#         print("*", end=" ")
#     print()  

# # Q18. Rhombus

# N = int(input("Enter N : "))
# for i in range(N,0,-1):
#     for j in range(i,0,-1):
#         print(" ",end=" ")
#     for k in range (N):
#         print("*",end=" ")
#     print()

# # Q19. Mirrored Number Pattern

# N = int(input("Enter N : "))
# for i in range(1, N + 1):
#     for j in range(1,1+i):
#         print(j, end=" ")
#     for k in range(2 * (N - i)):
#         print(" ", end=" ")
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# # Q20. Centered Number Pyramid

# N = int(input("Enter Number : "))
# for i in range(1,1+N):
#     for j in range (N-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print(i,end=" ")
#     print()

# # Q21. Palindromic Number Pyramid

# N = int(input("Enter N : "))
# for i in range(1, N + 1):
#     for k in range (N-i):
#         print(" ",end=" ")
#     for j in range(1,1+i):
#         print(j, end=" ")
#     for j in range(i-1, 0, -1):
#         print(j, end=" ")
#     print()

# # Q22. Alphabet Palindrome Pyramid

# N = int(input("Enter N : "))
# for i in range(1, N + 1):
#     for k in range (N-i):
#         print(" ",end=" ")
#     for j in range(1,1+i):
#         print(chr(64+j), end=" ")
#     for j in range(i-1, 0, -1):
#         print(chr(64+j), end=" ")
#     print()

# Q23. Reverse-Starting Alphabet Triangle

# n = int(input("Enter N : "))
# for i in range (1,n+1):
#     for j in range(n - i + 1, n + 1):
#         print(chr( 64 + j ),end=" ")
#     print()



# # # Level 3 — Mixed Logic and Repeated Sequences



# # Q24. Increasing and Decreasing Star Triangle

# N = int(input("Enter Number: "))
# for i in range(1, N + 1):
#     for j in range(i):
#         print("*", end="")
#     print()
# for a in range (N-1,0,-1):
#     for b in range(a):
#         print("*", end="")
#     print()

# # Q25. Number Hourglass

# N = int(input("Enter N : "))
# for a in range (N,0,-1):
#     for b in range (1,1+a):
#         print(b, end=" ")
#     print()
# for i in range (2,N+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# # Q26. Alphabet Hourglass

# N = int(input("Enter N : "))
# for a in range (N,0,-1):
#     for b in range (1,1+a):
#         print(chr(64+b), end=" ")
#     print()
# for i in range (2,N+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()

# # Q27. Alternating Star and Hash Grid

# N =  int(input("Enter N : "))
# for i in range(N):
#     for j in range (N):
#         if ((i + j) % 2 == 0):
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()

# # Q28. Binary Checkerboard

# N =  int(input("Enter N : "))
# for i in range(N):
#     for j in range (N):
#         if ((i + j) % 2 == 0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()

# # Q29. Multiplication Grid

# N =  int(input("Enter N : "))
# for i in range(1,N+1):
#     for j in range (1,N+1):
#         print(i*j,end=" ")
#     print()

# # Q30. Alternating-Direction Rows

# N =  int(input("Enter N : "))
# for i in range(1,N+1):
#     if i % 2 == 0:
#         for j in range (i,0,-1):
#             print(j,end=" ")
#     else:
#         for j in range (1,i+1):
#             print(j,end=" ")
#     print()

# # Q31. Number Diamond

# N = int(input("Enter N : "))


# for i in range(1, N + 1):
#     for k in range(N - i):
#         print(" ", end=" ")
#     for j in range(1, 1 + i):
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
#     print()
# for i in range(N - 1, 0, -1):
#     for k in range(N - i):
#         print(" ", end=" ")
#     for j in range(1, 1 + i):
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
#     print()

# # Q32. Concentric Number Square

# N = int(input("Enter N: "))
# size = 2 * N - 1
# for i in range(size):
#     for j in range(size):
#         if i < j and i < size-1-i and i < size-1-j:
#             value = N - i
#         elif j < size-1-i and j < size-1-j:
#             value = N - j
#         elif size-1-i < size-1-j:
#             value = N - (size-1-i)
#         else:
#             value = N - (size-1-j)
#         print(value, end=" ")
#     print()


# # # Level 4 — Hollow Patterns and Conditions

# #  Q33. Hollow Square

# N =  int(input("Enter N : "))
# for i in range(N):
#     for j in range (N):
#         if i == 0 or i == N-1 or j == 0 or j == N-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# # Q34. Hollow Rectangle

# row =  int(input("Enter row : "))
# column =  int(input("Enter column : "))

# for i in range(row):
#     for j in range (column):
#         if i == 0 or i == row-1 or j == 0 or j == column-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# # Q35. Hollow Number Square

# N =  int(input("Enter N : "))
# for i in range(N):
#     for j in range (N):
#         if i == 0 or i == N-1 or j == 0 or j == N-1:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()

# # Q36. Hollow Right-Angled Triangle

# N =  int(input("Enter N : "))
# for i in range(N):
#     for j in range (i+1):
#         if i == N - 1 or j == 0 or j == i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# N = int(input("Enter N: "))

# # Q37. Hollow Inverted Triangle

# N = int(input("Enter N: "))
# for i in range(N):
#     for j in range(N - i):
#         if i == 0 or j == 0 or j == N - i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # Q38. Hollow Pyramid

# N = int(input("Enter N : "))
# for i in range (N+1):
#     for j in range (N-i):
#         print(" ",end= " ")
#     for k in range (1,2*i):
#         if k == 1 or k == (2 * i - 1) or i == N:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print( )
    
# # Q39. Hollow Diamond

# N = int(input("Enter N : "))
# for i in range (N+1):
#     for j in range (N-i):
#         print(" ",end= " ")
#     for k in range (1,2*i):
#         if k == 1 or k == (2 * i - 1) :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print( )
# for i in range (N - 1, 0, -1):
#     for j in range (N-i):
#         print(" ",end= " ")
#     for k in range (1,2*i):
#         if k == 1 or k == (2 * i - 1) :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print( )

# # Q40. X Pattern

# N = int(input("Enter N : "))
# for i in range(N):
#     for j in range (N):
#         if i == j or i + j == N - 1:
#             print("X",end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # Q41. Cross Pattern

# N = int(input("Enter N : "))
# mid = N // 2
# for i in range(N):
#     for j in range(N):
#         if i == j or i + j == N - 1 or i == mid :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # Q50. Custom Symbol Square

# N = int(input("Enter Number : "))
# symbol = input("Enter Symbol: ")
# for i in range (1,N+1):
#     for j in range (1,N+1):
#         print(symbol,end=" ")
#     print()

# # Q51. User-Sized Hollow Rectangle

# row =  int(input("Enter row : "))
# column =  int(input("Enter column : "))

# for i in range(row):
#     for j in range (column):
#         if i == 0 or i == row-1 or j == 0 or j == column-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# Q52. Create Your Own Pattern
N = int(input("Enter N (odd number recommended) : "))
mid = N // 2
for i in range(N):
    for j in range(N):
        if j == 0 or (i <= mid and j == mid - i + 1) or (i > mid and j == i - mid):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    
