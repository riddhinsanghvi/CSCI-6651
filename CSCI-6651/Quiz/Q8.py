def display_options():
    print("1. Input the Key Dictionary")
    print("2. View the Key Dictionary")
    print("3. Modify the Key Dictionary")
    print("4. Specify the File to Encrypt")
    print("5. Encrypt the File creating a new file with the original file name ")
    print("6. Quit")

def input_key_dictionary():
    print("Enter key mappings, in the form plaintext:cipher")
    print("Enter an empty line when finished.")
    k_d = {}
    while True:
        line = input("mapping> ").strip()
        if line == "":
            break
        if ':' not in line:
            print("Invalid format. Use plaintext:cipher (single characters).")
            continue
        left, right = line.split(':', 1)
        if len(left) != 1 or len(right) != 1:
            print("Both plaintext and cipher must be exactly ONE character.")
            continue
        p, c = left, right
        if c in k_d.values():
            # Prevent duplicate cipher values to keep a simple 1-to-1 map
            print(f"Cipher character '{c}' is already used. Choose a different cipher char.")
            continue
        k_d[p] = c
        print(f"Added mapping: '{p}' -> '{c}'")
    return k_d

def view_key_dictionary(k_d):
    if not k_d:
        print("(Key dictionary is empty)")
        return
    print("Key Dictionary (plaintext -> ciphertext):")
    for k in sorted(k_d.keys()):
        print(f"  '{k}' -> '{k_d[k]}'")
        print()

def modify_key_dictionary(key_dict):
    print("Modify Key dictionary")
    ch = input("Enter the character to modify: ")
    if ch in key_dict: 
        new_value = input(f"Enter the new value for the charcater {ch}: ")
        if len(new_value) ==1:
            key_dict[ch] = new_value
            print("Modified Successfully!!")
        else:
            print("Value must be one character!!")
    else:
        print(f"{ch} not found in the dictionary")

def file_encryption(file_name, key_dict):
    try:
        with open(file_name, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("File not Found")
        return

    encrypt = ""
    for ch in text:
        encrypt += key_dict.get(ch, ch)

    new_file = file_name.replace(".txt", "-ENCRYPTED.txt")
    with open(new_file,'w') as f:
        f.write(encrypt)
    print(f"Encryption Successful in the file with name {new_file}")

def main():
    key_dict = {}

    while True:
        display_options()
        choice = input("Choose option (1-6): ")
        if choice == '1':
            key_dict = input_key_dictionary()
        elif choice == '2':
            print("View Key Dictionary")
            view_key_dictionary(key_dict)

        elif choice =='3':
            modify_key_dictionary(key_dict)

        elif choice == '4':
            file_name = input("Enter the file name that you want to encrypt: ")
            print(file_name)

        elif choice == '5':
            file_encryption(file_name, key_dict)

        elif choice == '6':
            print("Quitting. Goodbye.")
            break


if __name__ == "__main__":
    main()