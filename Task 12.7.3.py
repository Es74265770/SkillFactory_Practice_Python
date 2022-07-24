# Задание 12.7.3

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

per_cent_list = list(per_cent.values())

money = int(input("Введите сумму: "))

a = float(per_cent_list[0])
b = float(per_cent_list[1])
c = float(per_cent_list[2])
d = float(per_cent_list[3])
e = money

a = round(e*a/100)
b = round(e*b/100)
c = round(e*c/100)
d = round(e*d/100)

deposit = [a, b, c, d]

print("deposit = ", deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))


