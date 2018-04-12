
API Platform Cloud Service REST API client using Python

This blog introduces a few useful Python scripts designed to repeatably perform some common administrative and development operations on an API Platform CS instance.
The scripts are written in Python and can be executed on all python supported platforms

Prerequisites
Requires Python version 3.6 and the requests module installed.
The API Platform Cloud Service REST API documentation is available here - @@link [INTERNAL]
The python scripts can be downloaded FROM here @@LINK

Usage information
Use --help to get the usage of every script
For example, python listapis.py --help
	==========
	['listapis.py', '--help']
	usage: listapis.py [-h] [-cf CONFIGFILE]

	Lists all APIs from APICS and writes to console. Only writes to the console,
	use exportallapis to persist details in File system

	optional arguments:
	  -h, --help            show this help message and exit
	  -cf CONFIGFILE, --configfile CONFIGFILE
							config file specifying server, auth, proxy and other
							details in json format;
	==========
All scripts accept a common config file as argument which contains the details required to connect to and authenticate against the 
API Platform Cloud service. the file is in json format and defaults to apipcs_config.json when not provided.
Here is an example of how the file would appear

	=======apipcs_config.json:
	{
		"server": "http://slc10ehk.us.oracle.com:7201/apiplatform" ,
		"auth": ["weblogic","welcome1"],
		"basedir": "C:/apip-python-base-dir"

	}
	===============
	
Additionally, proxy infomation can also be provided when a http/https proxy server is required to connect to the API platform Cloud Service
	===============
	{
		"server": "https://10.252.158.26/apiplatform" ,
		"auth": ["weblogic","welcome1"],
		"proxy": {
			"http": "www-proxy.us.oracle.com:80", 
			"https": "www-proxy.us.oracle.com:80"
		},
		"basedir": "/home/sraghura/APIPRESTAPI/json"

	}
	===============



Common Administrative Operations:

Exporting all APIs from an API Platform (exportallapis.py)
This script will export the metadata of all APIs defined in API platform Cloud Service.
The metadata in json format will be persisted within the destination directory specified in the client file system. 
In addition to the API metadata, the following additional artifacts are also fetched and persisted to the file system - 
	*API resources like files used to specify the Overview and Documentation content for APIs
	*API Grants that have been issued to every API
	*API Contracts associated with every API

	Usage:
	==========
	python exportallapis.py --help
	usage: exportallapis.py [-h] [-cf CONFIGFILE] [--destdir DESTDIR]

	This program exports all APIs and its associated artifacts from APICS and
	persist them on the file system

	optional arguments:
	  -h, --help            show this help message and exit
	  -cf CONFIGFILE, --configfile CONFIGFILE
							config file specifying server, auth, proxy and other otails in json format;
	  --destdir DESTDIR     directory path on local file system where all the 
							exported API artifacts will be saved to; defaults to
							current directory
	==========

Exporting all Applications from an API Platform (exportallapplications.py)
This script will export the metadata of all Applications created on API platform Cloud Service.
The metadata in json format will be persisted within the destination directory specified in the client file system. 
In addition to the Applications' metadata, the following additional artifacts are also fetched and persisted to the file system - 
	*Application registrations associated with every Application being exported
	
	usage:
	==============
	usage: exportallapplications.py [-h] [-cf CONFIGFILE] [--destdir DESTDIR]
	This program exports all Applications from APICS and persist them on the file system

	optional arguments:
	  -h, --help            show this help message and exit
	  -cf CONFIGFILE, --configfile CONFIGFILE
							config file specifying server, auth, proxy and other
							details in json format;
	  --destdir DESTDIR     directory path on local file system where all the exported Apps and artifacts will be saved to; 
							defaults to current directory
	==============


Exporting all Gateways from an API Platform (exportallgateways.py)
This script will export the metadata of all Gateways created on API platform Cloud Service.
The metadata in json format will be persisted within the destination directory specified in the client file system. 
In addition to the gateways' metadata, the following additional artifacts are also fetched and persisted to the file system - 
	*Gateway Grants that have been issued to every API
	*Gateway registrations associated with every gateway
	
	usage:
	==============
	usage: exportallgateways.py [-h] [-cf CONFIGFILE] [--destdir DESTDIR]
	This program exports all Gateways' metadata from APICS and persist them on the file system

	optional arguments:
	  -h, --help            show this help message and exit
	  -cf CONFIGFILE, --configfile CONFIGFILE
							config file specifying server, auth, proxy and other details in json format;
	  --destdir DESTDIR     directory path on local file system where all the
							exported gateway details will be saved to; defaults to current directory
	==============

Importing APIs into an API Platform (importapis_fromdir.py)
This script scans through all the API metadata jsons in a specified directory and creates them on the target API Platform server
The script also reads any resources referenced, like files used to specify the Overview and Documentation content from the same directory
 and includes their content when creating the API on the target API Platform server
Note that API grants and contracts are not used when importing. The new APIs will be created on target server with default grants and no contracts.

	Usage
	=============
	usage: importapis_fromdir.py [-h] [-cf CONFIGFILE] --dirpath DIRPATH

	Import APIs into APICS by reading all json files in specified dirpath;

	optional arguments:
	  -h, --help            show this help message and exit
	  -cf CONFIGFILE, --configfile CONFIGFILE
							config file specifying server, auth, proxy and other details in json format;
	  --dirpath DIRPATH     directory path; All json files from this directory will be imported
	=============
 

Importing Applications into an API Platform (importapplications_fromdir.py)
This script scans through all the Application metadata json files in a specified directory and creates them on the target API Platform server
Note that Application registrations will not be used when importing. The new Applications will be created on target server with no registrations.

	Usage
	==============
	usage: importapplications_fromdir.py [-h] [-cf CONFIGFILE] --dirpath DIRPATH

	Import Applications into APICS by reading all json files in specified dirpath;

	optional arguments:
	  -h, --help            show this help message and exit
	  -cf CONFIGFILE, --configfile CONFIGFILE
							config file specifying server, auth, proxy and other
							details in json format;
	  --dirpath DIRPATH     directory path; All json files from this directory
							will be imported
	==============

Other Utility commands
The script bundle comes with few other utiity commands which may be useful for administrative and developer tasks. Given below are brief overview of these scripts. Most of them are self describing. Use the command help by invoking --help for their usage details

•	listapis.py - lists all API IDs to the console. Note- nothing is persisted to file system
•	listapps.py -  lists Application IDs, Gateways defined on API Platform
•	listgateways.py -  lists Gateway IDs, Gateways defined on API Platform
•	export_api_byid - export one API by specifying its API ID
•	importapi.py -  import one API into APi Platform. Requires full path of API metadata json file
•	importapp.py -  import one Application into APi Platform. Takes full path of Application metadata json file as argument
•	deleteapi-py - deletes an API when ID specified; Deletes all APIs when no API ID is specified. Useful for cleanup of environment, use with caution.Note that it exports the APIs prior to deleting them.
•	deleteapplication.py - 	similar to deleteapi.py above. Useful for cleanup tasks. Use with caution

REPL interface

The scripts also provide an interactive REPL interface for some of the above operations. The REPL shell can be started by invoking the repl.py  and optionally passing the config file as below.

python repl.py  [-cf CONFIGFILE]

The REPL also takes the same common config file as argument as before which contains the details required to connect to and authenticate against the API Platform Cloud service. It defaults to apipcs_config.json when not provided.
	{
		"server": "https://10.252.158.26/apiplatform" ,
		"auth": ["weblogic","welcome1"],
		"proxy": {
			"http": "www-proxy.us.oracle.com:80", 
			"https": "www-proxy.us.oracle.com:80"
		}
}
bash-4.1$ python3 repl.py -cf apipcs_config.json
['repl.py', '-cf', 'apipcs_config.json']
Namespace(configfile='apipcs_config.json')
done initing repl
APIPCS: >

The following commands are available from the REPL prompt. All commands connect to and execute operations on the API Platform CS server specified in the config json file.

Listapis
Listgateways
Listapps

Exportallapis [--destdir <dirpath>]
Exportallapps [--destdir <dirpath>]
Exportallgateways [--destdir <dirpath>]

importapis_fromdir [--dirpath <dirpath>]
importapps_fromdir [--dirpath <dirpath>]

The commands are self explanatory and they perform the same functions as their script counterparts !

Here is a sample REPL session extract for easy reference

>python3 repl.py -cf apipcs_exportfrom.json
done initing repl
APIPCS: >
APIPCS: > help
Documented commands (type help <topic>):
========================================
help
Undocumented commands:
======================
exit exportallgateways listapis listplans
exportallapis importapis_fromdir listapps shree
exportallapps importapps_fromdir listgateways
APIPCS: >
APIPCS: >
APIPCS: >
APIPCS: > listapis
Reading Config from - apipcs_exportfrom.json
Using https://10.252.158.26/apiplatform ;{'https': 'www-proxy.us.oracle.com:80', 'http': 'www-proxy.us.oracle.com:80'} ;None
id 378 links [{'href': 'https://10.252.158.26:443/apiplatform/management/v1/apis/378', 'method': 'GET', 'templated': 'true', 'rel': 'canonical'}]
id 381 links [{'href': 'https://10.252.158.26:443/apiplatform/management/v1/apis/381', 'method': 'GET', 'templated': 'true', 'rel': 'canonical'}]
id 794 links [{'href': 'https://10.252.158.26:443/apiplatform/management/v1/apis/794', 'method': 'GET', 'templated': 'true', 'rel': 'canonical'}]
***Found 3 APIs defined on the apipcs server

Logs
All script files and the REPL sessions write to log files within the apip-rest-python/logs directory. The log levels are set to default within the script .py files and the repl.py as shown below. 
logging.basicConfig(filename='logs/repl-apip-session-{:%Y%m%d-%H%M%S}.log'.format(datetime.datetime.now()), filemode='w', format='%(asctime)s %(message)s', level=logging.INFO)

The log level can be increased to debug for more diagnostic information to be logged to the console and the log files.

--Shreeni

Disclaimer:
These scripts are provided “AS IS” and without any official support from Oracle. Their use needs to be performed using details from the comments section and/or readme file (if one is included). Any bugs encountered, feedback, and/or enhancement requests are welcome.
No liability for the contents of these scripts can be accepted. Use the concepts, examples, and information at your own risk. However, great care has been taken to ensure that all technical information is accurate and as useful as possible.
This is an evolving set of python scripts, it is not a good example of “pythonic” code. It is expected that anyone using this would customize and extend to their needs.

