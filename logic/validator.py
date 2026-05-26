def validate_phones(df, col):
    seen = set()
    valid_rows = []
    invalid_rows = []

    for _, row in df.iterrows():
        num = str(row[col]).strip()
        if num in seen:
            continue
        seen.add(num)

        digits = ''.join(filter(str.isdigit, num))
        if len(digits) == 9 and (digits.startswith("59") or digits.startswith("56")):
            r = row.copy()
            r[col] = digits
            valid_rows.append(r)
        else:
            invalid_rows.append(row)

    return valid_rows, invalid_rows
