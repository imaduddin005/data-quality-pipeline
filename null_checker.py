def check_null_customer_name(cursor):
    query = """
    SELECT COUNT(*)
    FROM corrupted_superstore
    WHERE `Customer Name` IS NULL
    """

    cursor.execute(query)

    result = cursor.fetchone()

    return result[0]