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

class test_main(GaiaTestCase):
    
    def setUp(self):
        # Set up child objects...
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.dialer     = Dialer(self)
        self.contacts   = Contacts(self)
        
        self.num  = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Enter a number in the dialer.
        #
        self.dialer.launch()
        self.dialer.enterNumber(self.num)
        
        #
        # Press the add to contacts button, then select 'add to existing contact'.
        #
        x = self.UTILS.getElement(DOM.Dialer.add_to_contacts_button, "Add to contacts button")
        x.tap()
        
        x = self.UTILS.getElement(DOM.Dialer.add_to_existing_contact_btn, "Add to existing contact button")
        x.tap()

        #
        # You should now see the error message.
        #
        self.UTILS.switchToFrame(*DOM.Contacts.frame_locator)
        self.UTILS.waitForElements( ("xpath", "//*[contains(text(), 'Cannot add to contact')]"), 
                                    "Warning that there are no contacts.", True, 5, False)
                
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screen shot of current position:", x)