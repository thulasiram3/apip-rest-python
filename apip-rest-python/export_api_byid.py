#!/usr/bin/python3

import sys
import requests
import json
from test import test_getargs2
from pathlib import Path
from exportallapis import apipserver
import argparse
import datetime
import logging
                  
def main(*mainargs):
    logging.basicConfig(filename='logs/apip-session-{:%Y%m%d-%H%M%S}.log'.format(datetime.datetime.now()), filemode='w', format='%(asctime)s %(message)s', level=logging.DEBUG)    
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.info(sys.argv)
    if len(mainargs) == 0 : #if len(sys.argv)>1 and len(sys.argv)<5:
        parser = argparse.ArgumentParser(description='This program exports a single API from APICS using the apiid and persists to the file system')
        parser.add_argument('-cf','--configfile', dest='configfile', help='config file specifying server, auth, proxy and other details in json format;', default='apipcs_config.json', required=False)
        parser.add_argument('--apiid', dest='apiid', help='api-id of the api to be exported', required=True)
        cmdargs = parser.parse_args()
        
        logging.info(type(cmdargs))
        logging.info(cmdargs)
        #Feature specific args parse
        #serverargs = (cmdargs.server, cmdargs.user, cmdargs.passwd)
        serverargs = (cmdargs.configfile,)
        logging.info(serverargs) 
        api_id = cmdargs.apiid   #default CWD
        logging.info(api_id)
            
    else:
        logging.info(type(mainargs))
        #Feature specific args parse
        numargs = len(mainargs)
        logging.info(numargs)
        if numargs == 4: pass
        else: raise TypeError("Number of arguments expected is 4 ; got {} !".format(numargs)) 
        serverargs, api_id = mainargs[0:3], mainargs[3:4][0]
        logging.info(serverargs)
        logging.info(api_id)
            
    apisvr = apipserver(serverargs)
    apisvr.persistdetails(api_id, 'api')
    return 'success'
    
                  
if __name__ == "__main__": main()



