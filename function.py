#import random

# def generate_bucket_name(project_name):
    # random_suffix = random.randint(1000, 9999)
   # bucket_name = f"{project_name}-bucket-{random_suffix}"
    # return bucket_name

# using the function 
# new_bucket = generate_bucket_name("myproject")
# print(f"created new s3 bucket: {new_bucket}")




import random

def generate_bucket_name(project_name):
    random_suffix = random.randint(1000, 9999)
    bucket_name = f"{project_name}-bucket-{random_suffix}"
    return bucket_name
    
    
new_bucket = generate_bucket_name("myproject")
print(f"created new s3 bucket: {new_bucket}")
