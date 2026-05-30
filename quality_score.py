def get_null_score(total_rows, null_count):
    if total_rows == 0:
        return 0
    return round(((total_rows - null_count) / total_rows) * 100, 2)


def get_duplicate_score(total_rows, duplicate_count):
    if total_rows == 0:
        return 0
    return round(((total_rows - duplicate_count) / total_rows) * 100, 2)


def get_validity_score(total_rows, invalid_count):
    if total_rows == 0:
        return 0
    return round(((total_rows - invalid_count) / total_rows) * 100, 2)


def get_overall_score(null_score, dup_score, validity_score):
    return round((null_score + dup_score + validity_score) / 3, 2)