name = input("What is your name? ").split(" ")
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user(name[0], name[1])
print("Finish")