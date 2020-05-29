import subprocess

# Represent the command ls -a /var as a dictionary to use in subprocess.Popen
the_command = ["ls", "-a", "/var"]

# Send the stdout and stderr of the process to variables we can use in the script.
stdout, stderr = subprocess.Popen(the_command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# View the output of each variable.
print("stdout: %s" % stdout)
print("stderr: %s" % stderr)