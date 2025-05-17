#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        if breed is not None and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        elif not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name

        if breed is not None and breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            self.breed = None

