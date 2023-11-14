_counted = 0

def mark_as_counted(position):
    global _counted
    _counted |= (1 << position)


def check_if_counted(position):
    global _counted
    return bool(_counted & (1 << position))


def reset_all_to_not_counted():
    global _counted
    _counted = 0