#!/usr/bin/python3

import os
import sys
import requests
import json
from textwrap import indent
from APIPCSmodule import apipserver
from pathlib import Path
import argparse
import datetime
import logging
from tabulate import tabulate
                  
def main(*mainargs):
    logging.basicConfig(filename='logs/apip-session-{:%Y%m%d-%H%M%S}.log'.format(datetime.datetime.now()), filemode='w', format='%(asctime)s %(message)s', level=logging.INFO)  
    #logging.getLogger('urllib3').setLevel(logging.CRITICAL)      
    logging.getLogger("requests.packages.urllib3").setLevel(logging.CRITICAL) 
      
    #logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    #logging.info(sys.argv)
    apiid= None
    if len(mainargs) == 0 : 
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout)) # move here else will keep adding logger every loop
        logging.getLogger('urllib3').setLevel(logging.CRITICAL)        
        parser = argparse.ArgumentParser(description='Lists all APIs from APICS and writes to console. Only writes to the console, use exportallapis to persist details in File system')
        parser.add_argument('-cf','--configfile', dest='configfile', help='config file specifying server, auth, proxy and other details in json format;', default='apipcs_config.json', required=False)
        cmdargs = parser.parse_args()
        logging.debug(cmdargs)
        serverargs = (cmdargs.configfile,)
    elif len(mainargs) == 1: #REPL
        serverargs = mainargs[0]
    else:
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout)) # move here else will keep adding logger every loop
        logging.debug(mainargs)
        numargs = len(mainargs)
        if numargs==3: pass
        else: raise TypeError("Number of arguments expected is 3; got {} !".format(numargs)) 
        serverargs = mainargs[0:3]
    apisvr = apipserver(serverargs)
    allapis = apisvr.retrieveall('api')()
    prettyprint(allapis)
    #logging.info(tabulate(allapis))
    #for apiid in loopapis(allapis): 
        #logging.info('*** API id - {}'.format(apiid))
        #pass
    return 'success'
        
def loopapis(allapis): #generator func
    for k,v in allapis.items():
        if k == "count": count=v
        if k == "items": 
            items=allapis[k]
            for element in items: 
                for m,n in element.items(): 
                    if m == 'id': yield n
    logging.info('***Found {} APIs defined on the apipcs server'.format(count))
 
def prettyprint(allapis): #generator func
   for k,v in allapis.items():
       if k == "count": count=v
       if k == "items": 
           items=allapis[k]
           for element in items: 
               logging.info(tabulate(element.items(), tablefmt="plain"))
   logging.info('***Found {} APIs defined on the apipcs server'.format(count))
 
if __name__ == "__main__": main()


