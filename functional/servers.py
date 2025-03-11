import pulumi_aws as aws
from .security import security_group
from utils.variables import ami_id, instance_type, my_ssh_key, other_ssh_key


def create_server(name: str):
    user_data = f"""#!/bin/bash
    echo '{my_ssh_key}' >> /home/ubuntu/.ssh/authorized_keys
    echo '{other_ssh_key}' >> /home/ubuntu/.ssh/authorized_keys
    chmod 600 /home/ubuntu/.ssh/authorized_keys
    chown ubuntu:ubuntu /home/ubuntu/.ssh/authorized_keys
    """
    
    server = aws.ec2.Instance(
        name,
        ami=ami_id,
        instance_type=instance_type,
        user_data=user_data,
        security_groups=[security_group.name],
        tags={"Name": name},
    )
    return server

server1 = create_server("server1")
server2 = create_server("server2")
