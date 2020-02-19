def long(str):
    if len(str) >= 8:
        return True
    else:
        return False

def reg(str):
    if str.isupper() or str.islower() or str.isnumeric():
        return False
    else:
        return True

def num(str):
    for i in str:
        if i.isnumeric():
            return True
    return False

def spec(str):
    if '@' in str or '#' in str or '%' in str or '&' in str or '_' in str:
        return True
    return False

def if_ch(str):
    if str.isupper() or str.islower() or str.isnumeric() or spec(str):
        return True
    return False


def pas(str):
    if long(str) and reg(str) and num(str) and spec(str):
        for i in str:
            if if_ch(i):
                continue
            else:
                return False
        return True
    return False

print(pas('Fg4%rrrrr'))