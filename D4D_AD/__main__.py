'''
Created on Jan 14, 2013

@author: sscepano
'''
'''
Created on Nov 21, 2012

@author: sscepano
'''

# This one serves for reading in data in full --- for finding number of users, user homes etc
from collections import defaultdict
from multiprocessing import Pool
import logging
import numpy as n
import traceback
import networkx as nx

#####################################################
# diversity
#####################################################
from read_in import gravity_model as rd
from visualize import gravity_model as v
from analyse import gravity_model as a
#####################################################

_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')

    C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    #######################################################################
    # for reading in frequencies to compare to gravity model
    #######################################################################
    # defaultdict servers as matrix
    #######################################################################
    data = defaultdict(int)
    for subpref in range(256):
        data[subpref] = defaultdict(int)
        for subpref2 in range(256):
            data[subpref][subpref2] = defaultdict(int)

    old_usr = 0
    old_subpref = 0

    for c in C:
        data, old_usr, old_subpref = rd.read_in_file(c, data, old_usr, old_subpref)

    _log.info("Data loaded.")
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            reload(v)
            reload(a)
            #reload(s)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            new_data = a.calculate(data)
            v.plot(data, new_data)
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()