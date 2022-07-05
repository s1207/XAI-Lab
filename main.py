from manimlib.scene.scene import Scene
from matplotlib.collections import PatchCollection

import family_parser
import geometry
import os
import pandas as pd
from manim import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

if __name__ == '__main__':
    os.chdir('data')
    df = pd.DataFrame(pd.read_csv('test_family_tree.csv'))
    circle_array = family_parser.parse_csv('test family tree.csv', df)
    family_parser.find_relations(circle_array, df)
    for member in circle_array[1].children:
        print(member.name)

    # print(circle_array[1].children[1].name)
    circles_list = []
    c_x = 1
    c_y = 1
    for person in circle_array:
        circle = plt.Circle((c_x, c_y), 0.5, color='b', fill=False)
        circles_list.append(circle)
        c_x += 1
        c_y += 1

    fig, ax = plt.subplots()
    ax = plt.gca()
    ax.cla()  # clear things for fresh plot

    # change default range so that new circles will work
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 10))

    for circle in circles_list:
        ax.add_patch(circle)

    fig.savefig('plotcircles2.png')
