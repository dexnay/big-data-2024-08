import subprocess

def run_cmd(arg_list):
    print(f"Running command {' '.join(arg_list)}")
    proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_out, s_err = proc.communicate()
    s_return = proc.returncode
    return s_out, s_err, s_return

#run_cmd(['/home/student/hadoop-2.10.2/bin/hdfs', 'dfs', '-mkdir', '/temp1'])
#run_cmd(['/home/student/hadoop-2.10.2/bin/hdfs', 'dfs', '-put', 'result.txt', '/temp1'])
(s_out, s_err, s_return) = run_cmd(['/home/student/hadoop-2.10.2/bin/hdfs', 'dfs', '-cat', '/temp1/result.txt'])
print(f"{s_out} {s_err} {s_return}")