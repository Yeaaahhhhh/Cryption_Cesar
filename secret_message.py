import tkinter as tk
import random
import string

# Encryption function
def encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        shift = ord(key_char)
        encrypted_char = chr((ord(char) + shift) % 256)
        encrypted_text += encrypted_char
    return encrypted_text

# Decryption function
def decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        shift = ord(key_char)
        decrypted_char = chr((ord(char) - shift) % 256)
        decrypted_text += decrypted_char
    return decrypted_text

# Generate random key
def generate_key():
    key_length = random.randint(18, 30)
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=key_length))
    key_entry.delete(0, tk.END)
    key_entry.insert(tk.END, key)

# Encrypt message
def encrypt_message():
    plaintext = message_entry.get("1.0", tk.END).strip()
    key = key_entry.get()
    encrypted_text = encrypt(plaintext, key)
    encrypted_message_entry.delete("1.0", tk.END)
    encrypted_message_entry.insert(tk.END, encrypted_text)

# Decrypt message
def decrypt_message():
    encrypted_text = encrypted_message_entry.get("1.0", tk.END).strip()
    key = shared_key_entry.get()
    decrypted_text = decrypt(encrypted_text, key)
    decrypted_message_entry.delete("1.0", tk.END)
    decrypted_message_entry.insert(tk.END, decrypted_text)

# Create main window
root = tk.Tk()
root.title("Message Encryptor/Decryptor")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create input fields, labels, and buttons
message_label = tk.Label(root, text="Input your message here:")
message_entry = tk.Text(root, width=50, height=10, wrap=tk.WORD)
message_scrollbar = tk.Scrollbar(root, command=message_entry.yview)
message_entry.config(yscrollcommand=message_scrollbar.set)

key_label = tk.Label(root, text="Generate a key here:")
key_entry = tk.Entry(root, width=50)
generate_key_button = tk.Button(root, text="Generate Key", command=generate_key)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)

encrypted_message_label = tk.Label(root, text="Encrypted message/Or copy the encrypted message here:")
encrypted_message_entry = tk.Text(root, width=50, height=10, wrap=tk.WORD)
encrypted_message_scrollbar = tk.Scrollbar(root, command=encrypted_message_entry.yview)
encrypted_message_entry.config(yscrollcommand=encrypted_message_scrollbar.set)

shared_key_label = tk.Label(root, text="Copy/Input your key here:")
shared_key_entry = tk.Entry(root, width=50)

decrypt_button = tk.Button(root, text="Translate", command=decrypt_message)

decrypted_message_label = tk.Label(root, text="Your Decrypted message:")
decrypted_message_entry = tk.Text(root, width=50, height=10, wrap=tk.WORD)
decrypted_message_scrollbar = tk.Scrollbar(root, command=decrypted_message_entry.yview)
decrypted_message_entry.config(yscrollcommand=decrypted_message_scrollbar.set)

# Place widgets on the main window
message_label.grid(row=0, column=0, sticky=tk.W)
message_entry.grid(row=1, column=0, sticky=(tk.W, tk.E))
message_scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))

key_label.grid(row=2, column=0, sticky=tk.W)
key_entry.grid(row=3, column=0, sticky=(tk.W, tk.E))
generate_key_button.grid(row=3, column=1, sticky=(tk.W, tk.E))

encrypt_button.grid(row=1, column=2, sticky=(tk.W, tk.E))

encrypted_message_label.grid(row=4, column=0, sticky=tk.W)
encrypted_message_entry.grid(row=5, column=0, sticky=(tk.W, tk.E))
encrypted_message_scrollbar.grid(row=5, column=1, sticky=(tk.N, tk.S))

shared_key_label.grid(row=6, column=0, sticky=tk.W)
shared_key_entry.grid(row=7, column=0, sticky=(tk.W, tk.E))

decrypt_button.grid(row=7, column=1, sticky=(tk.W, tk.E))

decrypted_message_label.grid(row=8, column=0, sticky=tk.W)
decrypted_message_entry.grid(row=9, column=0, sticky=(tk.W, tk.E))
decrypted_message_scrollbar.grid(row=9, column=1, sticky=(tk.N, tk.S))

# Configure columns and rows for resizing behavior
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
for i in range(10):
    root.rowconfigure(i, weight=1)

# Run main loop
root.mainloop()