# AWS provider configuration
region         = "us-east-1"
profile        = "default"

# Project metadata
project_name   = "my-app"
environment    = "dev"
owner          = "dev-team"

# VPC configuration
vpc_cidr       = "10.0.0.0/16"
public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
private_subnets = ["10.0.101.0/24", "10.0.102.0/24"]

# EC2 instance configuration
instance_type  = "t3.micro"
key_pair_name  = "my-keypair"
allowed_ssh_cidr = "0.0.0.0/0"  # Be cautious with open access

# RDS database configuration
db_engine         = "postgres"
db_engine_version = "13.4"
db_instance_class = "db.t3.micro"
db_name           = "appdb"
db_username       = "admin"
db_password       = "securepassword123"  # Consider using secrets manager
db_allocated_storage = 20

# Autoscaling configuration
asg_min_size        = 1
asg_max_size        = 3
asg_desired_capacity = 2

# Tags applied to all resources
common_tags = {
  Project     = "my-app"
  Environment = "dev"
  Owner       = "dev-team"
}
