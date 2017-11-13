'''A python module for capturing the Euclidean distance of a 2D TSP problem.'''

# meta block
__author__ = "Steven Porretta"
__version__ = "0.0.1"
__maintainer__ = "Steven Porretta"
__email__ = "stevenporretta@scs.carleton.ca"
__status__ = "Development"

import math as m


def dist(p1, p2):
    '''Calculate the Euclidean distance between two points p1(x1,y1) and
       p2(x2,y2).'''
    delta_x = float(p2[0]) - float(p1[0])
    delta_y = float(p2[1]) - float(p1[1])
    # return the integer ceiling of the distances to ensure that rounding does
    # not produce overlapping points.
    return int(m.ceil(m.sqrt((pow(delta_x, 2) + pow(delta_y, 2)))))
