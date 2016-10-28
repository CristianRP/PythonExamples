def draw_pascal(n):
    for b in range(0, n):
        z = (b * 2) + 1
        print("   " * n, " 1 " * z)
        n -= 1

#z = (x * 2) + 1
#print(" " * n, "*" * z)
#n -= 1

print(draw_pascal(5))