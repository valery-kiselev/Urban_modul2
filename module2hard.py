def ancient_cipher(num):
    list = []
    number = num + 1 // 2
    for i in range(1, number):
        for j in range(i + 1, number):
            if num % (i + j) == 0:
                pass_numbers = str(i) + '-' + str(j)
                list.append(pass_numbers)
    return list

input_number = int(input('Введите число от 3 до 20: '))
print(*ancient_cipher(input_number))