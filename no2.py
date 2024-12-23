"""Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give
them options. If vegetarian, ask if they want "Salad" or "Pasta". If non-vegetarian, ask
if they want "Chicken" or "Fish".Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give
them options. If vegetarian, ask if they want "Salad" or "Pasta". If non-vegetarian, ask
if they want "Chicken" or "Fish"."""
a=input(" ae you vegetarian or non-vegetarian ")
if a=="veg":
    b=input(" salad ki pasta ")
    if b=="salad":
        print(" you are served sallad")
    elif b=="paata":
        print ("u are served pasta")
    else :
        print (" erreor ")
elif a=="nonveg":
    b=input (" chivken ki fish")
    if b=="chicken":
        print =(" ypu got chicekn")
    elif b=="fish":
        print("u got maccha")
    else :
        print(" correct van")
else :
    print (" veg or nn veg ")

