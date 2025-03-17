# AWS Server Replication with Pulumi & Ansible

## Overview

This project provisions two AWS EC2 instances using Pulumi and configures PostgreSQL replication between them using Ansible.

## Features

- **AWS EC2 Setup**: Creates two server instances with Pulumi.
- **Security Configuration**:
  - Allows all connections on port `22` (SSH).
  - Allows connections on ports `5432-5435` between instances in the same security group.
- **Replication Configuration**:
  - **Streaming Replication** is enabled on the `cluster main` of the `replica` server.
  - **Logical Replication** is set up on the `logical_replication` cluster.

## Prerequisites

Ensure you have the following installed before running the setup:

- [Pulumi](https://www.pulumi.com/)
- [AWS Vault](https://github.com/99designs/aws-vault)
- [Ansible](https://www.ansible.com/)
- Configured AWS credentials stored in `aws-vault`.

## Setup Instructions

1. **Deploy AWS Infrastructure**  
   Run the following command to create the EC2 instances:
   ```sh
   aws-vault exec <your_credentials> -- pulumi up
   ```
1. **Wait for Server Initialization**  
   After running Pulumi, allow a few minutes for the EC2 instances to fully initialize before proceeding.

2. **Configure Replication with Ansible**  
   Once the servers are ready, execute the following command:
   ```sh
   ansible-playbook -i inventory/aws.yml site.yml
   ```
### Notes

- **AWS Credentials**: Replace `<your_credentials>` with your AWS Vault profile before running Pulumi.  
- **Server Initialization**: Wait for the servers to fully initialize before executing the Ansible playbook.  
- **Troubleshooting**: If you face connection issues, check the security group settings.  
