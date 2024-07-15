number = int(input("Any number: "))

num_sum = 0

while number != 0:
    last_num = number % 10  # берем последнюю цифру числа
    num_sum += last_num
    number //= 10  # отбрасываем последнюю цифру числа

print("num:", number, "sum:", num_sum)
