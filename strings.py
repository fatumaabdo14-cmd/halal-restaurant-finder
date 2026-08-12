# single quote string
single_quote_string = 'This is a single quote string.'

double_quote_string = "This is a double quote string."

triple_single_quote_string = '''This is a triple single quote string.'''

print(single_quote_string)
print(double_quote_string)
print(triple_single_quote_string)

# exercise
aws_region = 'us-east-1'

ec2_instance_type ="t2.micro"

# multi-line string
iam_policy = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example_bucket"
        }
    ]
}"""
print (aws_region)
print (ec2_instance_type)
print (iam_policy)
    