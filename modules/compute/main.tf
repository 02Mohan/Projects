resource "aws_instance" "example" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = var.subnet_id  # Use the subnet_id variable here

  tags = {
    Name = "ExampleInstance"
  }
}
