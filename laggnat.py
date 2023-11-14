def laggnat(a, b):
    if b > 12:
        return 'NO'
    else:
        _30th = [4, 6, 9, 11]
        _31th = [1, 3, 5, 7, 8, 10, 12]
        _28th = [2]
        if b in _30th and b not in _31th:
            if a > 30:
                return 'NO'
            else:
                return 'YES'
        if b in _30th and b not in _31th:
            if a > 30:
                return 'NO'
            else:
                return 'YES'
