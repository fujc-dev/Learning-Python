#

number = 33
convertion = input("请猜数字")
guess = int(convertion)
if guess == number:
    print("OK,干得漂亮")
elif guess > number:
    print("大兄弟,大了")
else:
    print("小了")

