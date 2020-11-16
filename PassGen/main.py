import random
import pyperclip


def generatePassword(chars, charList):
    password = []
    for i in range(chars):
        nextChar = characterList[random.randint(0, len(charList))]
        password.append(nextChar)
    return ''.join(password)


def copyToClipBoard(copy):
    pyperclip.copy(copy)


if __name__ == "__main__":
    characterList = "ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+1234567890"
    lengthToGenerate = int(input("Length: "))
    copyToClipBoard(generatePassword(lengthToGenerate, characterList))
    print('Copied To Clipboard!')
