from collections import defaultdict

from manimlib.mobject.geometry import Circle

import circle
import pandas as pd
import os
from manimlib import *


def parse_csv(filename, dframe):
    temp = pd.concat([dframe['Name1'], dframe['Name2']]).unique()
    test_array = []
    for name in temp:
        test_array.append(circle.Circle(name))
    return test_array


def find_relations(circles_array, dframe):
    for member in circles_array:
        relations = dframe[dframe['Name1'] == member.name]
        #print(relations)
        member.children = {x for x in circles_array if x.name in
                           relations[relations['relation'] == 'child']['Name2'].tolist()}
        member.spouses = {x for x in circles_array if x.name in
                          relations[relations['relation'] == 'spouse']['Name2'].tolist()}
        member.parents = {x for x in circles_array if x.name in
                          relations[relations['relation'] == 'parent']['Name2'].tolist()}
    return None

def initialize_circles(circles_array):
    initial_circle = Circle(2.5)
    return None


#initialize_circles(circle_array)
