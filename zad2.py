import math


def is_number_prime(*numbers):
    for num in numbers:
        if num == 0 or num == 1:
            print(f"{num} to nie liczba pierwsza.")
        elif num == 2 or num == 3:
            print(f"{num} jest liczbą pierwsza")
        else:
            flag = False
            i = 2
            while i in range(2, math.ceil(math.sqrt(num))):
                if num % i == 0:
                    flag = False
                    break
                else:
                    flag = True
                i += 1

            if flag:
                print(f"{num} jest liczba pierwsza")
            else:
                print(f"{num} nie jest liczba pierwsza")


is_number_prime(0, 1, 2, 3, 8, 12, 13, 54)
