# define the aws account ID 
aws_account_id = '123456789012'

# define the aws account ID
project_name = " cloud_project"

# concatenate strings to form the s3 bucket name
bucket_name = aws_account_id + "-" + project_name + "-bucket" 


# print the resulting bucket name
print("The S3 bucket name is:", bucket_name)


# execise ec2 string concatenation
 
# environment name pro, dev, staging 
environment_name = "dev"
# application name 
application_name = "my_app"
# instance type
instance_number = "02"
# concatenate 
instance_name = environment_name + "-" + application_name + "-" + "instance-" + instance_number
# print 
print("The EC2 instance name is:", instance_name)