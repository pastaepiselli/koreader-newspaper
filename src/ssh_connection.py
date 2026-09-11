import paramiko

hostname: str = ""
port: int = 2222

client = paramiko.SSHClient()
client.connect(hostname, port)

# TODO: caricare i file epub nella caretella koreader chiamatea news

client.close()
