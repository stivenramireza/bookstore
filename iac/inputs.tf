variable "whitelist_ipv4" {
  type = string
  description = "Personal IPv4"
}

variable "ec2_ami" {
  type = string
  description = "Instance AWS AMI ID"
}

variable "project_name" {
  type = string
  description = "Porject Name"
}

variable "cluster_admin_username" {
  type = string
  description = "cluster username"
}

variable "cluster_admin_password" {
  type = string
  description = "cluster password"
}
