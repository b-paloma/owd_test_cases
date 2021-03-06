#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *

#
# Imports particular to this test case.
#
from tests._mock_data.contacts import MockContacts

class test_main(GaiaTestCase):
    
    _testNum = "123456789"
    
    def setUp(self):
        # Set up child objects...
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.dialer     = Dialer(self)
        self.contacts   = Contacts(self)
        

        self.cont1 = MockContacts().Contact_1
        self.cont1["tel"]["value"] = "111111111"
        self.data_layer.insert_contact(self.cont1)
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Enter a number in the dialer.
        #
        
        self.dialer.launch()
        self.dialer.enterNumber(self._testNum)
        
        #
        # Press the add to contacts button, then select 'add to existing contact'.
        #
        x = self.UTILS.getElement(DOM.Dialer.add_to_contacts_button, "Add to contacts button")
        x.tap()
        
        x = self.UTILS.getElement(DOM.Dialer.add_to_existing_contact_btn, "Add to existing contact button")
        x.tap()

        self.UTILS.switchToFrame(*DOM.Contacts.frame_locator)
        self.contacts.viewContact(self.cont1["name"], p_HeaderCheck=False)

        x = self.UTILS.getElement( ("name", "tel[0][value]"), "Phone number 1")
        self.UTILS.TEST(x.get_attribute("value") == self.cont1["tel"]["value"], 
                        "1st number is %s (it was %s)." % (self.cont1["tel"]["value"], x.get_attribute("value")))

        x = self.UTILS.getElement( ("name", "tel[1][value]"), "Phone number 2")
        self.UTILS.TEST(x.get_attribute("value") == self._testNum, 
                        "2nd number is %s (it was %s)." % (self._testNum, x.get_attribute("value")))
        
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Final screenshot:", x)