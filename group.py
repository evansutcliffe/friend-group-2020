"""An example of how to represent a group of acquaintances in Python."""

my_group = [
    {"Name":"Jill","Age": 26,"Job":"Biologist","Connections":[]},
    {"Name":"Zalika","Age": 28,"Job":"Artist","Connections":[]},
    {"Name":"John","Age": 27,"Job":"Writer","Connections":[]},
    {"Name":"Nash","Age": 34,"Job":"Chef","Connections":[]},
    ]


#Jill's connections
my_group[0]["Connections"] = [(my_group[2],"Partner")] # Jill and John
my_group[0]["Connections"].append((my_group[1],"Friend")) # Jill and Zalika

#Zalika's connections
my_group[1]["Connections"] = [(my_group[0],"Friend")] # Zalika and Jill

#John's Connections
my_group[2]["Connections"] = [(my_group[0],"Partner")] #John and Jill

#Nash's Connections
my_group[3]["Connections"] = [(my_group[2],"Cousin")]
my_group[3]["Connections"].append((my_group[1],"Landlord"))

tot_ages = []
tot_ages_conns = []
tot_ages_friends = []
tot_conns = []


for person in my_group:
    
    n_conns = len(person['Connections'])
    
    tot_ages.append(person['Age'])
    tot_conns.append(n_conns) #number of connections
    n_friends = 0 #intialise number of friends to 0
    
    #Pick out only people with more than one connection
    if n_conns >= 1:
        tot_ages_conns.append(person['Age'])
        
        #Loop over the connections to see how many friends people have
        for conn in person['Connections']:
            if conn[1] == 'Friend':
                n_friends =+ 1
    
        if n_friends >= 1 :
            tot_ages_friends.append(person['Age'])

print('Maximum age = ' + str(max(tot_ages)))
print('Average connections = ' + str(sum(tot_conns)/len(tot_conns)))
print('Maximum age of people with at least one connection = ' + str(max(tot_ages_conns)))
print('Maximum age of people with at least one friend = ' + str(max(tot_ages_friends)))

import yaml

with open('my_group.yaml', 'w') as f:
    
    data = yaml.dump(my_group, f)
    
a_yaml_file = open("my_group.yaml")
parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
print(parsed_yaml_file[1]['Name'])
