print('Я очень простой калькулятор, посчитаем?', '\n')

def start():
    try:
        num1 = float(input('Введи 1ое число: '))
        num2 = float(input('Введи 2ое число: '))
    except ValueError:
        print('Это не число, попробуй снова', '\n')
        start()
    operation = choose_operation()
    result = calculating(num1, num2, operation)
    print(f"У меня получилось: {result} \n")

def choose_operation():
    question = """
Что будем делать? Я умею:

Складывать: +
Вычитать: -
Умножать: *
Делить: /

Выбери действие: """

    correct = '+-*/'
    operation = input(question)

    while operation not in correct:
        print('Я так не умею, выбери снова.')
        operation = input(question)
    return operation

def calculating(num1, num2, operation):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print('Мне запрещено делить на ноль, придется начинать сначала.', '\n')
            start()
    return result

start()

def end():
    while True:
        wish = (input('Посчитаем ещё? (да/нет) ')).lower()
        right = ['да', 'нет']
        while wish not in right:
            print('Либо да, либо нет, третьего не дано')
            wish = (input('Посчитаем ещё? (да/нет) ')).lower()
        if wish == 'да':
            start()
        elif wish == 'нет':
            print( '\n' 'Приходи ещё посчитать :)')
            break
end()