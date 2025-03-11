import pulumi
from functional.servers import server1, server2
from functional.firewall import db_ingress_rule

pulumi.export("server1_public_ip", server1.public_ip)
pulumi.export("server2_public_ip", server2.public_ip)
