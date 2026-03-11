correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Käyttäjätunnus: ")
    password = input("Salasana: ")

    if username == correct_username and password == correct_password:
        print("Tervetuloa")
        break
    else:
        attempts += 1
        if attempts == 5:
            print("Pääsy evätty")
        else:
            print("Väärä tunnus tai salasana, yritä uudelleen.")