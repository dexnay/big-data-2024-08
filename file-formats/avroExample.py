import avro.schema

from avro.datafile import DataFileWriter
from avro.io import DatumWriter

file_schema = avro.schema.parse(open("employee.avsc", 'r').read())
print(file_schema)

employee = {
    "employee_id": 12,
    "employee_name": 'Andrey',
    "joining_date": 20240101,
    "salary": 12300.5,
    "address": "test",
    "update_date_time": 20240101010101
}

writer = DataFileWriter(open("employee.avro", "wb"), DatumWriter(), file_schema)
writer.append(employee)
writer.close()