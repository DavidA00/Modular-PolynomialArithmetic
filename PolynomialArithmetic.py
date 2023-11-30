# DEG 2 3 4 5 6 7 
L2= [1,1,1]
L3= [1,1,0,1]
L4= [1,1,0,0,1]
L5= [1,0,0,1,0,1]
L6= [1,0,0,0,0,1,1]
L7= [1,0,0,0,0,0,1,1]

# Irreducible Polynomial degree 8
L8 = [0]*9
L8[8] = 1
L8[4] = 1
L8[3] = 1
L8[1] = 1
L8[0] = 1
L8.reverse()

# Irreducible Polynomial degree 163
L163 = [0]*164
L163[163] = 1
L163[99] = 1
L163[97] = 1
L163[3] = 1
L163[0] = 1
L163.reverse()

# Irreducible Polynomial degree 233
L233 = [0]*234
L233[233] = 1
L233[201] = 1
L233[105] = 1
L233[9] = 1
L233[0] = 1
L233.reverse()

# Irreducible Polynomial degree 239
L239 = [0]*240
L239[239] = 1
L239[207] = 1
L239[111] = 1
L239[47] = 1
L239[0] = 1
L239.reverse()

# Irreducible Polynomial degree 283
L283 = [0]*284
L283[283] = 1
L283[249] = 1
L283[219] = 1
L283[27] = 1
L283[0] = 1
L283.reverse()

# Irreducible Polynomial degree 409
L409 = [0]*410
L409[409] = 1
L409[377] = 1
L409[185] = 1
L409[57] = 1
L409[0] = 1
L409.reverse()

# Irreducible Polynomial degree 571
L571 = [0]*572
L571[571] = 1
L571[507] = 1
L571[475] = 1
L571[417] = 1
L571[0] = 1
L571.reverse()

degree_lists = {
        2: L2,
        3: L3,
        4: L4,
        5: L5,
        6: L6,
        7: L7,
        8: L8,
        163: L163,
        233: L233,
        239: L239,
        283: L283,
        409: L409,
        571: L571
}
    


def DectoBin(decimal_number):
    return bin(int(decimal_number))[2:]

def HextoBin(hex_string):
    return bin(int(hex_string, 16))[2:]

def BintoPoly(binary_string,deg):
    # assumes the user would never give a binary string of length longer than is required (ie that of M -1 )
    return Mod( [int(bit) for bit in (binary_string)], deg) 

def DectoPoly(dec,deg):
    return BintoPoly(DectoBin(dec),deg)

def HextoPoly(dec,deg):
    return BintoPoly(HextoBin(dec), deg)

def PolytoBin(binary_list):
    x = ''.join(map(str, (binary_list)))
    return x

    
def PolytoHex(binary_list):
    binary_str = PolytoBin(binary_list) 
    decimal_number = int(binary_str, 2)
    hex_string = hex(decimal_number)[2:]  # [2:] removes the '0x' prefix
    return hex_string

def PolytoDec(binary_list):
    binary_str = PolytoBin(binary_list)
    decimal_number = int(binary_str, 2)
    return decimal_number

def MakeGF2(L):
    for i in range(0,len(L)):
        L[i] = L[i]%2
    return L


#Printing function
def PolyPrint(L):
    if(len(L)==0): 
        print("There is no Polynomial!")
        return
    for i in range(len(L)-1):
        if(L[i]==1 and (len(L)-i-1 != 1)):
            print("x^" + str(len(L)-i-1) ,end= " + ")
        elif(L[i]==1 and (len(L)-i-1 == 1)):
            print("x",end= " + ")
    if (L[len(L)-1] == 1):
        print(1)
    else: print(0)

def getMfromdeg(deg):
    return degree_lists[deg]



#Modular Addition
def Add(A, B):
    X= MakeGF2(A.copy())
    Y= MakeGF2(B.copy()) 
    result = []
    X.reverse()
    Y.reverse()
    for i in range(max(len(X), len(Y))):
        bit_X = X[i] if i < len(X) else 0
        bit_Y = Y[i] if i < len(Y) else 0
        result.append(bit_X ^ bit_Y) 

    result.reverse()
    while len(result) > 0 and result[0] == 0:
        result.pop(0)

    return result

def Sub(L1, L2):
    t= Add(L1,L2)
    #print("as a result of subtracting", L1, "and", L2, " we get ", t)
    return t 
#Modular Substraction same as addition

## what follows is an alternative slow way of implementing multiplication 
# Normal Multiplication
# def Mult(L1,L2):
#     deg = len(L1)+len(L2)-2
#     mult = [0]*(deg+1)
#     for i in range (len(L1)):
#         for j in range (len(L2)):
#             mult[i+j] = (L1[i]*L2[j] + mult[i+j])%2
#     return mult

# # Mod of 2 polynomial
# def ModMult(L1, L2 , M):
#
#     #let us get the raw molar multiplication polynomial
#     L3 = Mult(L1,L2)
#     #let us get the irreductable polynomial
#     return Mod(L3,M)
#let us get the irreductable polynomial
def Mult(X, Y):
    X= MakeGF2(X)
    Y= MakeGF2(Y)
    product = [0] * (len(X) + len(Y) - 1)

    # Perform polynomial multiplication using shift and XOR
    for i in range(len(X)):
        for j in range(len(Y)):
            product[i + j] ^= X[i] & Y[j]
    #print("as a result of multiplying", X, "and", Y, " we get ", t)
    return product

def Mod(L , deg):

    """we are interested in when M is irreducible, but this function works just fine if its not"""

    M = getMfromdeg(deg)
    
    quotient = [0] * len(L)


    for i in range(len(L) - len(M) + 1):
        for j in range(len(M)):
            quotient[i + j] ^= L[i] & M[j]

        if quotient[i] == 1:
            for j in range(len(M)):
                L[i + j] ^= M[j]

    L1 = L[-len(M) + 1:]
    
    sol = [0]* (len(M)-1)
    
    i= len(L1)-1
    j= len(sol)-1
    if i==j: 
        return L1
    elif i<j:
        sol = [0]* (len(M)-1)
        for i in range(len(L1)-1,-1,-1):
            sol[j] = L1[i]
            j-=1 
            
        return sol
        
    else: 
        return L1[-(len(M)-1):]

def xor(a, b):
    # initialize result
    result = []

    # Traverse all bits, if bits are same, then XOR is 0, else 1
    for i in range(len(b)):
        if a[i] == b[i]:
            result.append(0)
        else:
            result.append(1)

    return result

def quot(A, B):
    # Number of bits to be XORed at a time.
    divisor = B.copy()
    dividend= A.copy()
    while len(dividend) > 0 and dividend[0] == 0:
            dividend.pop(0)
    while len(divisor) > 0 and divisor[0] == 0:
            divisor.pop(0)


    pick = len(divisor)

    # Slicing the dividend to appropriate length for a particular step
    tmp = dividend[0: pick]
    quot= [] 

    while pick < len(dividend):
        while len(tmp) > 0 and tmp[0] == 0:
            tmp.pop(0)

        
        if len(tmp)== len(divisor):
            quot.append(1)
            # Replace the dividend by the result of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + [dividend[pick]]
             

        else:  
            tmp = xor([0]*len(tmp), tmp) + [dividend[pick]]
            quot.append(0)
        # Increment pick to move further
        pick += 1

    # For the last n bits, we have to carry it out normally, as an increased value of pick
    # will cause Index Out of Bounds.
    
    while len(tmp) > 0 and tmp[0] == 0:
        tmp.pop(0)
    
    if len(tmp)== len(divisor):
        quot.append(1) 
    else: 
        quot.append(0) 

    return quot


def gcd(X,Y,deg):
    """ this function returns gcd(X,Y)mod(M)"""
    
    M = getMfromdeg(deg)

    def EA(A,B):
        if B==0: return A
        R = Mod(A, B)
        return EA(B,R )
    A= X
    B= Y
    Temp = EA(A,B)
    return Mod(Temp,M)
    
# function for extended Euclidean Algorithm 
# def gcdExtended(A, B, M): 
#     """we are interested to use this function when B= M """
#     if PolytoDec(A) == 0 : 
#         return B, Mod([0],M) , Mod([1], M) 
#     gcd,X1,Y1 = gcdExtended(Mod(B,A), A, M) 
#     X = Sub (Y1 , Mult(quot(B,A,M), X1 , M ),M ) 
#     Y = X1 
#     return gcd,X,Y

def EEA( A1,A2,A3,B1,B2,B3,deg):
    # print("start of round", 5-c)
    # print("we have A1,A2,A3",A1,A2,A3)
    # print ("WE have B1,B2,B3",B1,B2,B3)
    if sum(B3) == 0:
        return A3, -1, -1
    if sum( B3[:len(B3)-1])==0 and B3[len(B3)-1]==1:
        # in this case, we have B2 as the inverse 
        return B3,B2,B1

    # print("the quotient before mod is", temp)
    Q= Mod(quot(A3, B3), deg) 
    # print( "the quotient for this round is", Q)
    T1 = Mod (Sub(A1, Mult(Q,B1)), deg) 
    T2 = Mod( Sub(A2, Mult(Q,B2)),  deg ) 
    # print (" Q* B3 = ", temp)
    T3 = Mod(Sub(A3, Mult(Q, B3)) , deg) 
    # print("end of round",5-c)
    # print("we have A1,A2,A3",B1,B2,B3)
    # print ("WE have B1,B2,B3",T1,T2,T3)
    return EEA (B1,B2, B3 ,T1,T2,T3, deg)

def Inverse( b , deg):
    M= getMfromdeg(deg)
    gcd, X, Y = EEA(Mod([1], deg),Mod([0],deg), M ,Mod([0],deg), Mod([1], deg),b,deg) 
    return X

def Div( A, B,deg ):
    return Mult(A, Inverse(B,deg))

# print("hello world")

# # x= input ("please choose 1 for binary, 2 for hexadecimal, 3 for decimal: ")
# X = input("please enter A\n")
# Y= input("please enter B\n")


# deg = 4

# A= BintoPoly(X,deg)
# B= BintoPoly(Y,deg)
# print("the inverse of B is\n")
# PolyPrint(Inverse (B,deg))
# print (" the addition is \n") 
# PolyPrint(Mod(Add(A,B),deg))
# print ("the subtraction is\n")
# PolyPrint(Mod(Sub(A,B),deg))
# print("the multiplication is\n")
# PolyPrint(Mod(Mult(A,B),deg) )
# print("the division is\n")
# PolyPrint(Mod(Div(A,B,deg),deg) )
# print("the quot is\n")
# PolyPrint(Mod(quot(A,B),deg) )







