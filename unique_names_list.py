# The function receives a list that contains the first and last names of people in the form of tuples.
# The output is a list where all firstnames are unique. When the original list contains duplicated firstnames, any
# of the people with the firstname can be returned in the modified output.

# less time complexity
import random


def get_unique_first_names(list_input):
    names_collection = {}

    for info in list_input:
        if info[0] not in names_collection:
            names_collection[info[0]] = []

        names_collection[info[0]].append(info[1])

    modified_list = [(key, random.choice(value)) for key, value in names_collection.items()]

    return modified_list

# print(get_unique_first_names(
#         [
#             ("John", "Doe"),
#             ("Jane", "Doe"),
#             ("Emily", "Clark"),
#             ("Michael", "Smith"),
#             ("Sarah", "Johnson"),
#             ("James", "Williams"),
#             ("John", "Wilson"),
#             ("David", "Brown"),
#             ("Michael", "Davis"),
#             ("Emily", "Martinez"),
#             ("Emma", "Garcia"),
#             ("James", "Taylor"),
#             ("Olivia", "Anderson"),
#             ("Sophia", "Thomas"),
#             ("William", "Jackson"),
#             ("Michael", "White"),
#         ]
#     )
# )
