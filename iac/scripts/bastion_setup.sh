#!/bin/bash


# Default Variables
aws_custom_documentdb_tls='https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem'
documentdb_dns="${documentdb_dns}"


# Install Common Tools
apt-get update -qq && apt-get install -y unzip zip curl wget git


# Install MongoDB Client
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | \
tee /etc/apt/sources.list.d/mongodb-org-5.0.list
apt-get update -qq && apt-get install -y mongodb-org


# Download AWS TLS Certs for DocumentDB
wget -O /usr/local/share/rds-combined-ca-bundle.pem $aws_custom_documentdb_tls
cat <<END >> /etc/bash.bashrc
echo DocumentDB Domain Name: $documentdb_dns
END
