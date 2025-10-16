import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import urllib.request

def set_window_icon(root: tk.Tk, icon_name="uwu.png"):
    """
    Use a local PNG (uwu.png) as the window/icon image.
    Place uwu.png next to this script.
    Keeps a reference on root to avoid GC.
    """
    base = Path(__file__).with_name(icon_name)
    if not base.exists():
        return
    try:
        img = tk.PhotoImage(file=str(base))
        root._uwu_icon = img
        root.iconphoto(True, img)
    except Exception:
        
        pass

class FileRenamerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer")
        set_window_icon(self.root, "uwu.png")
        # state variables
        self.csv_path = tk.StringVar()
        self.directory_path = tk.StringVar()
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # CSV File Selection
        tk.Label(self.root, text="CSV File:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.csv_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_csv).grid(row=0, column=2, padx=5, pady=5)
        
        # Directory Selection
        tk.Label(self.root, text="Directory:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.directory_path, width=50).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_directory).grid(row=1, column=2, padx=5, pady=5)
        
        # Status Text
        self.status_text = tk.Text(self.root, height=15, width=70)
        self.status_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        
        # Rename Button
        tk.Button(self.root, text="Rename Files", command=self.rename_files).grid(row=3, column=1, pady=20)

    def browse_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filename:
            self.csv_path.set(filename)
    
    def browse_directory(self):
        dirname = filedialog.askdirectory()
        if dirname:
            self.directory_path.set(dirname)
    
    def log_message(self, message):
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
    
    def rename_files(self):
        csv_path = self.csv_path.get()
        directory_path = self.directory_path.get()
        
        if not csv_path or not directory_path:
            messagebox.showerror("Error", "Please select both CSV file and directory")
            return
        
        try:
            self.status_text.delete(1.0, tk.END)
            self.log_message("Starting file renaming process...")
            
            with open(csv_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                if not {'OldFileName', 'NewFileName'}.issubset(csv_reader.fieldnames):
                    self.log_message("Error: CSV must have 'OldFileName' and 'NewFileName' columns")
                    return
                
                for row in csv_reader:
                    old_path = Path(directory_path) / row['OldFileName']
                    new_path = Path(directory_path) / row['NewFileName']
                    
                    if old_path.exists():
                        try:
                            old_path.rename(new_path)
                            self.log_message(f"Renamed: {row['OldFileName']} -> {row['NewFileName']}")
                        except Exception as e:
                            self.log_message(f"Error renaming {row['OldFileName']}: {str(e)}")
                    else:
                        self.log_message(f"File not found: {row['OldFileName']}")
            
            self.log_message("\nFile renaming completed!")
            
        except Exception as e:
            self.log_message(f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = FileRenamerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()