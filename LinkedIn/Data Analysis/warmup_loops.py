import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

employees = [
    {"name": "John Mckee", "salary": 32000, "job_title": "Developer"},
    {"name": "Lisa Crawford", "salary": 44000, "job_title": "Manager"},
    {"name": "Sujan Patel", "salary": 33000, "job_title": "Developer"},
    {"name": "Ali Lee", "salary": 24000, "job_title": "Support Engineer"},
    {"name": "Ella Ruiz", "salary": 28000, "job_title": "Developer"},
]

dev_salaries = [
    employee["salary"] for employee in employees if employee["job_title"] == "Developer"
]
print(dev_salaries)

# ANAGRAMS
print([*"eleven plus two"])


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
