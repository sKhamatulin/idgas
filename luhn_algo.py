from lesson5 import get_sum_1

card_number = '5536913756577538'

last_num = int(card_number[len(card_number) - 1])

rest_of_nember = card_number[0: len(card_number) - 1]

sum_1 = 0
sum_2 = 0
sum_3 = 0

for i in range(0, len(rest_of_nember)):
    if i%2 == 0:
        elem = int(rest_of_nember[i]) * 2
        if elem >= 10:
            elem = elem - 9
            sum_1 += elem
        else:
            sum_1 += elem
    else:
        elem = int(rest_of_nember[i])
        sum_2 += elem


sum_3 = sum_1 + sum_2


check_num = 0

while (sum_3%10) != 0:
    sum_3 += 1
    check_num += 1


# print(rest_of_nember + str(check_num) == card_number)

print(f'some sum is {get_sum_1("12413523875236587316478235567823645")}')
