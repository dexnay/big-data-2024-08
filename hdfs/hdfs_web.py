from pywebhdfs.webhdfs import PyWebHdfsClient

webhdfs_client = PyWebHdfsClient('localhost', '50070', 'hadoop_web')
webhdfs_client.make_dir('/test')
fs_list = webhdfs_client.list_dir('/')
print(fs_list)

