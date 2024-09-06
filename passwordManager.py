import os
import random

_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
_symbols = '~`!@#$%^&*()_-+={[}]|\:;"\'<,>.?/'
_numbers = '0123456789'

def createAccount():
    os.system('cls')
    print("""================================
        PASSWORD MANAGER
================================\n""")
    _accName = input("Account name: ")
    _accLogin = input("Login: ")

    def ask(_accName, _accLogin):
        global passGen
        passGen = input("\nGenerate new password? [Yes/No]: ").lower()

        if passGen == "yes" or passGen == 'y' or passGen == "1":
            def genPassword(passwordAmount, passwordLength, useSymbols, useNumbers):
                print()
                num = 0
                passwords = []
                while 0 < passwordAmount:
                    gen = []
                    for i in range(passwordLength):            
                        if i < 2:
                            rand_letter = random.randrange(2)
                            if rand_letter == 0:
                                gen.append(random.choice(_chars.lower()))
                            else:
                                gen.append(random.choice(_chars))
                                
                        else:
                            if (useSymbols == "Yes" and useNumbers == "Yes"):
                                rand = random.randrange(4)
                                if rand == 0:
                                    gen.append(random.choice(_chars.lower()))
                                elif rand == 1:
                                    gen.append(random.choice(_chars))
                                elif rand == 2:
                                    gen.append(random.choice(_numbers))
                                else:
                                    gen.append(random.choice(_symbols))
                                
                            elif (useNumbers == "Yes" and useSymbols == "No"):
                                rand = random.randrange(3)
                                if rand == 0:
                                    gen.append(random.choice(_chars.lower()))
                                elif rand == 1:
                                    gen.append(random.choice(_chars))
                                else:
                                    gen.append(random.choice(_numbers))
                                    
                            elif (useSymbols == "Yes" and useNumbers == "No"):
                                rand = random.randrange(3)
                                if rand == 0:
                                    gen.append(random.choice(_chars.lower()))
                                elif rand == 1:
                                    gen.append(random.choice(_chars))
                                else:
                                    gen.append(random.choice(_symbols))
                                    
                            elif (useSymbols == "No" and useNumbers == "No"):
                                rand = random.randrange(2)
                                if rand == 0:
                                    gen.append(random.choice(_chars.lower()))
                                elif rand == 1:
                                    gen.append(random.choice(_chars))
                                
                    passwords.append(f''.join(str(i) for i in gen))
                    passwordAmount -= 1
                
                for x in passwords:
                    num += 1
                    print(f'[{str(num)}] ' + x)
                
                def askForChoice(amount, passwords):
                    global _accPassword
                    try:
                        os.system('cls')
                        print("""================================
    PASSWORD GENERATOR
================================\n""")
                        print(f"\n> Amount of passwords: {amount}")
                        print(f"> Password length [8-256]: {passwordLength}\n")
 
                        num = 0
                        for x in passwords:
                            num += 1
                            print(f'[{str(num)}] ' + x)

                        choice = int(input(f"\nChoose password [{1}-{num}]: "))
                        _accPassword = passwords[choice-1]
                    except:
                        input("\nValue must be intiger!")
                        askForChoice(amount, passwords)
                    return _accPassword
                
                _accPassword = askForChoice(passwordAmount, passwords)
                os.system('cls')
                print("""================================
         PASSWORD MANAGER
================================\n""")
                print(f"""Account name: {_accName}
Login: {_accLogin}
Password: {_accPassword}""")
        
            def getAmount():
                global passwordAmount
                os.system('cls')
                print("""================================
       PASSWORD GENERATOR
================================\n""")
                passwordAmount = int(input("\n> Amount of passwords: "))
                def getInput():
                    try:
                        os.system('cls')
                        print("""================================
       PASSWORD GENERATOR
================================\n""")
                        print(f"\n> Amount of passwords: {passwordAmount}")
                        
                        passwordLength = int(input("> Password length [8-256]: "))
                        if passwordLength < 8:
                            input("\nYour password must be at least 8 characters long!")
                            getInput()
                        elif passwordLength > 256:
                            input("\nMax password length is 256!")
                            getInput()
                        else:
                            
                            # Password settings
                            def getPasswordSettingUsingSymbols():
                                os.system('cls')
                                print("================================")
                                print("       PASSWORD GENERATOR")
                                print("================================\n")
                                print(f"> Password amount: {passwordAmount}")
                                print(f"> Password length [8-256]: {passwordLength}")
                                
                                useSymbols = str(input(f"> Use symbols {_symbols} [Yes/No]: "))
                                
                                if(useSymbols == "Yes" or useSymbols == "yes" or useSymbols == "1"):
                                    useSymbols = "Yes"
                                elif(useSymbols == "No" or useSymbols == "no" or useSymbols == "0"):
                                    useSymbols = "No"
                                else:
                                    input("\nWrong input!")
                                    getPasswordSettingUsingSymbols()
                                
                                def getPasswordSettingUsingNumbers():
                                    os.system('cls')
                                    print("================================")
                                    print("       PASSWORD GENERATOR")
                                    print("================================\n")
                                    print(f"> Password amount: {passwordAmount}")
                                    print(f"> Password length: {passwordLength}")
                                    print(f"> Use symbols {_symbols} [Yes/No]: {useSymbols}")
                                    
                                    useNumbers = str(input(f"> Use numbers {_numbers} [Yes/No]: "))
                                    
                                    if(useNumbers == "Yes" or useNumbers == "yes" or useNumbers == "1"):
                                        useNumbers = "Yes"
                                    elif(useNumbers == "No" or useNumbers == "no" or useNumbers == "0"):
                                        useNumbers = "No"
                                    else:
                                        input("\nWrong input!")
                                        getPasswordSettingUsingNumbers()
                                        
                                    # Calling function to generate password with following variables
                                    genPassword(passwordAmount, passwordLength, useSymbols, useNumbers)
                                getPasswordSettingUsingNumbers()
                            getPasswordSettingUsingSymbols()
                    except ValueError:
                        input("\nValue must be intiger!")
                        getInput()
                getInput()
            getAmount()
        elif passGen == "no" or passGen == "n" or passGen == "0":
            os.system('cls')
            print("""================================
        PASSWORD MANAGER
================================\n""")
            print(f"Account name: {_accName}")
            print(f"Login: {_accLogin}")
            global _accPassword
            _accPassword = input("Password: ")
        else:
            os.system('cls')
            print("""================================
        PASSWORD MANAGER
================================\n""")
            print(f"Account name: {_accName}")
            print(f"Login: {_accLogin}")
            print("\nTo accept type: 'Yes'/'yes'/'Y'/'y'/'1'\nTo deny type: 'No'/'no'/'N'/'n'/'0'")
            ask(_accName, _accLogin)
    ask(_accName, _accLogin)

    _accMail = input("e-mail: ")
    _accUrl = input("Url: ")
    _accDescription = input("Description: ")

    print("\nSaving acount details...")

    f = open("accounts.txt", "a")
    f.write(f"""==============================================
    Account name: {_accName}
    Login: {_accLogin}
    Password: {_accPassword}
    E-mail: {_accMail}
    Url: {_accUrl}
    Description: {_accDescription}\n\n""")
    f.close()

    print("Account saved!")

createAccount()