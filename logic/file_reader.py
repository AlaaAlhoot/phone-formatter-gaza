import pandas as pd

def read_file(path):
    ext = path.lower().split(".")[-1]
    if ext == "csv":
        df = pd.read_csv(path, dtype=str)
    elif ext in ("xlsx", "xls"):
        df = pd.read_excel(path, dtype=str)
    else:
        raise ValueError("صيغة الملف غير مدعومة")
    df = df.fillna("")
    return df
