#!/usr/bin/env python3

import os,sys

import numpy as np
import matplotlib.pyplot as plt

class Node( object ):
    def __init__( self, label, color, size ):
        self.label = label
        self.color = color
        self.size = size

    def get_label( self ):
        return self.label

    def get_color( self ):
        return self.color

    def get_size( self ):
        return self.size

    
Nodes = []

sizes = []
colors = []

with open( "./groups-struct.dat", "r" ) as fin:
    lines = fin.readlines()
    for i in lines:
        dat = i.replace("\n", "").split(":")
        Nodes.append( Node( label=dat[0], color=dat[1], size=dat[2] ) )

colacc = ""
for node in Nodes:
    if colacc == node.color:
        sizes[-1] = str(int(sizes[-1]) + int(node.size))
    else:
        colacc = node.color
        colors.append(node.color)
        sizes.append(node.size)

fig1, ax1 = plt.subplots() 
#wedges, texts = ax1.pie(sizes, explode=None, labels=None, colors=colors, autopct='%1.0f%%', wedgeprops=dict(width=0.5, edgecolor='black'))
wedges, pct, texts = ax1.pie(sizes, colors=colors, autopct='%1.1f%%', pctdistance=0.7, wedgeprops=dict(linewidth=0.5, width=0.5, edgecolor='black'), startangle=85)

ax1.set(aspect="equal")

labels = [ 'Climate change', 'Animals extinction', 'Resources depletion', 'Pollution', 'Social', 'Other' ]

ax1.legend(wedges, labels,
          title="Problems",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

ax1.set_title("Categories of global problems")


plt.show()
