import random

def cube_throw() -> int:
    return random.randint(1,6)

def throw_two_hundred_times() -> int:
    x = 0
    for i in range(200):
        if cube_throw() == 6:
            x += 1
    return x

def over_30_check() -> int:
    return int(throw_two_hundred_times() >= 30)

def main():
    x = 0
    for i in range(1000):
        if over_30_check() == 1:
            x += 1
    print("the x we got: ", x)
    print("the probability: ", x/ 1000)

main()
# The result we get approx 0.76 matches the probability from question 5 (א) -> 0.7673 using the normal approximation

