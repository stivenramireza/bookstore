resource "aws_instance" "bastion01" {
  ami           = var.ec2_ami
  instance_type = "t2.micro"
  key_name      = "${aws_key_pair.web_instance.key_name}"

  user_data_base64 = base64encode(templatefile("./scripts/bastion_setup.sh", {
    documentdb_dns: aws_docdb_cluster.docdb.endpoint
  }))

  subnet_id                   = aws_subnet.public01.id
  associate_public_ip_address = true
  vpc_security_group_ids      = [
    aws_security_group.ssh_public_access.id
  ]
}

output "bastion01_instace_public_ipv4" {
  value = aws_instance.bastion01.public_ip
}
