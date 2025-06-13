import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from backend import PasswordEvaluator
from backend import PasswordGenerator
from PIL import Image, ImageTk
import os

class EntropyXApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EntropyX – Password Strength Checker & Generator")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        icon_img = ImageTk.PhotoImage(file=os.path.join("assets", "favicon.png"))
        self.root.iconphoto(False, icon_img)
        self._load_logo()
        self._set_icon()

        self._build_password_checker_ui()
        self._build_password_generator_ui()

    def _set_icon(self):
        try:
            icon_path = os.path.join("assets", "favicon.png")
            self.icon_img = ImageTk.PhotoImage(file=icon_path)
            self.root.iconphoto(False, self.icon_img)
        except Exception as e:
            print(f"Could not set favicon: {e}")


    def _load_logo(self):
        logo_path = os.path.join("assets", "logo.png")
        try:
            image = Image.open(logo_path)
            image = image.resize((400, 90), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(image)  # Store as instance variable

            logo_label = tk.Label(self.root, image=self.logo_img, bg=self.root.cget("bg"))
            logo_label.pack(pady=(10, 0))

        except Exception as e:
            print(f"Could not load logo: {e}")


    def _build_password_checker_ui(self):
        frame = ttk.Labelframe(self.root, text="🔍 Password Strength Checker", padding=10)
        frame.pack(padx=10, pady=10, fill="x")

        entry_frame = ttk.Frame(frame)
        entry_frame.pack(pady=5)

        self.pwd_var = tk.StringVar()
        self.pwd_entry = ttk.Entry(entry_frame, textvariable=self.pwd_var, width=45, show="*")
        self.pwd_entry.grid(row=0, column=0)

        self.show_pwd = False
        self.eye_btn = ttk.Button(entry_frame, text="👁️", width=3, command=self.toggle_password_visibility)
        self.eye_btn.grid(row=0, column=1, padx=5)

        check_btn = ttk.Button(frame, text="Check Strength", command=self.check_password_strength)
        check_btn.pack(pady=5)

        self.score_label = ttk.Label(frame, text="", font=("Arial", 10, "bold"))
        self.score_label.pack(pady=5)

        self.feedback_box = scrolledtext.ScrolledText(frame, height=7, width=80, wrap=tk.WORD, font=("Segoe UI", 9))
        self.feedback_box.pack()
        self.feedback_box.tag_configure("warn", foreground="red")

    def toggle_password_visibility(self):
        self.show_pwd = not self.show_pwd
        self.pwd_entry.config(show="" if self.show_pwd else "*")
        self.eye_btn.config(text="🙈" if self.show_pwd else "👁️")

    def _build_password_generator_ui(self):
        frame = ttk.Labelframe(self.root, text="🔐 Password Generator", padding=10)
        frame.pack(padx=10, pady=10, fill="x")

        options = ttk.Frame(frame)
        options.pack(pady=5)

        self.length_var = tk.IntVar(value=16)
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        ttk.Label(options, text="Length:").grid(row=0, column=0, padx=5)
        ttk.Spinbox(options, from_=4, to=64, textvariable=self.length_var, width=5).grid(row=0, column=1)

        ttk.Checkbutton(options, text="Uppercase", variable=self.upper_var).grid(row=1, column=0, sticky="w", padx=5)
        ttk.Checkbutton(options, text="Lowercase", variable=self.lower_var).grid(row=1, column=1, sticky="w", padx=5)
        ttk.Checkbutton(options, text="Digits", variable=self.digits_var).grid(row=2, column=0, sticky="w", padx=5)
        ttk.Checkbutton(options, text="Special", variable=self.special_var).grid(row=2, column=1, sticky="w", padx=5)

        gen_btn = ttk.Button(frame, text="Generate Password", command=self.generate_password)
        gen_btn.pack(pady=5)

        self.generated_password_var = tk.StringVar()
        output = ttk.Entry(frame, textvariable=self.generated_password_var, width=60)
        output.pack(pady=5)

        copy_btn = ttk.Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_btn.pack()

    def check_password_strength(self):
        password = self.pwd_var.get()
        if not password:
            messagebox.showwarning("Missing Input", "Please enter a password.")
            return

        evaluator = PasswordEvaluator(password)
        score, feedback = evaluator.evaluate()

        self.score_label.config(text=f"Score: {score}/100")
        self.feedback_box.delete("1.0", tk.END)

        for fb in feedback:
            self.feedback_box.insert(tk.END, f"• {fb}\n", "warn")

    def generate_password(self):
        try:
            gen = PasswordGenerator(
                length=self.length_var.get(),
                use_upper=self.upper_var.get(),
                use_lower=self.lower_var.get(),
                use_digits=self.digits_var.get(),
                use_special=self.special_var.get()
            )
            pwd = gen.generate()
            self.generated_password_var.set(pwd)
        except ValueError as e:
            messagebox.showerror("Generator Error", str(e))

    def copy_to_clipboard(self):
        pwd = self.generated_password_var.get()
        if pwd:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo("Copied", "Password copied to clipboard!")



