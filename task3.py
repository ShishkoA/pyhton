listofphrase = []

def phrases():
    while True:
        try:
            phrase = input("Enter your phrase: ")
            if phrase == "stopped":
                break
            else:
                listofphrase.append(phrase)

        except Exception as e:
            print(e)


phrases()