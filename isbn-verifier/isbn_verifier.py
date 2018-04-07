def verify(isbn):
    count = 0
    total = 0
    for ch in isbn:
        if count <= 9 and ch.isdigit():
            total += int(ch) * (10 - count)
            count += 1
        elif count == 9 and ch == 'X':
            total += 10
            count += 1
        elif ch == '-':
            pass
        else:
            return False

    return count == 10 and not total % 11
