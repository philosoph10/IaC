import pulumi_aws as aws


security_group = aws.ec2.SecurityGroup(
    "iac-security-group",
    description="Allow SSH and DB access",
    ingress=[
        {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]},
    ],
    egress=[
        {"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]},
    ],
)
