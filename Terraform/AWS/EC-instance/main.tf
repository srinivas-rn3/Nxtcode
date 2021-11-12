terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "Terraform Demo" {
  ami           = "ami-0831e2fc76f8844e6"
  instance_type = "t2.micro"
  instance_count = var.instance_count
  key_name = aws_key_pair.terraform-demo.key_name

  tags = {
    Name = "Terraform-${count.index + 1}"
  }
}
