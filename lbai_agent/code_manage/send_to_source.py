import paramiko

# 远程服务器的地址、用户名和密码
hostname = '192.168.2.33'
username = 'test1'
password = '123456'

# 本地文件路径和远程目录
local_file = 'created_code.py'
remote_directory = '/home/test1/lbai_agent_source/'

def send():
    # 创建SSH客户端对象
    ssh = paramiko.SSHClient()

    # 自动添加远程服务器的主机密钥（可选）
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接远程服务器
        ssh.connect(hostname, username=username, password=password)

        # 创建SFTP客户端对象
        sftp = ssh.open_sftp()

        try:
            # 上传文件到远程服务器
            sftp.put(local_file, remote_directory + local_file)

            print(f"文件 {local_file} 成功发送到远程目录 {remote_directory}")
        finally:
            # 关闭SFTP客户端连接
            sftp.close()
    finally:
        # 关闭SSH客户端连接
        ssh.close()
