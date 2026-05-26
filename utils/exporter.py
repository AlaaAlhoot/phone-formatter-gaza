import pandas as pd

def export_all_txt(groups, path):
    """Export all groups with label headers."""
    lines = []
    for i, g in enumerate(groups, 1):
        lines.append(f"المجموعة {i}:")
        lines.extend(g)
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def export_group_txt(group, path):
    """Export single group — numbers only, no label."""
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(group))

def export_invalid_excel(invalid_rows, columns, path):
    """Export invalid rows with all original columns."""
    df = pd.DataFrame(invalid_rows, columns=columns)
    df.to_excel(path, index=False)

def export_valid_excel(valid_rows, columns, path):
    """Export valid rows with all original columns."""
    df = pd.DataFrame(valid_rows, columns=columns)
    df.to_excel(path, index=False)
