error = False
try:
    import os
    from os import system
    system("title " + "Roblox Fee Calculator,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
    import python_percentage
except:
    error = True
if error == True:
    while True:
        fix = input("Missing Module, Wanna Try Auto Fix (y/n): ")
        if fix == "y" or fix == "n":
            break
        else:
            print("Enter A Valid Choice")
    if fix == "n":
        exit()
    if fix == "y":
        try:
            import os
            os.system("pip install python-percentage")
            print("Problem May Be Fixed Now, Restart Prgoram")
            input("")
            exit()
        except:
            print("Error Fixing Error")
            input("")
            exit()
def calc():
    while True:
        while True:
            try:
                e = input("Enter Amount Of Robux: ")
                e = float(e)
                break
            except:
                print("Enter A Valid Choice")
        r =  python_percentage.get_percentage(30.0, e)
        print("Fee: " + str(r))
        print("")
        h = float(e) - r
        print("Owner Will Get: " + str(h))
        print("")
        j = float(e) + float(r)
        print("If Want No Fee Need Pay: " +  str(j))
        input("")
        clear()
def clear():
    try:
        import os
        os.system("cls")
    except:
        pass
calc()
