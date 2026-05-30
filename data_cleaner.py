def get_clean_data(cursor):
    query = """
    SELECT *
    FROM corrupted_superstore
    WHERE Sales >= 0
      AND Quantity > 0
      AND Profit >= 0
      AND `Customer Name` IS NOT NULL
      AND `Customer Name` != ''
    """
    cursor.execute(query)
    return cursor.fetchall()