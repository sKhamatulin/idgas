card_number = '5536913756577538'


def get_last_num(number):
    return int(number[len(number) - 1])


def get_first_part(number):
    return number[0: len(number) - 1]


def get_sum_1(number):
    sum_1 = 0
    for i in range(0, len(number)):
        if i%2 == 0:
            elem = int(number[i]) * 2
            if elem >= 10:
                elem = elem - 9
                sum_1 += elem
            else:
                sum_1 += elem    
    return sum_1


def get_sum_2(number):
    sum_2 = 0
    for i in range(0, len(number)):
        if i%2 != 0:
            elem = int(number[i])
            sum_2 += elem
    return sum_2


def get_sum_3(first_part, second_part):
    sum_3 = first_part + second_part
    return sum_3


def get_check_num(sum):
    check_num = 0
    while (sum%10) != 0:
        sum += 1
        check_num += 1
    return check_num


def get_new_number(first_part, num):
    return first_part + str(num)


def is_correct(value_1, value_2):
    return value_1 == value_2


if __name__ == '__main__':
    last_num = get_last_num(card_number)
    first_part = get_first_part(card_number)
    sum_1 = get_sum_1(first_part)
    sum_2 = get_sum_2(first_part)
    sum_3 = get_sum_3(sum_1, sum_2)
    check_num = get_check_num(sum_3)
    new_number = get_new_number(first_part, check_num)
    answer = is_correct(card_number, new_number)
    print(f'answer is {answer}')
