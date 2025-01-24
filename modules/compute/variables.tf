variable "subnet_id" {
  description = "The ID of the subnet where the EC2 instance will be launched"
  type        = string
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "Type of the EC2 instance"
  type        = string
}

variable "key_name" {
  description = "The EC2 key pair name"
  type        = string
}
