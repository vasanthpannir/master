ctab = {"g1":"red",
        "g2":"blue",
        "g3":"green"
        }
stab = {
         "arun" : "blr-g1",
         "john" : "chn-g3",
         "manu" : "hyd-g2",
         "elan" : "trm-g1"
}

a = input("enter the name:\n")

if a in stab:
    print("City is", stab[a].split("-")[0])
    print("Color is",ctab[stab[a].split("-")[1]])

