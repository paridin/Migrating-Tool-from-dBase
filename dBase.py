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
from dbfpy import dbf

'''
 Configure section
 RUN_DIR Specifies the path of the current directory
'''
RUN_DIR = ('/').join(os.path.abspath(__file__).split('/')[0:-1])

class MigrationFromDBase:
    '''
        This class works for migrate the dBase to orm django
        actually tested only on pypy
    '''
    def fetch_dbase_table(self, table, keys):
        ''' Fetches rows from a dBase Table

        Retrieves rows pertaining to the given keys from the Table instance

        :param table:  the name of the table
        :param keys: the list of keys
        :return list: Return a list with internal dictionary
        '''
        db = dbf.Dbf("%s/tables/%s" % (RUN_DIR, table))
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
        db = dbf.Dbf("%s/tables/%s" % (RUN_DIR, table))
        dbkeys = []
        for r in db.fieldNames:
            dbkeys.append(r)
        return dbkeys

# Testing tool
if __name__ == '__main__':
    m = MigrationFromDBase()
    menus = m.fetch_dbase_table('ACCMENU.DBF', ['NOMBRE'])
    for menu in menus:
        print (menu['NOMBRE'])

    keys = m.fetch_dbase_keys('ACCMENU.DBF')
    print (keys)
