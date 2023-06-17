# 3. Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MAX_DIGIT = 100000
MIN_DIGIT = 1
message = None

while True:
    user_num = int(input("Enter number from 1 to 100000: "))
    if MIN_DIGIT <= user_num <= MAX_DIGIT:
        break

if user_num != 1:
    for i in range(2, int(user_num ** 0.5) + MIN_DIGIT):
        if user_num % i == 0:
            message = "composite number"
            break
    if not message:
        message = "prime number"
else:
    message = "neither simple nor composite"

print(message)
