import avro

from avro.datafile import DataFileWriter
from avro.io import DatumWriter

employee = {
    "employee_id": 12,
    "employee_name": 'Andrey',
    "joining_date": 20240101,
    "salary": 123,
    "address": "test",
    "update_date_time": 20240101010101
}

