#!/usr/bin/python3

import os
import sys
import requests
import json
#from textwrap import indent
from APIPCSmodule import apipserver
#from pathlib import Path
import argparse
import datetime
import logging
                  
def main(*mainargs):
    logging.basicConfig(filename='logs/apip-session-{:%Y%m%d-%H%M%S}.log'.format(datetime.datetime.now()), filemode='w', format='%(asctime)s %(message)s', level=logging.DEBUG)    
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.info(sys.argv)
    apiid= None
    if len(mainargs) == 0 : 
        parser = argparse.ArgumentParser(description='Lists all APIs from APICS and writes to console. Only writes to the console, use exportallapis to persist details in File system')
        parser.add_argument('-cf','--configfile', dest='configfile', help='config file specifying server, auth, proxy and other details in json format;', default='apipcs_config.json', required=False)
        cmdargs = parser.parse_args()
        logging.info(cmdargs)
        serverargs = (cmdargs.configfile,)
    else:
        logging.info(mainargs)
        numargs = len(mainargs)
        if numargs==3: pass
        else: raise TypeError("Number of arguments expected is 3; got {} !".format(numargs)) 
        serverargs = mainargs[0:3]
    apisvr = apipserver(serverargs)
    allapis = apisvr.retrieveall('api')()
    for apiid in loopapis(allapis): 
        logging.warn('*** API id - {}'.format(apiid))
        
def loopapis(allapis): #generator func
    for k,v in allapis.items():
        if k == "count": count=v
        if k == "items": 
            items=allapis[k]
            for element in items: 
                for m,n in element.items(): 
                    if m == 'id': yield n
    logging.info('***Found {} APIs defined on the apipcs server'.format(count))
 
 
if __name__ == "__main__": main()
#if __name__ == "__main__": main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")



