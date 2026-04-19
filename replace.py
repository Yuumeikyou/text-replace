import tkinter as tk
from tkinter import filedialog, messagebox

def process_file():
    # getting words from user input in text fields
    old_text = entry_old.get()
    new_text = entry_new.get()
    
    if not old_text:
        messagebox.showerror("Error", "Input sentence or word to searh in original file")
        return

    # choosing original text file
    input_path = filedialog.askopenfilename(
        title="Choose original text file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not input_path:
        return

    # choosing where to save file
    output_path = filedialog.asksaveasfilename(
        title="Save result as",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not output_path:
        return

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
            new_content = content.replace(old_text, new_text)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        messagebox.showinfo("Done", f"Replace finished.\nResult saved in:\n{output_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Cannot process file:\n{e}")

# creating a main menu
root = tk.Tk()
root.title("Text file replace")
root.geometry("500x250")
root.resizable(False, False)

# original string text field
tk.Label(root, text="Input original string:", font=("Arial", 14)).pack(pady=(20, 0))
entry_old = tk.Entry(root, width=40, font=("Arial", 14))
entry_old.pack(pady=5)

# text field for new replace string
tk.Label(root, text="Input replace string:", font=("Arial", 14)).pack(pady=(10, 0))
entry_new = tk.Entry(root, width=40, font=("Arial", 14))
entry_new.pack(pady=5)

# start button
btn_process = tk.Button(root, text="Go to file selection", 
                        command=process_file, font=("Arial", 14), bg="#4CAF50", fg="black")
btn_process.pack(pady=12)

root.mainloop()