from random import randint

# 4. Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

rand_int = randint(0, 1)
attempts = 10

print("\nGuess the number from 0 to 1000 in 10 attempts")

while attempts != 0:
    user_number = int(input("\nEnter your number: "))
    if user_number > rand_int:
        attempts -= 1
        print(f"\nThe hidden number is less, you still have {attempts} attempts")
    elif user_number < rand_int:
        attempts -= 1
        print(f"\nThe hidden number is greater, you still have {attempts} attempts")
    else:
        print("\U0001F44F Great!!! \U0001F44F \U0001F609")
        break

else:
    print("\n\U00002620 \U0001F136\U0001F130\U0001F13C\U0001F134   \U0001F13E\U0001F145\U0001F134\U0001F141 \U00002620")
