def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def caesar_tool():   # ✅ THIS MUST EXIST
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))

    print("1. Encrypt\n2. Decrypt")
    choice = input("Choose: ")

    if choice == '1':
        print("Encrypted:", encrypt(text, shift))
    else:
        print("Decrypted:", decrypt(text, shift))
 
