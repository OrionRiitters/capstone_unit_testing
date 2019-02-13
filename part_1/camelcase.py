def promptUser():
    userInput = input('Please type in a sentence!\n')
    return userInput

def camelCaseify(string):
    camelCased = ''
    string = string.lower()
    splitString = string.split(' ')
    charSwitch = False

    for s in splitString:
        newString = ''
        for chr in s:
            if charSwitch == True:
                newString += chr.capitalize()
                charSwitch = False
            else:
                newString += chr.lower()
        camelCased += newString
        charSwitch = True

    return camelCased

def main():
    userInput = promptUser()
    camelCaseify(userInput)

if __name__ == '__main__':
    main()
