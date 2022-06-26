print('start')
height = int(input('Enter the hieght of the animal in feet: '))
if height <= 1  :
    print("Given height of the animal is Short!")
    squeak = str(input("your animal can squeak or not?, yes/no: "))
    if squeak == "yes" :
        print("it might be a Rat!")
    else :
        print("it might be a Squirrel!")
else:
    print("Given height of the animal is Tall!")
    neck = str(input("what is height of neck?, short/tall: "))
    if neck == 'short' :
        nose = str(input("what is the size of the nose?, small/large:  "))
        if nose == 'large' :
            place = str(input("where does that animal live?, on land/in water: "))
            if place == 'on land' :
                print("it might be a rhinoceros")
            else:
                print("it might be a Hippo")
        else:
            print("it might be an elephant")
    else:
        print("it might be a giraffe")
