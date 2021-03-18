# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 06:57:03 2020

@author: Remote
"""


import csv
import os
import pandas as pd
import numpy as np
import datetime as dt
import dateutil
from dateutil.parser import parse

filepath = 'G:/My Drive/PGE Frequency Response/Nan Script Test/'
file_list = os.listdir(filepath)
for i in file_list:
    fullfile = filepath+'/'+i
    print("Now processing " + fullfile + " .....")