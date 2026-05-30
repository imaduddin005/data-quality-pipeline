def check_duplicate_orders(cursor):
    query = """
    SELECT `Order ID`, COUNT(*) as cnt
    FROM corrupted_superstore
    GROUP BY `Order ID`
    HAVING COUNT(*) > 1
    """

    cursor.execute(query)
    result = cursor.fetchall()

    formatted = []

    for row in result:
        formatted.append(f"{row[0]} → {row[1]} duplicates")

    return formatted