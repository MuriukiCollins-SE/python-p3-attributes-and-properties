#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        # Always check name first, but only if name is provided
        if name is not None and (not isinstance(name, str) or len(name) == 0 or len(name) > 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = None
            self.job = None
        elif job is not None and job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self.name = None
            self.job = None
        else:
            if name is not None:
                self.name = name.title()
            else:
                self.name = None
            if job is not None and job in APPROVED_JOBS:
                self.job = job
            else:
                self.job = None