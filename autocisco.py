import netmiko
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.108.6',
    port = 22,
    username = 'admin',
    password = 'pass',
)
output = sshCli.send_command("show ip int br")
print("{}\n".format(output))
config_commands = [
    'int gi 2',
    'ip add 192.168.102.6 255.255.255.0',
    'desc PYTHONBYROB\'s gigabit 2',
    'no shut',
    'int gi 3',
    'ip add 192.168.103.6 255.255.255.0',
    'desc PYTHONBYROB\'s gigabit 3',
    'no shut'
]
sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))
output = sshCli.send_command("show ip int br")
print("{}\n".format(output))
