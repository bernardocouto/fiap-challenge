# FIAP Challenge

## Arquitetura

![Arquitetura]('./documentations/images/architecture.jpg')

## AWS

### Terraform

Para utilização do Terraform será necessário criar um Bucket no AWS S3 com nome `fiap-challenge-terraform` para armazenamento dos arquivos `.tfstate`. Além da infraestrutura do AWS S3 utilizaremos também uma tabela do AWS DynamoDB com o nome `fiap-challenge-terraform` e *Partition Key* com nome `LockID` do tipo String para garantia do Lock da execução do Terraform.
