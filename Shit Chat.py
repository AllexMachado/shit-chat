havingkids = ['yes', 'Yes!', 'I do', 'yup', 'duh', 'yeah']
nothavingkids = ['nah', 'tf no', 'NO!?', 'ew, no', 'no?', 'no', 'No', 'NO']
creator = ['Allex']

def get_valid_name():
    while True:
        name = input("Hi! What was your name again? Since it's been so long we had a chit-chat ")
        if name in creator:
            print("What... no you... you can't be me... Answer YOUR name >:(")
        else:
            return name

def get_valid_age():
    while True:
        age = input("Damn, how old are you now? ")
        if age.isdigit():
            return int(age)
        else:
            print("Tf, that's not an age, tell me your REAL age man.")

def check_kids():
    while True:
        kids = input("Dude... do you... like... have kids now? " if age >= 35 else "Ik is too soon, but do you plan on having kids one day? ")
        if kids in havingkids:
            print("DAMN, so you DID age like a parent...")
            break
        elif kids in nothavingkids:
            print("WOW okay...")
            break
        else:
            print("Dude, be serious.")

name = get_valid_name()
age = get_valid_age()
check_kids()

