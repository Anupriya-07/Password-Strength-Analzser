from zxcvbn import zxcvbn

password = input("Enter a password to check: ")
result = zxcvbn(password)
print(f"Password score (0 to 4): {result['score']}")
print("Feedback:", result['feedback'])
print("Estimated time to crack (offline fast hash):", result['crack_times_display']['offline_fast_hashing_1e10_per_second'])
def generate_wordlist(info_dict):
    # Simple combinations
    base_words = [
        info_dict['name'],
        info_dict['pet'],
        info_dict['name'] + info_dict['year'],
        info_dict['pet'] + info_dict['year'],
        info_dict['name'][::-1],
    ]
    # Leetspeak replacements
    leet = lambda w: w.replace('a', '@').replace('e', '3').replace('i', '1').replace('o', '0')
    base_words += [leet(word) for word in base_words]
    return list(set(base_words)) # remove duplicates

user_info = {
    'name': input("Enter your name: "),
    'pet': input("Enter your pet's name: "),
    'year': input("Enter a special year (e.g., birth): "),
}
wordlist = generate_wordlist(user_info)
with open('custom_wordlist.txt', 'w') as f:
    for word in wordlist:
        f.write(word + '
')
print("Wordlist created as custom_wordlist.txt")
:import tkinter as tk
from zxcvbn import zxcvbn

def check_password():
    pwd = entry.get()
    res = zxcvbn(pwd)
    result_label.config(text=f"Score: {res['score']}
{res['feedback']['suggestions']}")

root = tk.Tk()
root.title("Password Strength Analyzer")
entry = tk.Entry(root, show="*")
entry.pack()
tk.Button(root, text="Check Strength", command=check_password).pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
