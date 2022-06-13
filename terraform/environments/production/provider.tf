provider "aws" {
  default_tags {
    tags = {
      Project    = "fiap-chanllenge"
      Stage      = var.environment
      Terraform  = true
    }
  }
  region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket         = "fiap-chanllenge-terraform"
    key            = "fiap-chanllenge.tfstate"
    region         = "us-east-1"
    dynamodb_table = "fiap-chanllenge-terraform"
  }
}
