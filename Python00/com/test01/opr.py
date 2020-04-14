# 산술연산

a = 21
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a ** b)

# a 의 b제곱
print(a / b)
print(a // b)
# 몫 (floor division)
print(a % b)
# 나머지

# 비교연산
a, b = 5, 3
print(a == b)
print(a != b)
print(a > b)
print(a <= b)

print(a is b)
print(a is not b)

print(True or False)
print(False and True)
print(not False)

# 범위연산
list01 = list(range(100))
print(list01)
# 0 ~ 99

print(list01[2])
print(list01[12:49])
# 12 ~ 48
print(list01[12:49:3])

# [start: end] -> start ~ end-1
# [start: end: step] -> start, start + step, ... , end-1

str01 = 'Hello, World!'
print(str01)
print(str01[0: 5])#??
print(str01[7:])#???

# reverse
print(str01[-1])
print(str01[-1:])
print(str01[:-1])
print(str01[::-1])

# 멤버연산
list02 = [0, 1, 2, 3, 4]
print(3 in list02)
print(5 not in list02)
print(4 not in list02)













