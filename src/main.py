def generate_id(l: list) -> int:
    if len(l) > 0:
        return max([task.id for task in l]) + 1
    return 0





