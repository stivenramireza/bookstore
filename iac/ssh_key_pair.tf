resource "aws_key_pair" "web_instance" {
  key_name   = "ssh_web_instance"
  public_key = file("./ssh_keys/web_instance.pub")
}
