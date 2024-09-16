from pyarrow import fs

hadoop_fs = fs.HadoopFileSystem('127.0.0.1', 9000)

hadoop_fs.create_dir('/test')
info = hadoop_fs.get_file_info('/')
print(info)