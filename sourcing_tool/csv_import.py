"""
This script imports csv files
"""
from csvkit.utilities.csvsql import CSVSQL
import os
from subprocess import Popen
import psycopg2

os.chdir("IPEDS_Data")

for file_name in os.listdir():
        tablename, ext = os.path.splitext(file_name)
        if ext == ".csv":
            args = \
            ["csvsql","--db","postgresql://wfa_demos:QVLqMejz@10.118.4.223:5432/sourcing","--table",tablename,"-e","LATIN1","--insert",file_path+"/"+file_name]
            print(args)
            Popen(args,shell=True)
            print("I finished " +tablename + "!!")
