from sql_generator import generate_sql
from db import execute_query

question = input("Ask: ")


sql = generate_sql(question)


##only select queries allowed 
if not sql.upper().startswith("SELECT"):
    raise Exception("Only SELECT queries allowed")

print("\nGenerated SQL:")
print(sql)

rows = execute_query(sql)

print("\nResults:")

for row in rows:
    print(row)