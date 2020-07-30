"""
We need to design the algorithm for arrange the words.
"""

digit = ['', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
digit2 = ['ten', 'eleven', 'twelve', 'thir', 'for',
          'fif', 'six', 'seven', 'eigh', 'nine', 'twenty']

def main():

    total = 0
    for i in range(1, 1001):
        total += len(words(i))
        print(i, words(i), len(words(i)))
    
    print(total)

def twodigits(number):
    answer = ''

    if number < 13:
        answer = digit2[number % 10]
    elif number == 14:
        answer = 'fourteen'
    elif number < 20:
        answer = f'{digit2[number%10]}teen'
    elif number < 30:
        answer = f'{digit2[-1]} {digit[number%10]}'
    else:
        answer = f'{digit2[number//10]}ty {digit[number%10]}'

    return answer

def words(number):
    answer = ''

    if (number < 10):
        answer = digit[number]

    elif (number < 100):
        answer = twodigits(number)

    elif (number < 1000):
        if number % 100 == 0:
            answer = f'{digit[number//100]} hundred'
        elif number % 100 < 10:
            answer = f'{digit[number//100]} hundred and {digit[number%100]}'
        else:
            answer = f'{digit[number//100]} hundred and {twodigits(number%100)}'
    else:
        answer = 'one thousand'

    return answer.replace(' ', '')

if __name__ == "__main__":
    main()
