"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {"Name":"Jill","Age": 26,"Job":"Biologist","Connections":[]},
    {"Name":"Zalika","Age": 28,"Job":"Artist","Connections":[]},
    {"Name":"John","Age": 27,"Job":"Writer","Connections":[]},
    {"Name":"Nash","Age": 34,"Job":"Chef","Connections":[]},
    ]

my_group[0]["Connections"] = [(my_group[2],"Patner")] # Jill and John
my_group[0]["Connections"].append((my_group[1],"Friend")) # Jill and John


