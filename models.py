# creates a dictionary with all fluent Models

# ! NEEDS TO BE COMPLETED

# Declare Dictionary

models = {}

# Viscosity Models

models["Viscous"] = {
    "Laminar": "/define/models/viscous laminar\nyes",
    "ke-realizable": "/define/models/viscous ke-realizable\nyes\n/define/models/viscous/near-wall-treatment enhanced-wall-treatment\nyes\n",
}

# Radiation Models

models["Radiation"] = {
    "DO": "/define/models/radiation discrete-ordinates\nyes\n4\n4\n4\n4\n",
}

# Energy 

models["Energy"] = "/define/models energy\nyes\nno\nno\nno\nyes\n"
