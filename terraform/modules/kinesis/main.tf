resource "aws_kinesis_stream" "fiap_challenge_stream" {
  name = "fiap-challenge-stream-${var.environment}"
}
