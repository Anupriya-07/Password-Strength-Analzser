import tkinter as tk
from zxcvbn import zxcvbn

# Wordlist generator functions
def leetspeak(word):
    substitutions = {'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['5', '$'], 't': ['7'], 'l': ['1']}
    variants = {word}
    for idx, char in enumerate(word.lower()):
        if char in substitutions:
            for sub in substitutions[char]:
                variant = word[:idx] + sub + word[idx+1:]
                variants.add(variant)
    return list(variants)

def generate_wordlist(info_dict):
    words = set()
    base_words = [
        info_dict['name'],
        info_dict['pet'],
        info_dict['color'],
        info_dict['year'],
        info_dict['name'] + info_dict['year'],
        info_dict['pet'] + info_dict['year'],
        info_dict['name'][::-1],
        info_dict['pet'][::-1]
    ]
    for word in base_words:
        words.add(word)
        words.update(leetspeak(word))
    return list(words)

def save_wordlist(wordlist):
    with open('custom_wordlist.txt', 'w') as f:
        for word in wordlist:
            f.write(word + '\n')

# Tkinter GUI
def check_password():
    pwd = password_entry.get()
    result = zxcvbn(pwd)
    feedback = "\n".join(result['feedback']['suggestions']) if result['feedback']['suggestions'] else "No suggestions"
    result_label.config(text=f"Score: {result['score']}\n{feedback}")

def create_wordlist():
    info_dict = {
        'name': name_entry.get(),
        'pet': pet_entry.get(),
        'color': color_entry.get(),
        'year': year_entry.get()
    }
    wordlist = generate_wordlist(info_dict)
    save_wordlist(wordlist)
    wordlist_label.config(text="Wordlist saved to custom_wordlist.txt")

root = tk.Tk()
root.title("Password Tool")
root.geometry("400x400")

# Password strength section
tk.Label(root, text="Enter password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
tk.Button(root, text="Check Strength", command=check_password).pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Wordlist generator section
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Pet Name:").pack()
pet_entry = tk.Entry(root)
pet_entry.pack()
tk.Label(root, text="Favorite Color:").pack()
color_entry = tk.Entry(root)
color_entry.pack()
tk.Label(root, text="Special Year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()
tk.Button(root, text="Generate Wordlist", command=create_wordlist).pack(pady=5)
wordlist_label = tk.Label(root, text="")
wordlist_label.pack(pady=5)

root.mainloop()


