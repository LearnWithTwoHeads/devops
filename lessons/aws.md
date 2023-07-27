## AWS Services
- If a subnet is associated with a route table that has a route to the internet gateway it is known as a public subnet. If it is not associated with a route table that has route to the internet gateway it is known as a private subnet
- The EC2 instance is only aware of the private (internal) IP address space defined within the VPC
- You can provide internet access to your instances without assigning public IP addresses by using a NAT device
- The internet gateway provides the one-to-one NAT on behalf of your instance
- The steps to allow internet traffic into instances within your VPC: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html
- Intereseting guide on server architecture with VPCs: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html
- Two tier web architecture guide: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-web-database-servers.html

## Route53, EC2, S3, RDS