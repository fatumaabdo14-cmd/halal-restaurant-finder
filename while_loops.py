import random
import time 

def simulate_instance_state():
    states = ["pending",  "running"]
    return random.choice(states)

instance_state = "pending"
attempts =0 

while instance_state != "running" and attempts < 6:
    print(f"attempts {attempts + 1}: instance state is {instance_state}")
    instance_state = simulate_instance_state()
    attempts += 1
    time.sleep(1) # wait for 1 second between checks 
    
    if instance_state == "running":
        print("Instance is running.")
    else:
        print("instance did not start in time.")