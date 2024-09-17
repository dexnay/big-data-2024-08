import pyarrow as pa
from pyarrow import parquet

pa.table({
    "employee_id": [12],
    "employee_name": ['Andrey'],
    "joining_date": [20240101],
    "salary": [12300.5],
    "address": ["test"],
    "update_date_time": [20240101010101]
})
parquet.write_table("employee.parquet")
