import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from assets.style import *
from logic.file_reader import read_file

class Screen1(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG)
        self.app = app

        # ── Top header bar ──────────────────────────────
        header = tk.Frame(self, bg=PRIMARY, height=56)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="📱 منسق أرقام الجوال",
                 font=FONT_TITLE, bg=PRIMARY, fg=WHITE).pack(side="right", padx=20)
        tk.Label(header, text="الخطوة 1 من 3",
                 font=FONT_SMALL, bg=PRIMARY, fg=GRAY).pack(side="left", padx=20)

        # ── File card ───────────────────────────────────
        card = tk.Frame(self, bg=CARD, relief="solid", bd=1)
        card.pack(fill="x", padx=35, pady=20)

        tk.Label(card, text="اختيار الملف", font=FONT_BOLD,
                 bg=CARD, fg=PRIMARY).pack(anchor="e", padx=15, pady=(12, 4))
        tk.Label(card, text="يدعم: xlsx  |  xls  |  csv",
                 font=FONT_SMALL, bg=CARD, fg=TEXT_LIGHT).pack(anchor="e", padx=15)

        sep = tk.Frame(card, bg=BORDER, height=1)
        sep.pack(fill="x", padx=15, pady=8)

        file_row = tk.Frame(card, bg=CARD)
        file_row.pack(fill="x", padx=15, pady=(0, 12))

        tk.Button(file_row, text="📂 استعراض", **BTN_PRIMARY,
                  command=self.browse).pack(side="left", padx=(0, 10))
        self.path_var = tk.StringVar(value="لم يتم اختيار ملف بعد...")
        tk.Label(file_row, textvariable=self.path_var, font=FONT_SMALL,
                 bg=CARD, fg=TEXT_LIGHT, anchor="e").pack(side="right", fill="x", expand=True)

        # ── Preview controls ────────────────────────────
        ctrl = tk.Frame(self, bg=BG)
        ctrl.pack(fill="x", padx=35, pady=(0, 8))
        tk.Label(ctrl, text="عدد الأسطر للعرض:", font=FONT,
                 bg=BG, fg=TEXT).pack(side="right")
        self.rows_var = tk.StringVar(value="5")
        tk.Entry(ctrl, textvariable=self.rows_var, width=5,
                 **ENTRY, justify="center").pack(side="right", padx=6)
        tk.Button(ctrl, text="عرض", **BTN_OUTLINE,
                  command=self.show_preview).pack(side="right")

        # ── Table ───────────────────────────────────────
        tbl_frame = tk.Frame(self, bg=BG)
        tbl_frame.pack(fill="both", expand=True, padx=35)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", font=FONT, rowheight=26, background=WHITE,
                        fieldbackground=WHITE, foreground=TEXT)
        style.configure("Treeview.Heading", font=FONT_BOLD,
                        background=PRIMARY, foreground=WHITE)
        style.map("Treeview", background=[("selected", PRIMARY)])

        self.tree = ttk.Treeview(tbl_frame, show="headings", height=9)
        sx = ttk.Scrollbar(tbl_frame, orient="horizontal", command=self.tree.xview)
        sy = ttk.Scrollbar(tbl_frame, orient="vertical",   command=self.tree.yview)
        self.tree.configure(xscrollcommand=sx.set, yscrollcommand=sy.set)
        sy.pack(side="left", fill="y")
        self.tree.pack(fill="both", expand=True)
        sx.pack(fill="x")

        # ── Footer ──────────────────────────────────────
        foot = tk.Frame(self, bg=BG)
        foot.pack(fill="x", padx=35, pady=12)
        tk.Label(foot, text="تطوير علاء الحوت",
                 font=FONT_SMALL, bg=BG, fg=GRAY).pack(side="left")
        tk.Button(foot, text="التالي  ←", **BTN_SUCCESS,
                  command=self.go_next).pack(side="right")

    def browse(self):
        path = filedialog.askopenfilename(
            filetypes=[("ملفات البيانات", "*.xlsx *.xls *.csv")])
        if not path:
            return
        try:
            self.app.df = read_file(path)
            # reset cache
            self.app.last_settings = {}
            self.app.valid_rows = []
            self.app.invalid_rows = []
            self.app.groups = []
            self.path_var.set(path)
            self.show_preview()
        except Exception as e:
            messagebox.showerror("خطأ", str(e))

    def show_preview(self):
        if self.app.df is None:
            return
        try:
            n = max(1, int(self.rows_var.get()))
        except:
            n = 5
        df = self.app.df.head(n)
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        for col in df.columns:
            self.tree.heading(col, text=col, anchor="e")
            self.tree.column(col, width=140, anchor="e", minwidth=80)
        for i, (_, row) in enumerate(df.iterrows()):
            tag = "even" if i % 2 == 0 else "odd"
            self.tree.insert("", "end", values=list(row), tags=(tag,))
        self.tree.tag_configure("even", background="#F2F3F4")
        self.tree.tag_configure("odd",  background=WHITE)

    def go_next(self):
        if self.app.df is None:
            messagebox.showwarning("تنبيه", "يرجى اختيار ملف أولاً")
            return
        self.app.show_screen(1)
