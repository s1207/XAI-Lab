from collections import defaultdict

from manimlib.mobject.geometry import Circle

import circle
import pandas as pd
import os
from manimlib import *

os.chdir('data')
df = pd.DataFrame(pd.read_csv('small_family_tree.csv'))


def parse_csv(filename, dframe):
    temp = pd.concat([dframe['Name1'], dframe['Name2']]).unique()
    test_array = []
    for name in temp:
        test_array.append(circle.Circle(name))
    return test_array


def find_relations(circles_array, df):
    for member in circles_array:
        #member.relations = defaultdict(list)
        relations = df[df['Name1'] == member.name]
        print(relations.shape)
        member.children = [x for x in circles_array if (x.name == df['relation' == 'child'] and x.name == df['Name2'])]

    return None


circle_array = parse_csv('small family tree.csv', df)
find_relations(circle_array, df)

def initialize_circles(circles_array):
    initial_circle = Circle(2.5)
    return None


initialize_circles(circle_array)
