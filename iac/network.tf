resource "aws_vpc" "main" {
  cidr_block       = "172.31.0.0/16"
  instance_tenancy = "default"
  enable_dns_support = true
  enable_dns_hostnames = true
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table" "public_igw" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
}

// ================= // 
// PUBLIC SUBNET 01 //
// ================= // 
resource "aws_subnet" "public01" {
  cidr_block       = "172.31.0.0/20"
  vpc_id     = aws_vpc.main.id

  availability_zone = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true 
}

resource "aws_route_table_association" "ig01" {
  subnet_id      = aws_subnet.public01.id
  route_table_id = aws_route_table.public_igw.id
}
// ================= // 
// PUBLIC SUBNET 02  //
// ================= // 
resource "aws_subnet" "public02" {
  cidr_block       = "172.31.16.0/20"
  vpc_id     = aws_vpc.main.id
  availability_zone = data.aws_availability_zones.available.names[1]

  map_public_ip_on_launch = true 
}

resource "aws_route_table_association" "ig02" {
  subnet_id      = aws_subnet.public02.id
  route_table_id = aws_route_table.public_igw.id
}

data "aws_availability_zones" "available" {
  state = "available"
}

// ================= // 
// PRIVATE SUBNET 01 //
// ================= // 
resource "aws_subnet" "private01" {
  cidr_block        = "172.31.32.0/20"
  vpc_id            = aws_vpc.main.id
  availability_zone = data.aws_availability_zones.available.names[0]
}

resource "aws_route_table" "nat01" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.public01.id
  }
}

resource "aws_route_table_association" "nat01" {
  subnet_id      = aws_subnet.private01.id
  route_table_id = aws_route_table.nat01.id
}

// ================= // 
// PRIVATE SUBNET 02 //
// ================= // 
resource "aws_subnet" "private02" {
  cidr_block        = "172.31.48.0/20"
  vpc_id            = aws_vpc.main.id
  availability_zone = data.aws_availability_zones.available.names[1]
}

resource "aws_route_table" "nat02" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.public02.id
  }
}

resource "aws_route_table_association" "nat02" {
  subnet_id      = aws_subnet.private02.id
  route_table_id = aws_route_table.nat02.id
}

