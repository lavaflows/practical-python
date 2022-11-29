# bounce.py
#
# Exercise 1.5

height = 100.0
bounce = 1

while bounce <= 10:
    height = height * (3/5)
    print(bounce, ' ', round(height,4))
    bounce += 1
