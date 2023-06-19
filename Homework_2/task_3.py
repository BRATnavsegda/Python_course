# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions
import math


def get_fraction_numbers(fraction):
    nums = fraction.split('/')
    for i in range(nums.__len__()):
        nums[i] = int(nums[i])
    return nums


def addition(na, da, nb, db):
    """na/da + nb/db"""
    g = math.gcd(da, db)
    if g == 1:
        return [na * db + da * nb, da * db]
    s = da // g
    t = na * (db // g) + nb * s
    g2 = math.gcd(t, g)
    if g2 == 1:
        return [t, s * db]
    return [t // g2, s * (db // g2)]


def multiplication(na, da, nb, db):
    """na/da * nb/db"""
    g1 = math.gcd(na, db)
    if g1 > 1:
        na //= g1
        db //= g1
    g2 = math.gcd(nb, da)
    if g2 > 1:
        nb //= g2
        da //= g2
    result = [na * nb, db * da]
    g3 = math.gcd(result[0], result[1])
    if g3 > 1:
        for i in range(result.__len__()):
            result[i] = int(result[i] / g3)

    return result


def rounding(lst):
    g1 = math.gcd(lst[0], lst[1])
    if g1 > 1:
        for i in range(lst.__len__()):
            lst[i] = int(lst[i] / g1)
    return lst


def list_to_frac(lst):
    return f'{lst[0]}/{lst[1]}'


fraction_1 = get_fraction_numbers(input("Enter fraction №1: "))
fraction_2 = get_fraction_numbers(input("Enter fraction №2: "))

print("\nFractions module: ")
f1 = fractions.Fraction(fraction_1[0], fraction_1[1])
f2 = fractions.Fraction(fraction_2[0], fraction_2[1])

print(f'{f1} + {f2} = {f1 + f2}')
print(f'{f1} * {f2} = {f1 * f2}')

print("\nMy program: ")
add_fractions = rounding(addition(fraction_1[0], fraction_1[1], fraction_2[0], fraction_2[1]))
mul_fractions = rounding(multiplication(fraction_1[0], fraction_1[1], fraction_2[0], fraction_2[1]))

print(f'{list_to_frac(fraction_1)} + \
{list_to_frac(fraction_2)} = \
{list_to_frac(add_fractions)}')

print(f'{list_to_frac(fraction_1)} * \
{list_to_frac(fraction_2)} = \
{list_to_frac(mul_fractions)}')



