FONT       = ("Segoe UI", 11)
FONT_BOLD  = ("Segoe UI", 11, "bold")
FONT_TITLE = ("Segoe UI", 17, "bold")
FONT_SMALL = ("Segoe UI", 9)
FONT_NUM   = ("Consolas", 10)

BG           = "#EEF2F7"
PRIMARY      = "#1A5276"
PRIMARY_DARK = "#154360"
ACCENT       = "#1E8449"
ACCENT_LIGHT = "#27AE60"
DANGER       = "#C0392B"
DANGER_LIGHT = "#E74C3C"
WHITE        = "#FFFFFF"
GRAY         = "#AEB6BF"
TEXT         = "#1C2833"
TEXT_LIGHT   = "#7F8C8D"
CARD         = "#FFFFFF"
BORDER       = "#D5D8DC"
HEADER_BG    = "#1A5276"

BTN = {"font": FONT_BOLD, "relief": "flat", "cursor": "hand2", "padx": 14, "pady": 7}
BTN_PRIMARY = {**BTN, "bg": PRIMARY,      "fg": WHITE, "activebackground": PRIMARY_DARK, "activeforeground": WHITE}
BTN_SUCCESS = {**BTN, "bg": ACCENT,       "fg": WHITE, "activebackground": "#196F3D",    "activeforeground": WHITE}
BTN_DANGER  = {**BTN, "bg": DANGER,       "fg": WHITE, "activebackground": "#922B21",    "activeforeground": WHITE}
BTN_OUTLINE = {**BTN, "bg": WHITE,        "fg": PRIMARY, "activebackground": BG,         "activeforeground": PRIMARY}
BTN_SMALL   = {"font": FONT_SMALL, "relief": "flat", "cursor": "hand2", "padx": 10, "pady": 4}

ENTRY = {"font": FONT, "relief": "solid", "bd": 1, "bg": WHITE, "fg": TEXT, "highlightthickness": 0}
