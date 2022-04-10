resource "aws_docdb_cluster" "docdb" {
  cluster_identifier      = "${var.project_name}-docdb-cluster"
  engine                  = "docdb"
  master_username         = "${var.cluster_admin_username}"
  master_password         = "${var.cluster_admin_password}"
  backup_retention_period = 1
  preferred_backup_window = "07:00-09:00"
  skip_final_snapshot     = true
  apply_immediately       = true

  vpc_security_group_ids  = [
    aws_security_group.documentdb_access.id
  ]

  db_subnet_group_name    = aws_docdb_subnet_group.default.name
}

resource "aws_docdb_cluster_instance" "cluster_instances" {
  count              = 1
  engine             = "docdb"
  identifier         = "${var.project_name}-docdb-instance-${count.index}"
  cluster_identifier = aws_docdb_cluster.docdb.id
  instance_class     = "db.t3.medium"
  apply_immediately  = true
}

resource "aws_docdb_subnet_group" "default" {
  name       = "main"
  subnet_ids = [
    aws_subnet.private01.id, 
    aws_subnet.private02.id
  ]

  tags = {
    Name = "My docdb subnet group"
  }
}

output "cluster_docdb_dns" {
  value = aws_docdb_cluster.docdb.endpoint
}
