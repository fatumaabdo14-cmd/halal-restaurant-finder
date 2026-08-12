# dictionaries
# - store and review innformation 
# - key values

# ec2
ec2_instance ={
    "instance_id": "i-1234567890abcdef0",
    "instance_type": "t2.micro",
    "state": "running",
    "public_ip_address": "10.0.1.100",
}

instance_id = ec2_instance["instance_id"]
print(f"this is a {instance_id} instance")

public_ip = ec2_instance.get("public_ip_address", "no public ip address is here")
print(f"this instance has a public IP address is: {public_ip}")

# adding new key value pair
ec2_instance["availability_zone"] = "us-west-2a"
ec2_instance["state"] = "stopped"
print(ec2_instance)
 
 # using the pop 
rm_instannce_type = ec2_instance.pop("instance_type")
print(f"this is the removes instance type:{rm_instannce_type}")

# using del 
del ec2_instance["availability_zone"]
print(ec2_instance)






