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
        # print(relations)
        member.children = {x for x in circles_array if x.name in
                           relations[relations['relation'] == 'child']['Name2'].tolist()}
        member.spouses = {x for x in circles_array if x.name in
                          relations[relations['relation'] == 'spouse']['Name2'].tolist()}
        member.parents = {x for x in circles_array if x.name in
                          relations[relations['relation'] == 'parent']['Name2'].tolist()}
    return None


def initialize_circles(circles_array):
    step = 0.5
    for person in circles_array:
        person.radius = 0.5
        person.xCoordinate = step
        person.yCoordinate = 1
        step += 2 * person.radius
    return None


def adjust_circles_for_spouses(person):
    c_x = person.xCoordinate
    c_y = person.yCoordinate
    for spouse in person.spouses:
        spouse.xCoordinate = c_x + person.radius
        spouse.yCoordinate = c_y
    return c_x, c_y


def adjust_circles_for_children(person):
    c_x = person.xCoordinate
    c_y = person.yCoordinate
    for child in person.children:
        child.xCoordinate = c_x + list(person.spouses)[0].xCoordinate if len(list(person.spouses)) > 0 else child.xCoordinate
        child.yCoordinate = c_y
        child.radius = person.radius / 2
    return c_x, c_y
