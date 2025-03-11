import pulumi_aws as aws
from .security import security_group


db_ingress_rule = aws.ec2.SecurityGroupRule(
    "db-access-rule",
    security_group_id=security_group.id,
    type="ingress",
    from_port=5432,
    to_port=5435,
    protocol="tcp",
    source_security_group_id=security_group.id,
)
