def passwort_prufen():
    user_name="Siva"
    richtiges_passwort="12345"
    Enter_Name=input("Your User-Name please:")

    if Enter_Name==user_name:

       for versuche in range (1,4):
           passwort=input(f"versuche {versuche}/3 - Passwort eingeben:")

           if passwort==richtiges_passwort:
              print("You are Welcome")
              break

           else:
                print("Wrong passwort!")
        
       else:
           print("Contact Admin please")

    else:
        print("User is not Found!")

passwort_prufen()

