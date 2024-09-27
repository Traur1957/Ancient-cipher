def password(number):
    f_num = ''
    for i in range(1, number):
        for j in range(i+1, number):
            if number % (i+j) == 0:
                f_num += str(i) + str(j)
    return f_num


print('Введите число')
print(password(int(input())))