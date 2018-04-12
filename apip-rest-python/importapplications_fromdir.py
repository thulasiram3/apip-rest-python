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
                  
def main(*mainargs):
    logging.basicConfig(filename='apip-session-{:%Y%m%d-%H%M%S}.log'.format(datetime.datetime.now()), filemode='w', format='%(asctime)s %(message)s', level=logging.DEBUG)    
    logging.info(sys.argv)
    if len(mainargs) == 0 : #if len(sys.argv)>1 and len(sys.argv)<5:
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
        parser = argparse.ArgumentParser(description='Import Applications into APICS by reading all json files in specified dirpath;')
        parser.add_argument('-cf','--configfile', dest='configfile', help='config file specifying server, auth, proxy and other details in json format;', default='apipcs_config.json', required=False)
        parser.add_argument('--dirpath', dest='dirpath', default='./', help='directory path; All json files from this directory will be imported', required=True)
        cmdargs = parser.parse_args()
        logging.info(cmdargs)
        serverargs = (cmdargs.configfile,)
        appdirpath = cmdargs.dirpath 
    elif len(mainargs) == 2: #REPL
        serverargs = mainargs[0]
        appdirpath = mainargs[1]
        #destdir = './'
        logging.info('Directory used for importapps= '+appdirpath)
       
    else:
        #Feature specific args parse
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
        numargs = len(mainargs)
        if numargs in  (3,4): pass
        else: raise TypeError("Number of arguments expected is 3 or 4 ; got {} !".format(numargs)) 
        serverargs = mainargs[0:3]
        appdirpath= mainargs[3:4][0] if numargs==4 else '.'

    found = None
    for jsonfile in findalljsonfiles(appdirpath): #Loop through all json files in CWD and import them
        found = 1
        logging.info('*** Processing json file {} found in current working directory '.format(jsonfile))
        apisvr = apipserver(serverargs)
        logging.info(jsonfile)
        apisvr.importapplication(jsonfile) #apisvr.importapi_stripartifacts(jsonfile) #todo use importapi when ready
    if not found: logging.info('No files to process in directory - {}'.format(appdirpath))     
    return 'success'
                         
def findalljsonfiles(appdirpath='./'): #generator func
    logging.info(appdirpath)
    try:
        for filename in os.listdir(path=appdirpath): 
            if filename.endswith('.json'): yield os.path.join(appdirpath, filename)
    except FileNotFoundError as fne:
        logging.info('Error - Incorrect location specified - {}'.format(appdirpath))
        logging.info('Root Cause - {}'.format(str(fne)))
    
if __name__ == "__main__": main() 




