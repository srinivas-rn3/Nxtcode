terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

resource "aws_key_pair" "terraform-demo" {
  key_name   = "terraform-demo"
  public_key = file("terraform-demo.pub")
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "Terraform_EC2_Creation" {
  ami           = "ami-0831e2fc76f8844e6"
  instance_type = "t2.micro"
  instance_count = var.instance_count
  key_name = aws_key_pair.terraform-demo.key_name

  tags = {
    Name = "Terraform-${count.index + 1}"
  }
}
