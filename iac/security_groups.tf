// ===============================================
//                      PUBLIC
// ===============================================

resource "aws_security_group" "web_access" {
  name        = "web_security_group"
  description = "Enable HTTP access"

  vpc_id = aws_vpc.main.id

  ingress {
    description = "Allow HTTP access from anywhere"
    from_port   = "80"
    to_port     = "80"
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow response traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "ssh_public_access" {
  name        = "ssh_public_access"
  description = "Enable SSH access"

  vpc_id = aws_vpc.main.id

  ingress {
    description = "Allow SSH access from anywhere"
    from_port   = "22"
    to_port     = "22"
    protocol    = "TCP"
    cidr_blocks = [var.whitelist_ipv4]
  }

  egress {
    description = "Allow response traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "ssh_private_access" {
  name        = "ssh_private_access"
  description = "Enable SSH access"

  vpc_id = aws_vpc.main.id

  ingress {
    description = "Allow SSH access from anywhere"
    from_port   = "22"
    to_port     = "22"
    protocol    = "TCP"
    cidr_blocks = [
      "172.31.0.0/20",
      "172.31.16.0/20"
    ]
  }

  egress {
    description = "Allow response traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "documentdb_access" {
  name        = "documentdb_private_access"
  description = "Enable Document access"

  vpc_id = aws_vpc.main.id

  ingress {
    description = "Allow Document access from anywhere"
    from_port   = "27017"
    to_port     = "27017"
    protocol    = "TCP"
    cidr_blocks = [
      # bastion public subnet
      "172.31.0.0/20",

      # lambdas private subnets
      "172.31.32.0/20",
      "172.31.48.0/20",
    ]
  }

  egress {
    description = "Allow response traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
