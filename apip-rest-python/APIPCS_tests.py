#!/usr/bin/python3

#from importapi import main as othermain
import APIPCSmodule
import export_api_byid
import importapis_fromdir
import importapi
import unittest
import exportallapis
import listapis
import listapps
import listplans
import exportallapplications
import exportallgateways
import importapis_fromdir
import deleteapi
import deleteapplication
import importapplications_fromdir

class test_importapi(unittest.TestCase):

    def test_import_by_id(self):
        pass

    # ------------API ----------------#
    
    def test_exportallapis(self):
        httpcode = exportallapis.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")
        self.assertEquals(httpcode, 'success')

    def test_exportapibyid(self):
        result = export_api_byid.main("http://slc10ehk:7201/apiplatform", "weblogic", "welcome1", "103")
        #localjsonfiles=[]
        #for jsonfile in importapis_fromdir.findalljsonfiles('./'):
        #    localjsonfiles.append(jsonfile)
        #self.assertIn('api-details-{}.json'.format('103'), localjsonfiles)
        self.assertEquals(result, 'success')

    def test_importapi(self):
        httpcode = importapi.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1", "api-details-100.json")
        self.assertEquals(httpcode, 'success')

    def test_deleteapi(self):
        res = deleteapi.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")
        self.assertEquals(res, 'deleted')
        
    def test_importapis_fromdir(self):
        res = importapis_fromdir.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1", 'apip-apis-for-import')
        self.assertEquals(res, 'success')

    def test_listapis(self):
        res = listapis.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")
        self.assertEquals(res, 'success')
        
    # ------------Apps ----------------#
    
    def test_exportallapplications(self):
        httpcode = exportallapplications.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")
        self.assertEquals(httpcode, 'success')

    def test_deleteapplication(self):
        res = deleteapplication.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")
        self.assertEquals(res, 'deleted')
    
    def test_importapplications_fromdir(self):
        res = importapplications_fromdir.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1", 'apip-apps-for-import')
        self.assertEquals(res, 'success')

    def test_listapps(self):
        res = listapps.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")
        self.assertEquals(res, 'success')

    # ------------Misc ----------------#
        
    def test_exportallgateways(self):
        httpcode = exportallgateways.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")
        self.assertEquals(httpcode, 'success')


    def test_listplans(self):
        res = listplans.main("http://slc10ehk.us.oracle.com:7201/apiplatform", "weblogic", "welcome1")
        self.assertEquals(res, 'success')


if __name__ == '__main__': unittest.main()




