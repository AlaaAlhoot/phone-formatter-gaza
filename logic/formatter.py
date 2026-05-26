def format_groups(valid_rows, col, group_size, separator, sep_on_last):
    numbers = ["0" + row[col] for row in valid_rows]
    groups = []
    for i in range(0, len(numbers), group_size):
        chunk = numbers[i:i + group_size]
        formatted = []
        for j, num in enumerate(chunk):
            is_last = j == len(chunk) - 1
            if is_last and not sep_on_last:
                formatted.append(num)
            else:
                formatted.append(num + separator)
        groups.append(formatted)
    return groups
