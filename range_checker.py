def check_invalid_values(cursor):
    query = """
    SELECT *
    FROM corrupted_superstore
    WHERE Sales < 0 OR Quantity <= 0
    """
    cursor.execute(query)
    return cursor.fetchall()