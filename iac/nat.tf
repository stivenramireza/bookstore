resource "aws_eip" "nat_gateway" {
  vpc = true
}

resource "aws_nat_gateway" "public01" {
  allocation_id = aws_eip.nat_gateway.id
  subnet_id     = aws_subnet.public01.id

  depends_on = [aws_internet_gateway.gw]
}

resource "aws_eip" "nat_gateway_02" {
  vpc = true
}

resource "aws_nat_gateway" "public02" {
  allocation_id = aws_eip.nat_gateway_02.id
  subnet_id     = aws_subnet.public02.id

  depends_on = [aws_internet_gateway.gw]
}
