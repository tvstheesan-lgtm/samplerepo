def passwort_prufen():
    User_Name="Siva"
    Richtiges_Password="12345"

    versuche=0
    Enter_Name=input("Your User _Name please;")
    if Enter_Name == User_Name:
       while versuche<3:
          Passwort=input("Passwort eigeben;")
          if Passwort==Richtiges_Password:
            print("Welcome to Myworld!")
            break

          else:
            versuche= versuche + 1
            print("Wrong passwort!")

       if versuche==3:
        print("Contact admin ")

    else:
      print("User is not found")

passwort_prufen()


