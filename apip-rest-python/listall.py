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
    logging.basicConfig(filename='logs/apip-session-{:%Y%m%d-%H%M%S}.log'.format(datetime.datetime.now()), filemode='w', format='%(asctime)s %(message)s', level=logging.DEBUG)    
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.info(sys.argv)
    item= None
    if len(mainargs) == 0 : 
        parser = argparse.ArgumentParser(description='Lists all Applications from APICS and writes to console. Only writes to the console, use exportallapps to persist details in File system')
        parser.add_argument('-cf','--configfile', dest='configfile', help='config file specifying server, auth, proxy and other details in json format;', default='apipcs_config.json', required=False)
        parser.add_argument('-i','--item', dest='item', help='type of artifacts (api, plan, application, gateway..) to be exported', required=True )

        cmdargs = parser.parse_args()
        logging.info(cmdargs)
        serverargs = (cmdargs.configfile,)
        item=cmdargs.item
    else:
        logging.info(mainargs)
        numargs = len(mainargs)
        if numargs==4: pass
        else: raise TypeError("Number of arguments expected is 4; got {} !".format(numargs)) 
        serverargs = mainargs[0:3]
        item = mainargs[3:4][0]
    apisvr = apipserver(serverargs)
    listitems = apisvr.listall(item)()
    return 'done'
    
#if __name__ == "__main__": main()
if __name__ == "__main__": main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1", "plan")



