#!/usr/bin/env python3

def array_of_names(people):
    names = []
    for first,last in people.items():
        name = f"{first.capitalize()} {last.capitalize()}"
        names.append(name)
    return names
    
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))