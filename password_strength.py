# Password Strength Analyzer with Custom Wordlist Generator

from zxcvbn import zxcvbn

# --- Password Strength Analyzer ---

def check_password_strength():
    password = input("Enter a password to check: ")
    result = zxcvbn(password)
    print(f"\nPassword score (0-4): {result['score']}")
    print("Feedback:", result['feedback'])
    print("Estimated time to crack (offline fast hash):", result['crack_times_display']['offline_fast_hashing_1e10_per_second'])

# --- Custom Wordlist Generator ---

def leetspeak(word):
    # Simple leetspeak replacements
    substitutions = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7'],
        'l': ['1']
    }
    variants = {word}
    for idx, char in enumerate(word.lower()):
        if char in substitutions:
            for sub in substitutions[char]:
                variant = word[:idx] + sub + word[idx+1:]
                variants.add(variant)
    return list(variants)

def generate_wordlist(info_dict):
    words = set()
    # Basic combinations
    base_words = [
        info_dict['name'],
        info_dict['pet'],
        info_dict['color'],
        info_dict['year'],
        info_dict['name'] + info_dict['year'],
        info_dict['pet'] + info_dict['year'],
        info_dict['name'][::-1],  # reversed name
        info_dict['pet'][::-1]    # reversed pet name
    ]
    for word in base_words:
        words.add(word)
        words.update(leetspeak(word))
    return list(words)

def save_wordlist(wordlist, filename="custom_wordlist.txt"):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    print(f"Wordlist saved to {filename}")

def main():
    print("--- Password Strength Analyzer ---")
    check_password_strength()
    print("\n--- Custom Wordlist Generator ---")
    user_info = {
        'name': input("Enter your name: "),
        'pet': input("Enter your pet's name: "),
        'color': input("Enter your favourite color: "),
        'year': input("Enter a special year (e.g., birth year): ")
    }
    wordlist = generate_wordlist(user_info)
    save_wordlist(wordlist)
    print("\nProject completed successfully!")

if __name__ == "__main__":
    main()

import tkinter as tk
from zxcvbn import zxcvbn

def check_password():
    pwd = entry.get()
    res = zxcvbn(pwd)
    result_label.config(text=f"Score: {res['score']}\n{res['feedback']['suggestions']}")

root = tk.Tk()
root.title("Password Strength Analyzer")
entry = tk.Entry(root, show="*")
entry.pack()
tk.Button(root, text="Check Strength", command=check_password).pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()

