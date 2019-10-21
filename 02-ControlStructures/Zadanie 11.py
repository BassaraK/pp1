nazwa = "marek"
haslo = "m-123"
login = input("Podaj login: ")
password = input("Podaj hasło: ")
if login==nazwa and password==haslo:
    print("Zalogowałeś się pomyślnie")
else:
    print("Podane dane są nie prawidłowe")