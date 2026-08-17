
import sys
print("Python version:", sys.version)

print("3 + 4 =", 3 + 4)
print("3 - 4 =", 3 - 4)
print("3 * 4 =", 3 * 4)
print("3 % 4 =", 3 % 4)
print("3 / 4 =", 3 / 4)
print("3 ** 4 =", 3 ** 4)
print("3 // 4 =", 3 // 4)

print("Stanley")
print("Sunwoo")
print("USA")
print("I am enjoying 30 days of python")

# 4. Check data types
print("Type of 10:", type(10))
print("Type of 9.8:", type(9.8))
print("Type of 3.14:", type(3.14))
print("Type of 4 - 4j:", type(4 - 4j))
print("Type of ['Asabeneh', 'Python', 'Finland']:", type(['Asabeneh', 'Python', 'Finland']))
print("Type of 'Your name':", type("Stanley"))
print("Type of 'Your family name':", type("Sunwoo"))
print("Type of 'Your country':", type("USA"))

import math
x1, x2 = 2, 3
y1, y2 = 10, 8

distance =  math.sqrt((x2-x1)**2 + (y2-y1)**2)
print ("euclidean distance:", distance)