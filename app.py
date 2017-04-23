import paramiko

hostname = '185.175.210.151'
port = 22
username = 'angsuman'
password = 'Angsu@2210'

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    #print(stdout.read())
    #app.run(host='0.0.0.0', port=80)
    s.close()
