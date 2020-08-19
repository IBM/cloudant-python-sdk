from ibmcloudant.cloudant_v1 import CloudantV1
import os
import unittest

# Read config file
configFile = 'cloudant.env'
configLoaded = None

if os.path.exists(configFile):
    os.environ['IBM_CREDENTIALS_FILE'] = configFile
    configLoaded = True
else:
    print('External configuration was not found, skipping tests...')

class TestIntegration(unittest.TestCase):
    def setUp(self):
        if not configLoaded:
          self.skipTest("External configuration not available, skipping...")
          
        self.cloudant = CloudantV1.new_instance(service_name='SERVER')
        self.db_name = os.environ.get('DATABASE_NAME', 'stores')
        self.assertIsNotNone(self.cloudant)
        self.assertIsNotNone(self.db_name)

    def test_server_information(self):
        response = self.cloudant.get_server_information()
        self.assertIsNotNone(response)
        result = response.get_result()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result['couchdb'])
        self.assertIsNotNone(result['version'])

    def test_head_database(self):
        response = self.cloudant.head_database(self.db_name)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.get_headers())
        self.assertTrue(len(response.get_headers()) > 0)

    def test_all_docs(self):
        response = self.cloudant.post_all_docs(self.db_name)
        self.assertIsNotNone(response)
        result = response.get_result()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result['rows'])
        self.assertTrue(len(result['rows']) > 0)
