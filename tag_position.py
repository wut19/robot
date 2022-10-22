import numpy as np

def load_config(r1,rx,ry):
    tag_positions = {}
    sftx = np.array([rx, 0, 0])
    sfty = np.array([0, ry, 0])
    tag_positions['0'] = np.array([
    [0, 0, 0],
    [r1, 0, 0],
    [r1, r1, 0],
    [0, r1, 0],
    ])
    tag_positions['1'] = tag_positions['0'] + sftx
    tag_positions['2'] = tag_positions['1'] + sfty
    tag_positions['3'] = tag_positions['0'] + sfty
    tag_positions['4'] = tag_positions['0'] + np.array([rx/2, 0,0])+np.array([0, ry/2, 0])
    destination = tag_positions['4'][0, :2] + np.array([r1/2, r1/2])
    return tag_positions, destination
tag_positions, destination = load_config(5.00, 76.5, 74.7)  
