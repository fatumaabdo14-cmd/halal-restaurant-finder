# list of EC2 instance 
# instance_ids = ["i-1234567890abcdef0", "i-0987654321fedcba0", "i-1122334455667788"]
# list of IP addresses
# IP addresses for a security group
# ip_addresses = ["10.0.1.100", "10.0.1.101", "10.0.1.102", "10.0.1.104"]
# list of availablity zones in a region
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

# print the lists
# print("EC2 Instance IDs:", instance_ids)
# print("IP Addresses:", ip_addresses)
print("Availability Zones:", availability_zones)

# Add a new ec2 id 
#ninstance_ids.append("i-2233445566778899")

# print("after adding a new instance id")

# print ("EC2 Instance IDs:", instance_ids)


# remove ec2 instance id 
# instance_ids.remove("i-0987654321fedcba0")
# print ("after removing an instance id")
# print ("EC2 Instance IDs:", instance_ids)

# check if an item is in the list 

# if "10.0.1.104" in ip_addresses:
   # print("yes, 10.0.1.104 is in the list")
# else:
   # print("no, 10.0.1.104 is not in the list")
    # print("IP Addresses:", ip_addresses)
    
# slicing a list
# first two AZ
# first_two_az = availability_zones[:2]
# print("First two availability zones:", first_two_az)

# sorting a list
# instance_ids.sort()
# print("Sorted EC2 Instance IDs:", instance_ids)

# finding the length of a list
# number_of_ip_addresses = len(ip_addresses)
# print("number of ip addresses:", len(ip_addresses))
  
# accessing list of items by index 
first_az = availability_zones[0]
last_az = availability_zones[-1]
print("First Availability Zone:", first_az)
print("Last Availability Zone:", last_az)




    
    

