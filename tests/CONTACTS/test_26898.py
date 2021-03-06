#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *
import time

#
# Imports particular to this test case.
#
from tests._mock_data.contacts import MockContacts

class test_main(GaiaTestCase):
    

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = Contacts(self)
        
        #
        # Prepare the contact.
        #
        self.cont = MockContacts().Contact_1

    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Launch contacts app.
        #
        self.contacts.launch()

        #
        # Create the contact.
        #
        self.contacts.startCreateNewContact()        
        contFields = self.contacts.getContactFields()
        self.contacts.replaceStr(contFields['givenName'  ] , self.cont["givenName"])
        self.contacts.replaceStr(contFields['familyName' ] , self.cont["familyName"])
        
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screenshot at this point", x)

        x = self.UTILS.getElement(DOM.Contacts.done_button, "Done button")
        x.tap()
        
        self.contacts.viewContact(self.cont["name"])
        
        time.sleep(1)
        self.UTILS.waitForNotElements( ("xpath", "//h2[text()='Home']"), "'Home' section.")
        
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screenshot at this point", x)

        
