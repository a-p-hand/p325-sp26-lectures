from cmath import sqrt

a_response = input("Enter a: ")
b_response = input("Enter b: ")
c_response = input("Enter c: ")

a = float(a_response)
b = float(b_response)
c = float(c_response)
solution = ((-1*b + sqrt(b**2 - 4 * a * c)) / (2 * a), (-1*b - sqrt(b**2 - 4 * a * c)) / (2 * a))
print(solution)