# implement fizzbang

for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBang')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Bang')
    else:
        print(num)
