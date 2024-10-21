def euclid(A,B):
    R = A%B
    print(A,B)
    if R == 0:
        return A
    return euclid(B,R)

print(euclid(192,162))