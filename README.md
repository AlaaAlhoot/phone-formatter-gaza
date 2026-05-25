<div dir="rtl">

# 📱 منسق أرقام الهواتف الفلسطينية

تطبيق سطح مكتب لتنسيق أرقام الهواتف الفلسطينية وتجميعها في مجموعات جاهزة للإرسال عبر SMS — يدعم استيراد Excel/CSV، والتحقق من صحة الأرقام (56x/59x)، وتقسيمها إلى مجموعات قابلة للنسخ والتصدير بصيغة TXT/Excel.

---

## ✨ المميزات

- 📂 **استيراد الملفات** — يدعم صيغ `.xlsx` و `.xls` و `.csv`
- 🔍 **معاينة البيانات** — عرض عدد مخصص من الأسطر قبل المعالجة
- ✅ **التحقق من الأرقام** — يقبل فقط الأرقام المكونة من 9 خانات والتي تبدأ بـ `59` أو `56`
- 🚫 **حذف التكرار** — إزالة الأرقام المكررة تلقائياً
- ✂️ **تقسيم المجموعات** — تقسيم الأرقام إلى مجموعات بعدد يحدده المستخدم
- 🔣 **رمز فاصل مخصص** — اختيار `;` أو `,` أو أي رمز آخر
- 📊 **إحصائيات فورية** — عدد القيم الكلية، الصحيحة، الخاطئة، وعدد المجموعات
- 📋 **نسخ سريع** — نسخ أي مجموعة إلى الحافظة بنقرة واحدة
- 💾 **تصدير متعدد الصيغ**:
  - تصدير مجموعة واحدة كملف `.txt`
  - تصدير كل المجموعات في ملف `.txt` واحد
  - تصدير الأرقام الصحيحة كملف `.xlsx` مع كامل البيانات
  - تصدير الأرقام الخاطئة كملف `.xlsx` مع كامل البيانات
- 🌐 **واجهة عربية** — دعم كامل للغة العربية من اليمين لليسار (RTL)

---

## 🖥️ واجهة البرنامج

| الشاشة | الوصف |
|--------|-------|
| **الشاشة 1** | تحميل الملف ومعاينة البيانات |
| **الشاشة 2** | ضبط الإعدادات (العمود، حجم المجموعة، الرمز الفاصل) |
| **الشاشة 3** | عرض النتائج والإحصائيات والتصدير |

---

## ⚙️ متطلبات التشغيل

- Python 3.10 أو أحدث
- المكتبات المطلوبة:

```
pandas
openpyxl
xlrd
pyperclip
pyinstaller
```

---

## 🚀 التشغيل

**1. استنساخ المشروع:**
```bash
git clone https://github.com/AlaaAlhoot/phone-formatter-gaza.git
cd phone-formatter-gaza
```

**2. تثبيت المكتبات:**
```bash
pip install -r requirements.txt
```

**3. تشغيل البرنامج:**
```bash
python main.py
```

---

## 📦 تحويل إلى ملف EXE

```bash
# على Windows فقط — انقر مزدوج على الملف
build.bat

# أو عبر CMD
pyinstaller --onefile --windowed --name "منسق_الجوال" main.py
```

الملف التنفيذي سيظهر في مجلد `dist/`

---

## 🗂️ هيكلية المشروع

```
phone-formatter-gaza/
│
├── main.py                    # نقطة الدخول
├── app.py                     # التحكم بالشاشات والبيانات
├── requirements.txt
├── build.bat                  # بناء EXE على Windows
│
├── screens/
│   ├── screen1_load.py        # شاشة تحميل الملف
│   ├── screen2_settings.py    # شاشة الإعدادات
│   └── screen3_results.py     # شاشة النتائج
│
├── logic/
│   ├── file_reader.py         # قراءة xlsx, xls, csv
│   ├── validator.py           # التحقق من الأرقام وحذف التكرار
│   └── formatter.py           # تقسيم المجموعات وإضافة الرموز
│
├── utils/
│   └── exporter.py            # تصدير TXT و Excel
│
└── assets/
    └── style.py               # الألوان والخطوط وإعدادات RTL
```

---

## 📋 قواعد التحقق من الأرقام

| الشرط | القيمة |
|-------|--------|
| عدد الخانات | 9 خانات بالضبط |
| البادئة المقبولة | `59` أو `56` |
| الأرقام المكررة | تُحذف تلقائياً |
| الأرقام غير الصالحة | تُصدَّر في ملف Excel منفصل |

---

## 👨‍💻 المطور

**علاء الحوت**
مطور Django ومدرس جامعي — الجامعة الإسلامية بغزة

[![GitHub](https://img.shields.io/badge/GitHub-AlaaAlhoot-181717?style=flat&logo=github)](https://github.com/AlaaAlhoot)

---

</div>

---

# 📱 Palestinian Phone Number Formatter

A desktop application for formatting and grouping Palestinian phone numbers into SMS-ready groups — supports Excel/CSV import, phone number validation (56x/59x), group splitting, clipboard copy, and export to TXT/Excel.

---

## ✨ Features

- 📂 **File Import** — Supports `.xlsx`, `.xls`, and `.csv` formats
- 🔍 **Data Preview** — Preview a custom number of rows before processing
- ✅ **Number Validation** — Accepts only 9-digit numbers starting with `59` or `56`
- 🚫 **Duplicate Removal** — Automatically removes duplicate entries
- ✂️ **Group Splitting** — Split numbers into groups of a user-defined size
- 🔣 **Custom Separator** — Choose `;`, `,`, or any custom symbol
- 📊 **Live Statistics** — Total, valid, invalid count and number of groups
- 📋 **Quick Copy** — Copy any group to clipboard in one click
- 💾 **Multi-format Export**:
  - Export a single group as `.txt`
  - Export all groups in one `.txt` file
  - Export valid numbers as `.xlsx` with all original columns
  - Export invalid numbers as `.xlsx` with all original columns
- 🌐 **Arabic UI** — Full RTL Arabic language support

---

## 🖥️ Screens

| Screen | Description |
|--------|-------------|
| **Screen 1** | Load file and preview data |
| **Screen 2** | Configure settings (column, group size, separator) |
| **Screen 3** | View results, statistics, and export |

---

## ⚙️ Requirements

- Python 3.10+
- Dependencies:

```
pandas
openpyxl
xlrd
pyperclip
pyinstaller
```

---

## 🚀 Getting Started

**1. Clone the repository:**
```bash
git clone https://github.com/AlaaAlhoot/phone-formatter-gaza.git
cd phone-formatter-gaza
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the application:**
```bash
python main.py
```

---

## 📦 Build as EXE (Windows)

```bash
# Double-click the file
build.bat

# Or via CMD
pyinstaller --onefile --windowed --name "phone_formatter" main.py
```

The executable will be generated inside the `dist/` folder.

---

## 🗂️ Project Structure

```
phone-formatter-gaza/
│
├── main.py                    # Entry point
├── app.py                     # Screen controller & shared state
├── requirements.txt
├── build.bat                  # Windows EXE builder
│
├── screens/
│   ├── screen1_load.py        # File loading screen
│   ├── screen2_settings.py    # Settings screen
│   └── screen3_results.py     # Results & export screen
│
├── logic/
│   ├── file_reader.py         # Read xlsx, xls, csv
│   ├── validator.py           # Validate & deduplicate numbers
│   └── formatter.py           # Group splitting & formatting
│
├── utils/
│   └── exporter.py            # TXT & Excel export utilities
│
└── assets/
    └── style.py               # Colors, fonts, RTL settings
```

---

## 📋 Validation Rules

| Condition | Value |
|-----------|-------|
| Digit count | Exactly 9 digits |
| Accepted prefixes | `59` or `56` |
| Duplicates | Removed automatically |
| Invalid numbers | Exported to a separate Excel file |

---

## 👨‍💻 Developer

**Alaa Al-Hout**
Django Developer & University Instructor — Islamic University of Gaza

[![GitHub](https://img.shields.io/badge/GitHub-AlaaAlhoot-181717?style=flat&logo=github)](https://github.com/AlaaAlhoot)
