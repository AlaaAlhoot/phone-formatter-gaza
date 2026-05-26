import tkinter as tk
from tkinter import messagebox
from assets.style import *

class Screen2(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG)
        self.app = app

        # ── Header ──────────────────────────────────────
        header = tk.Frame(self, bg=PRIMARY, height=56)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="⚙️  الإعدادات",
                 font=FONT_TITLE, bg=PRIMARY, fg=WHITE).pack(side="right", padx=20)
        tk.Label(header, text="الخطوة 2 من 3",
                 font=FONT_SMALL, bg=PRIMARY, fg=GRAY).pack(side="left", padx=20)

        # ── Settings card ───────────────────────────────
        card = tk.Frame(self, bg=CARD, relief="solid", bd=1)
        card.pack(fill="x", padx=50, pady=25)

        def add_row(label_text):
            f = tk.Frame(card, bg=CARD)
            f.pack(fill="x", padx=20, pady=10)
            tk.Label(f, text=label_text, font=FONT_BOLD, bg=CARD,
                     fg=TEXT, width=24, anchor="e").pack(side="right")
            return f

        # Column
        r1 = add_row("عمود رقم الجوال:")
        self.col_var = tk.StringVar()
        self.col_menu = tk.OptionMenu(r1, self.col_var, "")
        self.col_menu.config(font=FONT, bg=WHITE, relief="solid",
                             activebackground=BG, width=22, anchor="e")
        self.col_menu["menu"].config(font=FONT)
        self.col_menu.pack(side="right", padx=10)

        tk.Frame(card, bg=BORDER, height=1).pack(fill="x", padx=20)

        # Group size
        r2 = add_row("عدد القيم في المجموعة:")
        self.size_var = tk.StringVar(value="20")
        tk.Entry(r2, textvariable=self.size_var, width=7,
                 **ENTRY, justify="center").pack(side="right", padx=10)

        tk.Frame(card, bg=BORDER, height=1).pack(fill="x", padx=20)

        # Separator
        r3 = add_row("الرمز الفاصل:")
        self.sep_var = tk.StringVar(value=";")
        for sym in [";", ","]:
            tk.Radiobutton(r3, text=sym, variable=self.sep_var, value=sym,
                           font=FONT_BOLD, bg=CARD, fg=PRIMARY,
                           activebackground=CARD, selectcolor=WHITE).pack(side="right", padx=6)
        tk.Label(r3, text="أو اكتب:", font=FONT_SMALL, bg=CARD,
                 fg=TEXT_LIGHT).pack(side="right", padx=(0, 4))
        self.custom_sep = tk.Entry(r3, width=5, **ENTRY, justify="center")
        self.custom_sep.pack(side="right")

        tk.Frame(card, bg=BORDER, height=1).pack(fill="x", padx=20)

        # Sep on last
        r4 = add_row("ضع الرمز على آخر قيمة في المجموعة:")
        self.sep_last_var = tk.BooleanVar(value=False)
        chk = tk.Checkbutton(r4, variable=self.sep_last_var, bg=CARD,
                              activebackground=CARD, selectcolor=WHITE,
                              relief="flat", cursor="hand2")
        chk.pack(side="right", padx=10)

        # ── Buttons ─────────────────────────────────────
        foot = tk.Frame(self, bg=BG)
        foot.pack(fill="x", padx=50, pady=20)
        tk.Label(foot, text="تطوير علاء الحوت",
                 font=FONT_SMALL, bg=BG, fg=GRAY).pack(side="left")
        tk.Button(foot, text="→  رجوع", **BTN_OUTLINE,
                  command=lambda: app.show_screen(0)).pack(side="right", padx=(8, 0))
        tk.Button(foot, text="معالجة  ←", **BTN_SUCCESS,
                  command=self.go_next).pack(side="right")

    def refresh(self):
        if self.app.df is None:
            return
        cols = list(self.app.df.columns)
        menu = self.col_menu["menu"]
        menu.delete(0, "end")
        for c in cols:
            menu.add_command(label=c, command=lambda v=c: self.col_var.set(v))
        if cols:
            self.col_var.set(cols[0])

    def go_next(self):
        col = self.col_var.get()
        if not col:
            messagebox.showwarning("تنبيه", "اختر عمود الجوال")
            return
        try:
            size = int(self.size_var.get())
            assert size > 0
        except:
            messagebox.showerror("خطأ", "عدد المجموعة يجب أن يكون رقماً صحيحاً موجباً")
            return
        sep = self.custom_sep.get().strip() or self.sep_var.get()
        new_settings = {
            "col":      col,
            "size":     size,
            "sep":      sep,
            "sep_last": self.sep_last_var.get()
        }
        # invalidate cache if settings changed
        if new_settings != self.app.last_settings:
            self.app.valid_rows   = []
            self.app.invalid_rows = []
            self.app.groups       = []
        self.app.settings = new_settings
        self.app.show_screen(2)
