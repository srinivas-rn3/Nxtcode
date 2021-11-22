terraform {
required_providers {
aws = {
source = "hashicorp/aws"
version = "~> 3.27"
}
}

required_version = ">= 0.14.9"
}

resource "aws_key_pair" "terraform-demo" {
key_name = "MyEc2PrivateKey.ppk"
public_key = file("MyEc2PublicKey")
}

provider "aws" {
profile = "default"
region = "ap-south-1"
}

resource "aws_ebs_volume" "example" {
availability_zone = "ap-south-1a"
size = 40
}

resource "aws_instance" "Terraform_EC2_Creation" {
count = var.instance_count
ami = "ami-0f1fb91a596abf28d"
instance_type = "t2.micro"
key_name = aws_key_pair.terraform-demo.key_name
vpc_security_group_ids = ["sg-bbcb6fc2"]
  
root_block_device {
volume_size = "20"
volume_type = "gp2"
}


tags = {
Name = "Terraform-${count.index + 1}"
}
}
