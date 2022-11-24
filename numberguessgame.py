
import random
import time

print("hi welcome to guessing game plaese choose a number between 1 to 100")
print("im picking a number hmmm.")
time.sleep(1)
print("im picking a number hmmm..")
time.sleep(1)
print("im picking a number hmmm...")
time.sleep(1)
print("Right, I've picked a number, lets guess it")
time.sleep(2)

guess = int(input("what is ur guess : "))


correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("wrong, you need to guess higher. guess another one : "))
    else:
        guess = int(input("wrong you need to guess lower.what is ur guess : "))

print(f"you got the right answer, right answer was {correct_number} it took you {guess_count} times to get it right")

