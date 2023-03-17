x = input()
y = input()

try:
    z = int(x) / int(y)
except Exception as e:
    print(e)
