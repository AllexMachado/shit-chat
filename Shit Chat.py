name = input("Hi! What was your name again? Since it's been so long we had a shit chat ")

havingkids = ['yes','Yes!','I do','yup','duh','yeah']
nothavingkids = ['nah','tf no','NO!?','ew, no','no?','no','No','NO']
creator = ['Allex']

def check_name(name):
    if name in creator:
        print("What...no you... you can't be me...")
    else:
        check_age(age)

age = input("Damn, how old are you now? ")

def check_age(age):
    if age.isdigit():
        age = int(age)
        print("Damn, you aged...")
        check_ageness(age)
    else:
        print("Tf... that's not an age.")
        return

def check_ageness(age):
    if age >= 35:
        kids = input("Dude...do you...like...have kids now? ")
        check_kids(kids)  
    elif age <= 35:
        print("OOOOh, you're too young you little silly billy :3...")
        kids = input("But do you plan on having kids soon? ")
        check_kids(kids)  

def check_kids(kids):
    if kids in havingkids:
        print("GESSS, so you DID age like a parent...")
    elif kids in nothavingkids:
        print('WOW okay...')
    else:
        print("I guess you didn't answer properly.")

check_name(name)

