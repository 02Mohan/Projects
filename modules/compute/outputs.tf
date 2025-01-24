output "public_ip" {  # This might be redundant if you already have it in main.tf
  value = aws_instance.example.public_ip
}
