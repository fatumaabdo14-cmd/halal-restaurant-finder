# for loops 

instance_ids = ["i-123456", "i 23456", "i-abcde1234"]
for instance_id in instance_ids:
    print(f"checking status of instance {instance_id}")
    # code to check instance status 
    print(f"instance{instance_id} status check complete")
    
print("all instances have been checked")