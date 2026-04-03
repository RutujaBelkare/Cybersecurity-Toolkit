from caesar_cipher import caesar_tool
from image_encrypt import image_tool
from password_checker import check_password
from keylogger import start_keylogger
from packet_sniffer import start_sniffer

def main():
    while True:
        print("\n=== Cyber Security Toolkit ===")
        print("1. Caesar Cipher")
        print("2. Image Encryption")
        print("3. Password Checker")
        print("4. Keylogger")
        print("5. Packet Sniffer")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            caesar_tool()
        elif choice == '2':
            image_tool()
        elif choice == '3':
            pwd = input("Enter password: ")
            check_password(pwd)
        elif choice == '4':
            start_keylogger()
        elif choice == '5':
            start_sniffer()
        elif choice == '6':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
