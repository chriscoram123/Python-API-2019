import flask 
from flask import request, jsonify
import matlibplot.pyplot as plt
import numpy as np
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:23:51 2019

@author: christophercoram
"""
# API that gathers class data frm user inout, then displays outputs on application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Test data for catalog in the form of 2D charts
# plot variables
N = 5
dataOne = (20, 40, 17, 4, 8)
ind = np.arange(N)
width = 0.15
class Charts():
	def __init__(self, ):

		
	def chartData(self):
	 # Plotting Variables
     p1 = plt.bar(ind, dataOne, width)
     
     plt.title("Plot Examples")
     plt.ylabel("Y Examples")
     plt.xlabel("X Examples")
     plt.xticks(ind, ('Example1','Example2','Example3','Example4','Example5'))
     plt.yticks(np.arange(0, 50, 20))
     plt.legend((p1[0], ('Examples')))
     plt.show()