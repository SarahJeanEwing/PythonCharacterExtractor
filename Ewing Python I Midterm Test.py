#Sarah Ewing
#Python I Midterm Test
#10/11/2021

import tkinter as tk
from tkinter import ttk
import re

class PriceFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self,parent, padding="30 10 30 30")
        self.pack(fill=tk.BOTH, expand=True)

        self.textEntry = tk.StringVar()
        self.result = tk.StringVar()
        self.result.set("-")

        self.initComponents()

    def initComponents(self):
        self.pack()
        
        ttk.Label(self, text="Character Extractor").pack()
        ttk.Entry(self, width=25, textvariable=self.textEntry).pack()

        ttk.Label(self, textvariable=self.result).pack()

        ttk.Button(self, text="Extract Vowels", command=self.extractVowels).pack()

        ttk.Button(self, text="Extract Consonants", command=self.extractConsonants).pack()

    def extractVowels(self):
        output = ""
        result = re.findall(r'[^aeiou]', self.textEntry.get(), re.IGNORECASE)
        for letter in result:
            output += letter
        self.result.set(output)

    def extractConsonants(self):
        output = ""
        result = re.findall(r'[^bcdfghjklmnpqrstvwxyz]', self.textEntry.get(), re.IGNORECASE)
        for letter in result:
            output += letter
        self.result.set(output)


if __name__ == "__main__":
    root = tk.Tk()
    PriceFrame(root)
    root.mainloop()




