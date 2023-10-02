import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_bank(self):
        '''
            Test case written to test the list banks view. Checks the status code returned and no. of banks returned 
            by the request against the number available in our database.
        '''
        r = self.client.get('/api/get-banks/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 170)

    def test_branch(self):
        ''' Test Case written for returning branches by ifsc code. Checks the json returned by the request against
            the data available in our database
        '''
        r = self.client.get('/api/get-branch-by-ifsc/ABHY0065002/?format=json')
        data = {
                "ifsc": "ABHY0065002",
                "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
                "branch": "ABHYUDAYA NAGAR",
                "address": "ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033",
                "city": "MUMBAI",
                "district": "GREATER MUMBAI",
                "state": "MAHARASHTRA",
                "bank_id": 60
            }
        self.assertEqual(r.json(),data)


    