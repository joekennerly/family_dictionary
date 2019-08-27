my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

# for key,value in my_family.items():
#     print(f"{value['name']} is my {key} and is {value['age']} years old")

# Comprehension version
{
    print(f"{value['name']} is my {key} and is {value['age']} years old") for key, value in my_family.items()
}