Below is a basic example of production-ready Terraform configuration for creating an Amazon Virtual Private Cloud (VPC) with one EC2 instance. This example follows some standard AWS best practices, including using variable files and modules to manage resources.

```hcl
# vpc_module/main.tf

provider "aws" {
  region = var.region
}

variable "region" {}

resource "aws_vpc" "main" {
  cidr_block               = var.cidr_block
  enable_dns_support       = true
  enable_dns_hostnames     = true
  tags                      = {
    Name = "example-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.cidr_block
  availability_zone = var.availability_zones[0]
  map_public_ip_on_launch = true
  tags               = {
    Name = "example-public-subnet"
  }
}

resource "aws_security_group" "main" {
  name        = "default"
  description = "Default security group for VPC"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "example" {
  name = "sshkey"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_instance" "webserver" {
  ami                  = var.aws_ami
  instance_type        = "t2.micro"
  subnet_id            = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.main.id]
  key_name             = aws_key_pair.example.name

  tags = {
    Name = "example-webserver"
  }

  root_block_device {
    volume_size                = 8
    volume_type                 = var.aws_ebs_volume_type
    delete_on_termination       = true
    encrypted                    = false
  }
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_id" {
  value = aws_subnet.public.id
}

output "public_ip" {
  value = aws_instance.webserver.public_ip
}
```

Make sure to provide the necessary variables file (`variables.tf`):

```hcl
# vpc_module/variables.tf

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "cidr_block" {
  type    = string
  default = "10.0.0.0/16"
}

variable "aws_ami" {
  type    = string
  default = "ami-092b34f8a675dfe0c" # Example AMI for AWS, update with your actual AMI.
}

variable "aws_ebs_volume_type" {
  type    = string
  default = "standard"
}
```

And the main `main.tf` for using this module in another part of the configuration:

```hcl
# main.tf

module "vpc_module" {
  source      = "./vpc_module"
  region      = var.region
  cidr_block  = var.cidr_block
}

output "public_ip_for_webserver" {
  value = module.vpc_module.aws_instance.webserver.public_ip
}
```

Make sure to place these files in your workspace and run `terraform init`, then apply the configuration using `terraform apply`.

Remember, this is just a starting point. Depending on your requirements, you might need additional resources such as load balancers, RDS instances, EBS volumes, or other AWS services. Always review and test your Terraform configurations thoroughly to ensure they meet your needs securely and efficiently.