import parser
import geometry
import os
import pandas as pd
from manimlib import *

if __name__ == '__main__':
    os.chdir('data')
    df = pd.DataFrame(pd.read_csv('small_family_tree.csv'))
    circle_array = parser.parse_csv('small family tree.csv', df)
    parser.find_relations(circle_array, df)
    #print(circle_array[1].children[1].name)
    geometry()
