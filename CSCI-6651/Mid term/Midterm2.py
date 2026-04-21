def sort_key(item):
    char, count =item
    return (-count, ord(char))

def main():
    text = input("Enter a string: ").lower()

    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) +1
        
    freq_list = [[char, count] for char, count in freq.items()]

    freq_list.sort(key=sort_key)

    print(f"Input String: {text}")
    for char, count in  freq_list:
        display_char = "Space" if char == " " else char
        print(f"{display_char} count: {count}")

if __name__ == "__main__":
    main()