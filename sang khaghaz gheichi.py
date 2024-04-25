import random

tedad_bord_karbar=0
tedad_bord_computer=0
options=["s" , "k" , "g"]

while True:
    karbar_input=input("baraye shrooe bazi sang : s / kaghaz : k / gheichi : g ra vared konid va baraye khorooj q ra vared konids").lower()

    if (karbar_input=="q"): break

    if (karbar_input not in options): continue

    random_num=random.randint(0,2)

    computer_rand=options[random_num]

    if (karbar_input=="s" and computer_rand=="g"):
        print("To Bordi tabrik migam :)")

    elif (karbar_input=="k" and computer_rand=="s") or (karbar_input=="g" and computer_rand=="k"):
       print("To Bordi tabrik migam :)")

       tedad_bord_karbar+=1

    elif (karbar_input=="g" and computer_rand=="s"):
        print("man bordam :)")

    elif (karbar_input=="s" and computer_rand=="k") or (karbar_input=="k" and computer_rand=="g"):
       print("man bordam :)")

       tedad_bord_computer+=1

    else:
        karbar_input==computer_rand
        print("che jaleb mosavi shodim :|")

print("to:", tedad_bord_karbar )
print("man:", tedad_bord_computer )
