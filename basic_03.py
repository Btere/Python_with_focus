#Boolean operator and comparison operator
#And, or and not operator
# ==, !=, <,>, >=, <=
bot = (3==5) and (6>8)
cag = (5>4) or (9<4)
print(bot)
print(cag)

# Annoying while and if loop
_success = "repetitive habit"
_failure = 4
if _success == "repetitive habit":
    print("Let's stick to the habit daily")
    print("Let's remain focus in the journey of life")

while _failure < 8:
    print("failure is a product of no repetition")
    print("failure is a product of lack of focus, and reason why you live")
    print("It is a product of no plan")
    print("It is a product of no hands-on(Implemetation-action)")
    print("It is a product of looking for help all the time, and feeling weak")

# infinite while loop and how to break out of it
name = ''
while name != 'your name':
    print('Please type your name.')
name = input()
print('Thank you!')

# Another case study with Break statement
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
