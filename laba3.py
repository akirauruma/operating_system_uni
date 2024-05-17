import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")

        self.textBox1 = tk.Entry(root, width=50)
        self.textBox1.grid(row=0, column=1, padx=10, pady=5)
        self.textBox2 = tk.Entry(root, width=50)
        self.textBox2.grid(row=1, column=1, padx=10, pady=5)
        self.textBox3 = tk.Entry(root, width=50)
        self.textBox3.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Source Path").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Destination Path").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Rename to").grid(row=2, column=0, padx=10, pady=5)

        tk.Button(root, text="Select Source File", command=self.button_file_1_click).grid(row=0, column=2, padx=10,
                                                                                          pady=5)
        tk.Button(root, text="Select Destination File", command=self.button_file_2_click).grid(row=1, column=2, padx=10,
                                                                                               pady=5)
        tk.Button(root, text="Select Source Folder", command=self.button_folder_1_click).grid(row=0, column=3, padx=10,
                                                                                              pady=5)
        tk.Button(root, text="Select Destination Folder", command=self.button_folder_2_click).grid(row=1, column=3,
                                                                                                   padx=10, pady=5)

        tk.Button(root, text="Copy", command=self.button_copy_click).grid(row=3, column=0, padx=10, pady=5)
        tk.Button(root, text="Move to", command=self.button_move_click).grid(row=3, column=1, padx=10, pady=5)
        tk.Button(root, text="Delete", command=self.button_delete_click).grid(row=3, column=2, padx=10, pady=5)
        tk.Button(root, text="Rename", command=self.button_rename_click).grid(row=3, column=3, padx=10, pady=5)
        tk.Button(root, text="Switch Paths", command=self.button_exchange_click).grid(row=4, column=1, padx=10, pady=5)

    def button_copy_click(self):
        try:
            if self.is_file(self.textBox1.get()):
                file_path_src = self.textBox1.get()
                file_name = os.path.basename(file_path_src)
                file_path_dest = os.path.join(self.textBox2.get(), file_name)
                shutil.copy2(file_path_src, file_path_dest)
            else:
                dir_src = self.textBox1.get()
                dir_dest = os.path.join(self.textBox2.get(), os.path.basename(self.textBox1.get()))
                self.copy_dir_recursive(dir_src, dir_dest)
        except Exception as ex:
            self.wrong()

    def copy_dir_recursive(self, source, target):
        if os.path.abspath(source).lower() == os.path.abspath(target).lower():
            return
        if not os.path.exists(target):
            os.makedirs(target)
        for item in os.listdir(source):
            s = os.path.join(source, item)
            d = os.path.join(target, item)
            if os.path.isdir(s):
                self.copy_dir_recursive(s, d)
            else:
                shutil.copy2(s, d)

    def button_move_click(self):
        try:
            file_path_src = self.textBox1.get()
            if self.is_file(file_path_src):
                file_name = os.path.basename(file_path_src)
                file_path_dest = os.path.join(self.textBox2.get(), file_name)
                shutil.move(file_path_src, file_path_dest)
            else:
                dir_src = self.textBox1.get()
                dir_dest = os.path.join(self.textBox2.get(), os.path.basename(self.textBox1.get()))
                self.copy_dir_recursive(dir_src, dir_dest)
                shutil.rmtree(dir_src)
        except Exception as ex:
            self.wrong()

    def button_delete_click(self):
        try:
            path = self.textBox1.get()
            if self.is_file(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
        except:
            self.wrong()

    def button_rename_click(self):
        try:
            file_path_src = self.textBox1.get()
            if self.is_file(file_path_src):
                dir_name = os.path.dirname(file_path_src)
                new_file_name = os.path.basename(self.textBox3.get())
                file_path_dest = os.path.join(dir_name, new_file_name)
                shutil.move(file_path_src, file_path_dest)
            else:
                dir_name = os.path.dirname(file_path_src)
                new_dir_name = self.textBox3.get()
                new_dir_dest = os.path.join(dir_name, new_dir_name)
                shutil.move(file_path_src, new_dir_dest)
        except Exception as ex:
            self.wrong()

    def button_file_1_click(self):
        file_path = filedialog.askopenfilename(initialdir=self.textBox1.get())
        if file_path:
            self.textBox1.delete(0, tk.END)
            self.textBox1.insert(0, file_path)

    def button_file_2_click(self):
        file_path = filedialog.askopenfilename(initialdir=self.textBox2.get())
        if file_path:
            self.textBox2.delete(0, tk.END)
            self.textBox2.insert(0, file_path)

    def button_folder_1_click(self):
        folder_path = filedialog.askdirectory(initialdir=self.textBox1.get())
        if folder_path:
            self.textBox1.delete(0, tk.END)
            self.textBox1.insert(0, folder_path)

    def button_folder_2_click(self):
        folder_path = filedialog.askdirectory(initialdir=self.textBox2.get())
        if folder_path:
            self.textBox2.delete(0, tk.END)
            self.textBox2.insert(0, folder_path)

    def button_exchange_click(self):
        temp = self.textBox1.get()
        self.textBox1.delete(0, tk.END)
        self.textBox1.insert(0, self.textBox2.get())
        self.textBox2.delete(0, tk.END)
        self.textBox2.insert(0, temp)

    def is_file(self, path):
        return os.path.isfile(path)

    def wrong(self):
        messagebox.showerror("Attention!", "Invalid sequence of actions")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
