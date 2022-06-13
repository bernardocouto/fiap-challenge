resource "aws_s3_bucket" "fiap_challenge_bronze" {
  acl    = "private"
  bucket = "fiap-challenge-bronze-${var.environment}"
  versioning {
    enabled = false
  }
}

resource "aws_s3_bucket" "fiap_challenge_landing" {
  acl    = "private"
  bucket = "fiap-challenge-landing-${var.environment}"
  versioning {
    enabled = false
  }
}

resource "aws_s3_bucket" "fiap_challenge_silver" {
  acl    = "private"
  bucket = "fiap-challenge-silver-${var.environment}"
  versioning {
    enabled = false
  }
}
