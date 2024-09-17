import pyarrow as pa
from pyarrow import parquet
import pandas as pd

employee_table = pa.table({
    "employee_id": [12],
    "employee_name": ['Andrey'],
    "joining_date": [20240101],
    "salary": [12300.5],
    "address": ["test"],
    "update_date_time": [20240101010101]
})
parquet.write_table(employee_table, "employee.parquet")

table = parquet.read_table("employee.parquet", columns=['employee_id', 'employee_name', 'salary'])
employee_df = table.to_pandas()
print(employee_df.head())
