cipher_text = "L#dp#kdylqj#d#juhdw#wlph#lq#FVFL/9984$##Surihvvru#Dqwrqhwwl#lv#d#Frrs#Ndw$"

def freq_analysis(cipher_text):
    # Creating frequency analysis dictionary
    frequency_analysis = {}

    for char in cipher_text:
        if char != " ": #To ignore blank spaces
            if char in frequency_analysis:
                frequency_analysis[char] = frequency_analysis[char]+1
            else:
                frequency_analysis[char] = 1

    #Converting frequency dictionary to list of tuples
    frequency_list = []
    for c in frequency_analysis:
        frequency_list.append((c , frequency_analysis[c])) #Appending tuples of (character, count) to the freuency list

    print("Sorted Frequency Analysis tuple: ", sorted(frequency_list))

    return sorted(frequency_list)

#Function to decrypt the text using ceaser cipher 
def ceaser_cipher(s, shift):
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    out = []
    for c in s:
        if c.islower():
            out.append(lower[(lower.index(c) - shift) % 26])
        elif c.isupper():
            out.append(upper[(upper.index(c) - shift) % 26])
        else:
            out.append(c)
    return ''.join(out)

common_words = {"the","and","is","a","in","of","to","for","on","it","i","am","having","great","time","professor","co-op","coop","cooper","isn't","are","this","that","with","as","an","by","we","you","he","she","they"}

#Simple scoring: count how many common words appear in the text.
def score_candidate(s):
    low = s.lower()
   
    separators = "#/$,.!?;:()-0123456789" # replacing common delimiters with spaces for easier splitting
    for ch in separators:
        low = low.replace(ch, " ")
    tokens = [t for t in low.split() if t]
    score = 0
    for t in tokens:
        if t in common_words:
            score += 2
        if len(t) > 2 and t.isalpha():
            score += 0.2
    return score, tokens

#Brute Forcing to find the best possible output
def brute_force(s):
    results = []
    for shift in range(26):
        cand = ceaser_cipher(s, shift)
        score, tokens = score_candidate(cand)
        results.append((score, shift, cand, tokens))
        results = sorted(results)
    return results

def main():
    print("Ciphertext:")
    print(cipher_text)

    freq = freq_analysis(cipher_text)
    print(freq)
    
    print("Caesar Cipher shifts:")
    for shift in range(26):
        print("Shift", shift, ":", ceaser_cipher(cipher_text, shift))

    print("Brute-Force the ceasar cipher output:")
    results = brute_force(cipher_text)
    best = []
    for score, shift, cand, tokens in results[:20:-1]:
        print(f"\nShift = {shift}  (score={score:.2f})")
        print(cand)

    r_len = len(results)-1
    best_decrypt=results[r_len]
    print("\nThe best possible decryption of the cipher text will be:")
    print(best_decrypt[2])

if __name__ == "__main__":
    main()