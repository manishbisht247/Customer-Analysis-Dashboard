def get_customers(cursor, country = None, gender = None, minAge = None, maxAge = None):
    query = "SELECT * FROM customers"
    conditions = []
    values = []

    if country:
        conditions.append("country = %s")
        values.append(country)
    if gender:
        conditions.append("gender = %s")
        values.append(gender)
    if minAge:
        conditions.append("Age >= %s ")
        values.append(minAge)
    if maxAge:
        conditions.append("Age <= %s")
        values.append(maxAge)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    cursor.execute(query, values)
    return cursor.fetchall()