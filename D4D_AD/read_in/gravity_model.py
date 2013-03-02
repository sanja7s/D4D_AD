'''
Created on Feb 21, 2013

@author: sscepano
'''
from os.path import isfile, join
from collections import defaultdict
import networkx as nx
from datetime import datetime, date

# read in each movement between the subprefs or inside the same
# as a commuting. it must be unique users we count
# atm we count for two weeks, 10 times and average
def read_in_file(c, data, old_usr, old_subpref):
    
    i = 0
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                subpref = int(subpref)
                if subpref <> -1:
                    # for the same user we know last location
                    if usr == old_usr:
                        # so we record the movement (if already there, nothing)
                        data[old_subpref][subpref][usr] = 1
                    else:
                        # otherwise remember new user
                        # we lose some movements in this way, but according how data
                        # is sorted by single user movements, it is fine
                        # actually because we count on 2-weeks and average, we do not loose anything
                        old_usr = usr
                        old_subpref = subpref
    
    # here we after reading whole two weeks file save values of distinct users
    # who travelled between each two places in position [0] from data
    for subpref in range(256):
        for subpref2 in range(256):
            data[subpref][subpref2][0] += sum(data[subpref][subpref2].values()) 
    
    # test
    print data[200][100][0]
    print data[60][55][0]
    print data[120][77][0]
            
    print i            
    return data, old_usr, old_subpref