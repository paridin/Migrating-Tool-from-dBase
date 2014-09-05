# -*- coding: utf-8 -*-
# In a future you can use this tool in python 3.x
from __future__ import print_function
# This Tool is used to migrate from dBase to ORM in DJANGO
# Create on 04/Sep/14
# Last update on
# Contact roberto.estrada.ext@sicam.mx; restrada@paridin.com
# Depends Libs ['dbfpy-2.3.0 or above',]
__author__ = 'Roberto Estrada'
__version__ = "$Revision: e98737176f1d $"
# $Source$
import os
import sys
from dbfpy import dbf

class MigrationFromDBase:
    '''
        This class works for migrate the dBase to orm django
        actually tested only on pypy
    '''
    '''
     Configure section
     TABLES_DIR Specifies the path of the current directory
    '''
    TABLES_PATH = ('/').join(os.path.abspath(__file__).split('/')[0:-1]) + '/tables'

    def fetch_dbase_table(self, table, keys, path=None):
        ''' Fetches rows from a dBase Table

        Retrieves rows pertaining to the given keys from the Table instance

        :param table:  the name of the table
        :param keys: the list of keys
        :param path: Optional value, if you don't specify this value
         it will take it the default TABLES_PATH
        :return list: Return a list with internal dictionary
        '''
        if not path is None:
            if os.path.isdir(path):
                if path[-1] == '/':
                    self.TABLES_PATH = path[0:-1]
                else:
                    self.TABLES_PATH = path
            else:
                self.error(-1)
        db = dbf.Dbf("%s/%s" % (self.TABLES_PATH, table))
        dbase = []
        for r in db:
            for k in keys:
                dbase.append({k: r[k]})
        return dbase


    def fetch_dbase_keys(self, table):
        ''' Fetches keys from a dBase Table

        Retrieves keys pertaining to the given table from the instance

        :param table:  the name of the table
        :return list: Return a list with keys from the table
        '''
        db = dbf.Dbf("%s/%s" % (self.TABLES_PATH, table))
        dbase_keys = []
        for r in db.fieldNames:
            dbase_keys.append(r)
        return dbase_keys


    def set_path(self, path):
        self.TABLES_DIR = path

    def error(self,id):
        if id == -1:
            error = "Error the path is not a directory"

# Testing tool
if __name__ == '__main__':
    m = MigrationFromDBase()
    # specify path
    menus = m.fetch_dbase_table('ACCMENU.DBF', ['NOMBRE'], '/Volumes/home/paridin/Devel/python/ppm/migrations/')
    for menu in menus:
        print (menu['NOMBRE'])

    keys = m.fetch_dbase_keys('ACCMENU.DBF')
    print (keys)
