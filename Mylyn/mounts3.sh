#!/bin/bash
# Update the package repository
sudo yum update -y

# Install dependencies
sudo yum install -y automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel

# Install EPEL repository if not already installed
sudo amazon-linux-extras install epel -y

# Install s3fs
git clone https://github.com/s3fs-fuse/s3fs-fuse.git
cd s3fs-fuse
./autogen.sh
./configure
make
sudo make install

# Go back to the home directory
cd ~

# Create a directory to mount the S3 bucket
sudo mkdir -p /mnt/s3bucket

# Mount the S3 bucket using the IAM role credentials
sudo s3fs your-bucket-name /mnt/s3bucket -o iam_role=auto -o url=https://s3.amazonaws.com -o use_path_request_style

# Add the S3 bucket to /etc/fstab for automatic mounting at boot
echo "s3fs#your-bucket-name /mnt/s3bucket fuse _netdev,iam_role=auto,url=https://s3.amazonaws.com,use_path_request_style 0 0" | sudo tee -a /etc/fstab
