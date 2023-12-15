# creates a dictionary with all fluent commands


models = {
    "Energy": "/define/models energy\nyes\nno\nno\nno\nyes\n",
    "Viscous": {
        "Laminar": "/define/models/viscous laminar\nyes",
        "ke-realizable": "/define/models/viscous ke-realizable\nyes\n/define/models/viscous/near-wall-treatment enhanced-wall-treatment\nyes\n",
    },
    "Radiation": {
        "DO": "/define/models/radiation discrete-ordinates\nyes\n4\n4\n4\n4\n",
    },
}
