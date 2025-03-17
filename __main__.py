# import pulumi
# import yaml
# from functional.firewall import db_ingress_rule
# from functional.servers import server1, server2

# # Function to generate Ansible inventory
# def generate_inventory(server1_ip, server2_ip):
#     inventory = {
#         "all": {
#             "hosts": {
#                 "server1": {"ansible_host": server1_ip, "ansible_user": "ubuntu"},
#                 "server2": {"ansible_host": server2_ip, "ansible_user": "ubuntu"},
#             },
#             "children": {
#                 "primary": {"hosts": {"server1": {}}},
#                 "replica": {"hosts": {"server2": {}}},
#             },
#         }
#     }

#     with open("inventory/aws.yml", "w") as f:
#         yaml.dump(inventory, f, default_flow_style=False)

# # Pulumi Outputs for public IPs
# server1_ip = server1.public_ip.apply(lambda ip: ip)
# server2_ip = server2.public_ip.apply(lambda ip: ip)

# # Generate inventory after resolving outputs
# pulumi.Output.all(server1_ip, server2_ip).apply(lambda ips: generate_inventory(*ips))

# # Export for reference
# pulumi.export("server1_public_ip", server1_ip)
# pulumi.export("server2_public_ip", server2_ip)
import pulumi
import yaml
from functional.firewall import db_ingress_rule
from functional.servers import server1, server2

# Function to generate Ansible inventory
def generate_inventory(server1_public_ip, server2_public_ip, server1_private_ip, server2_private_ip):
    inventory = {
        "all": {
            "hosts": {
                "server1": {
                    "ansible_host": server1_public_ip,  # Ansible connects via public IP
                    "ansible_user": "ubuntu",
                    "private_ip": server1_private_ip,  # Store private IP for internal use
                },
                "server2": {
                    "ansible_host": server2_public_ip,  # Ansible connects via public IP
                    "ansible_user": "ubuntu",
                    "private_ip": server2_private_ip,  # Store private IP for internal use
                },
            },
            "children": {
                "primary": {"hosts": {"server1": {}}},
                "replica": {"hosts": {"server2": {}}},
            },
        }
    }

    with open("inventory/aws.yml", "w") as f:
        yaml.dump(inventory, f, default_flow_style=False)

# Pulumi Outputs for both Public and Private IPs
server1_public_ip = server1.public_ip.apply(lambda ip: ip)
server2_public_ip = server2.public_ip.apply(lambda ip: ip)
server1_private_ip = server1.private_ip.apply(lambda ip: ip)
server2_private_ip = server2.private_ip.apply(lambda ip: ip)

# Generate inventory after resolving outputs
pulumi.Output.all(server1_public_ip, server2_public_ip, server1_private_ip, server2_private_ip).apply(
    lambda ips: generate_inventory(*ips)
)

# Export for reference (if needed)
pulumi.export("server1_public_ip", server1_public_ip)
pulumi.export("server2_public_ip", server2_public_ip)
pulumi.export("server1_private_ip", server1_private_ip)
pulumi.export("server2_private_ip", server2_private_ip)
