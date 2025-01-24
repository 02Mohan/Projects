module "network" {
  source = "../../modules/network"
}

module "compute" {
  source        = "../../modules/compute/"
  ami_id        = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = module.network.subnet_id  # This is correct, as you're passing subnet_id here
}
