import tkinter as tk
import pyshorteners

def shorten_url():
    original_url = entry.get()
    if original_url:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(original_url)
        shortened_url_label.config(text=f"Shortened URL: {shortened_url}")
    else:
        shortened_url_label.config(text="Please enter a valid URL.")

root = tk.Tk()
root.title("URL Shortener")
label = tk.Label(root, text="Enter the URL to shorten:")
label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
shorten_button = tk.Button(root, text="Shorten", command=shorten_url)
shorten_button.pack(pady=5)
shortened_url_label = tk.Label(root, text="")
shortened_url_label.pack(pady=10)
root.mainloop()