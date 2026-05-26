@echo off
echo جاري بناء البرنامج...
pip install -r requirements.txt
pyinstaller --onefile --windowed --name "منسق_الجوال" --icon=NONE main.py
echo تم البناء! الملف في مجلد dist
pause
