import random

servers = [
    ('Server 1', 0.25),  
    ('Server 2', 0.30),  
    ('Server 3', 0.10),  
    ('Server 4', 0.35)   
]

def select_server(servers):
    rand_num = random.random() 
    cumulative_prob = 0.0
    
    for server, percentage in servers:
        cumulative_prob += percentage
        if rand_num < cumulative_prob:
            return server

while True:
    input("Press any key :")
    selected_server = select_server(servers)
    print(f"Selected Server: {selected_server}")
