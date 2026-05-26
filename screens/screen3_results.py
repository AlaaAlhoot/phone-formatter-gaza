import tkinter as tk
from tkinter import filedialog, messagebox
from assets.style import *
from logic.validator import validate_phones
from logic.formatter import format_groups
from utils.exporter import (export_all_txt, export_group_txt,
                             export_invalid_excel, export_valid_excel)
import pyperclip

class Screen3(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG)
        self.app = app

        # ── Header ──────────────────────────────────────
        header = tk.Frame(self, bg=PRIMARY, height=56)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="📊  النتائج",
                 font=FONT_TITLE, bg=PRIMARY, fg=WHITE).pack(side="right", padx=20)
        tk.Label(header, text="الخطوة 3 من 3",
                 font=FONT_SMALL, bg=PRIMARY, fg=GRAY).pack(side="left", padx=20)

        # ── Stats row ───────────────────────────────────
        self.stats_frame = tk.Frame(self, bg=CARD, relief="solid", bd=1)
        self.stats_frame.pack(fill="x", padx=30, pady=(14, 4))

        # ── Sizes bar ───────────────────────────────────
        self.sizes_frame = tk.Frame(self, bg=CARD, relief="solid", bd=1)
        self.sizes_frame.pack(fill="x", padx=30, pady=(0, 8))

        # ── Scrollable groups ───────────────────────────
        outer = tk.Frame(self, bg=BG)
        outer.pack(fill="both", expand=True, padx=30)

        self.canvas = tk.Canvas(outer, bg=BG, highlightthickness=0)
        sb = tk.Scrollbar(outer, orient="vertical", command=self.canvas.yview)
        self.inner = tk.Frame(self.canvas, bg=BG)
        self.inner.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self._cw = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.canvas.configure(yscrollcommand=sb.set)
        self.canvas.bind("<Configure>",
            lambda e: self.canvas.itemconfig(self._cw, width=e.width))
        self.canvas.bind_all("<MouseWheel>",
            lambda e: self.canvas.yview_scroll(-1*(e.delta//120), "units"))
        sb.pack(side="left", fill="y")
        self.canvas.pack(side="right", fill="both", expand=True)

        # ── Footer buttons ───────────────────────────────
        foot = tk.Frame(self, bg=BG)
        foot.pack(fill="x", padx=30, pady=10)
        tk.Label(foot, text="تطوير علاء الحوت",
                 font=FONT_SMALL, bg=BG, fg=GRAY).pack(side="left")
        tk.Button(foot, text="→  رجوع", **BTN_OUTLINE,
                  command=lambda: app.show_screen(1)).pack(side="right", padx=4)
        tk.Button(foot, text="📥 تصدير كل المجموعات  txt", **BTN_PRIMARY,
                  command=self.export_all).pack(side="right", padx=4)
        tk.Button(foot, text="✅ الصحيحة  Excel", **BTN_SUCCESS,
                  command=self.export_valid).pack(side="right", padx=4)
        tk.Button(foot, text="⚠️ الأخطاء  Excel", **BTN_DANGER,
                  command=self.export_invalid).pack(side="right", padx=4)

    # ── Refresh ──────────────────────────────────────────
    def refresh(self):
        s = self.app.settings
        # Use cached results if settings haven't changed
        if not self.app.groups or not self.app.last_settings or s != self.app.last_settings:
            valid, invalid = validate_phones(self.app.df, s["col"])
            self.app.valid_rows   = valid
            self.app.invalid_rows = invalid
            self.app.groups       = format_groups(valid, s["col"], s["size"], s["sep"], s["sep_last"])
            self.app.last_settings = dict(s)

        self._build_stats()
        self._build_sizes()
        self._build_groups()

    # ── Build stats ──────────────────────────────────────
    def _build_stats(self):
        for w in self.stats_frame.winfo_children():
            w.destroy()
        items = [
            ("إجمالي القيم",   len(self.app.df),           PRIMARY),
            ("صحيحة",          len(self.app.valid_rows),   ACCENT),
            ("خاطئة",          len(self.app.invalid_rows), DANGER),
            ("عدد المجموعات", len(self.app.groups),        PRIMARY),
        ]
        for i, (label, val, color) in enumerate(items):
            if i > 0:
                tk.Frame(self.stats_frame, bg=BORDER, width=1).pack(
                    side="right", fill="y", pady=10)
            f = tk.Frame(self.stats_frame, bg=CARD)
            f.pack(side="right", expand=True, fill="x", pady=12, padx=8)
            tk.Label(f, text=str(val),
                     font=("Segoe UI", 22, "bold"), bg=CARD, fg=color).pack()
            tk.Label(f, text=label,
                     font=FONT_SMALL, bg=CARD, fg=TEXT_LIGHT).pack()

    # ── Build sizes bar ──────────────────────────────────
    def _build_sizes(self):
        for w in self.sizes_frame.winfo_children():
            w.destroy()
        if not self.app.groups:
            return
        parts = "   |   ".join(
            [f"م{i+1}: {len(g)} قيمة" for i, g in enumerate(self.app.groups)])
        tk.Label(self.sizes_frame, text=parts,
                 font=FONT_SMALL, bg=CARD, fg=TEXT_LIGHT).pack(pady=6, padx=12)

    # ── Build groups ─────────────────────────────────────
    def _build_groups(self):
        for w in self.inner.winfo_children():
            w.destroy()

        sep = self.app.settings.get("sep", ";")

        for i, group in enumerate(self.app.groups, 1):
            card = tk.Frame(self.inner, bg=CARD, relief="solid", bd=1)
            card.pack(fill="x", pady=5)

            # Header
            hdr = tk.Frame(card, bg=HEADER_BG)
            hdr.pack(fill="x")
            tk.Label(hdr, text=f"المجموعة {i}   —   {len(group)} قيمة",
                     font=FONT_BOLD, bg=HEADER_BG, fg=WHITE).pack(side="right", padx=14, pady=8)
            tk.Button(hdr, text="💾 تصدير txt",
                      **BTN_SMALL, bg=WHITE, fg=ACCENT_LIGHT,
                      activebackground="#FDFEFE", activeforeground=ACCENT,
                      command=lambda g=group, idx=i: self.export_one(g, idx)
                      ).pack(side="left", padx=8, pady=6)
            tk.Button(hdr, text="📋 نسخ",
                      **BTN_SMALL, bg=WHITE, fg=PRIMARY,
                      activebackground="#FDFEFE", activeforeground=PRIMARY_DARK,
                      command=lambda g=group, sv=sep: self.copy_group(g, sv)
                      ).pack(side="left", padx=(0, 6), pady=6)

            # Numbers text box
            txt = tk.Text(card, font=FONT_NUM, bg="#F8F9FA", fg=TEXT,
                          relief="flat", height=min(len(group), 6),
                          wrap="none", padx=12, pady=8,
                          selectbackground=PRIMARY, selectforeground=WHITE)
            txt.insert("1.0", "\n".join(group))
            txt.config(state="disabled")

            sb_x = tk.Scrollbar(card, orient="horizontal", command=txt.xview)
            txt.configure(xscrollcommand=sb_x.set)
            txt.pack(fill="x", padx=10, pady=(6, 0))
            sb_x.pack(fill="x", padx=10, pady=(0, 8))

    # ── Actions ──────────────────────────────────────────
    def copy_group(self, group, sep):
        # Copy WITH separator (as displayed)
        pyperclip.copy("\n".join(group))
        messagebox.showinfo("تم النسخ", "✓ تم نسخ الأرقام إلى الحافظة")

    def export_one(self, group, idx):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile=f"المجموعة_{idx}.txt",
            filetypes=[("Text", "*.txt")])
        if path:
            # Export numbers only, no group label
            export_group_txt(group, path)
            messagebox.showinfo("تم", f"✓ تم تصدير المجموعة {idx}")

    def export_all(self):
        if not self.app.groups:
            messagebox.showwarning("تنبيه", "لا توجد مجموعات للتصدير")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="كل_المجموعات.txt",
            filetypes=[("Text", "*.txt")])
        if path:
            export_all_txt(self.app.groups, path)
            messagebox.showinfo("تم", "✓ تم تصدير كل المجموعات")

    def export_invalid(self):
        if not self.app.invalid_rows:
            messagebox.showinfo("تنبيه", "لا توجد قيم خاطئة")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            initialfile="الأرقام_الخاطئة.xlsx",
            filetypes=[("Excel", "*.xlsx")])
        if path:
            export_invalid_excel(self.app.invalid_rows,
                                 list(self.app.df.columns), path)
            messagebox.showinfo("تم", "✓ تم تصدير الأرقام الخاطئة")

    def export_valid(self):
        if not self.app.valid_rows:
            messagebox.showinfo("تنبيه", "لا توجد قيم صحيحة")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            initialfile="الأرقام_الصحيحة.xlsx",
            filetypes=[("Excel", "*.xlsx")])
        if path:
            export_valid_excel(self.app.valid_rows,
                               list(self.app.df.columns), path)
            messagebox.showinfo("تم", "✓ تم تصدير الأرقام الصحيحة")
