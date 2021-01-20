#simple exception implementation

try:
    age = int(input('Enter your age: '))
except ValueError:
    print('Invalid value')
