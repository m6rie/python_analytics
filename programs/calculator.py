class Calculator():

    def add(self, cal):
        numbers = cal.split('+')

        for number in numbers:
            number1 = float(numbers[0].strip(' '))
            number2 = float(numbers[1].strip(' '))
            return f'Result: {number1 + number2}\n'

    def substract(self, cal):
        numbers = cal.split('-')
        for number in numbers:
            number1 = float(numbers[0].strip(' '))
            number2 = float(numbers[1].strip(' '))
            return f'Result: {number1 - number2}\n'

    def multiply(self, cal):
        numbers = cal.split('*')
        for number in numbers:
            number1 = float(numbers[0].strip(' '))
            number2 = float(numbers[1].strip(' '))
            return f'Result: {number1 * number2}\n'
        
    def divide(self, cal):
        numbers = cal.split('/')
        for number in numbers:
            number1 = float(numbers[0].strip(' '))
            number2 = float(numbers[1].strip(' '))
            return f'Result: {number1 / number2}\n'

new_C = Calculator()

def fetch():
    print(          
        "+---------------------+\n" +
        "|      Calculator     |\n" +
        "+---------------------+\n" +
        "| C | | % | |   | | + |\n" +
        "+---+-+---+-+---+-+---+\n" +
        "| 7 | | 8 | | 9 | | / |\n" +
        "+---+-+---+-+---+-+---+\n" +
        "| 4 | | 5 | | 6 | | X |\n" +
        "+---+-+---+-+---+-+---+\n" +
        "| 1 | | 2 | | 3 | | - |\n" +
        "+---------+-+---+-+---+\n" +
        "|    0    | | . | | = |\n" +
        "+---------------------+\n" +
        "|   Press Q to exit   |\n" +
        "+---------------------+"
    )
    
    math = input('Please enter your calcul: ')
    while math.lower() != 'q':
        if '+' in math:
            print(new_C.add(math))
            fetch()
        elif '-' in math:
            print(new_C.substract(math))
            fetch()
        elif '/' in math:
            try:
                print(new_C.divide(math))
            except ZeroDivisionError:
                print('You cannot divide by 0, sorry!')
            finally:
                fetch()
        elif '*' in math:
            print(new_C.multiply(math))
            fetch()
        else:
            print('Not an operation. Please try again: ')
            fetch()
    else:
        exit()


print(fetch())