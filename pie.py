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

labels = []
sizes = []
colors = []

with open( "./groups-struct.dat", "r" ) as fin:
    lines = fin.readlines()
    for i in lines:
        dat = i.replace("\n", "").split(":")
        Nodes.append( Node( label=dat[0], color=dat[1], size=dat[2] ) )


for node in Nodes:
    labels.append( node.get_label() )
    sizes.append( node.get_size() )
    colors.append( node.get_color() )

fig1, ax1 = plt.subplots() 
#wedges, texts = ax1.pie(sizes, explode=None, labels=None, colors=colors, autopct='%1.0f%%', wedgeprops=dict(width=0.5, edgecolor='black'))
wedges, pct, texts = ax1.pie(sizes, colors=colors, autopct='%1.1f%%', pctdistance=0.9, wedgeprops=dict(linewidth=0.1, width=0.5, edgecolor='black'), startangle=85)

ax1.set(aspect="equal")
#ax1.set_title("pie")

#bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
#kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
kw = dict(arrowprops=dict(arrowstyle="-"), zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    #ax1.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.5*y), horizontalalignment=horizontalalignment, **kw)
    ax1.annotate(labels[i], xy=(x, y), xytext=(1.45*np.sign(x), 1.5*y), horizontalalignment=horizontalalignment, **kw)

plt.show()
