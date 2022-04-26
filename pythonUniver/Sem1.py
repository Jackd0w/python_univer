import math

b = int(input("Введите b"))
z1 = (math.sqrt(2*b + 2*math.sqrt(pow(b, 2) - 4)))/(math.sqrt(pow(b, 2) - 4) + b + 2)
z2 = 1/(math.sqrt(b + 2))

if __name__ == "__main__":
    print(z1)
    print(z2)17