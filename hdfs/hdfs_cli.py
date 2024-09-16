import subprocess

def run_cmd(arg_list):
    print(f"Running command {' '.join(arg_list)}")
    proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_out, s_err = proc.communicate()
    s_return = proc.returncode
    return s_out, s_err, s_return

run_cmd(['hdfs', 'dfs', '-mkdir', '/temp'])
run_cmd(['hdfs', 'dfs', '-put', 'result.txt', '/temp'])