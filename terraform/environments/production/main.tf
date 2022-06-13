module "kinesis" {
  environment = var.environment
  source      = "../../modules/kinesis"
}

module "s3" {
  environment = var.environment
  source      = "../../modules/s3"
}
