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
        
    _link        = "www.google.com"
    _TestMsg     = "Test " + _link + " this."
    
    _RESTART_DEVICE = True
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.messages   = Messages(self)
        self.browser    = Browser(self)
        
        #
        # Establish which phone number to use.
        #
        self.target_telNum = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        self.UTILS.logComment("Sending sms to telephone number " + self.target_telNum)
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        self.UTILS.getNetworkConnection()
        
        
        #
        # Launch messages app.
        #
        self.messages.launch()
        self.messages.deleteAllThreads() 
        #
        # Create and send a new test message.
        #
        self.messages.createAndSendSMS([self.target_telNum], self._TestMsg)
          
        #
        # Get the link of the first message
        #    
        x = self.UTILS.getElement( ("id", "message-1"), "Message sent")
        
        #
        #Verify that a valid URL appears highlight
        #
        y=x.find_element("tag name", "a")
        self.UTILS.TEST(y.text==self._link , "The web link is in the text message")
                