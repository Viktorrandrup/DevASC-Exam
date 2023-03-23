from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.101",
    port="22",
    username="cisco",
    password="cisco123!",
)
# Goes directly into
command = []

command.append("do show ip interface brief")

command.append("do show ip route")

command.append("interface loopback 15")

command.append("ip address 15.16.17.18 255.255.255.0")

command.append("ip route 0.0.0.0 0.0.0.0 lo15")

command.append("exit")

command.append("do sh run interface lo15")

output = sshCli.send_config_set(command)

print(output)
