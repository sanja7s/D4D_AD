'''
Created on Feb 21, 2013

@author: sscepano
'''

def calculate(data):
    
    file_name = "/home/sscepano/D4D res/AD/radiation_subprefs.tsv"
    f = open(file_name,"w")
    
    for subpref in range(1,256):
        for subpref2 in range(1,256):
            f.write(str(subpref) + '\t' + str(subpref2) + '\t' + str(data[subpref][subpref2][0]) + '\n')
    
    return