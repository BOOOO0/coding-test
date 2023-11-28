def number(str):
    if str == "code":
        return 0
    if str == "date":
        return 1
    if str == "maximum":
        return 2
    return 3


def extract(data, ext, val_ext):
    list = []
    for d in data:
        if d[ext] < val_ext:
            list.append(d)
    return list


def solution(data, ext, val_ext, sort_by):
    answer = extract(data, number(ext), val_ext)

    return sorted(answer, key=lambda x: x[number(sort_by)])
