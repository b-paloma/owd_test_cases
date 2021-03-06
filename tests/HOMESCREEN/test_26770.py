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
    
    _GROUP_NAME  = "Games"

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        
        self.UTILS      = UTILS(self)
        self.Settings   = Settings(self)
        self.EME        = EverythingMe(self)
        
        #
        # Don't prompt me for geolocation (this was broken recently in Gaia, so 'try' it).
        #
        try:
            self.apps.set_permission('Homescreen', 'geolocation', 'deny')
        except:
            self.UTILS.logComment("(Just FYI) Unable to automatically set Homescreen geolocation permission.")

        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
    
        #
        # Make sure 'things' are as we expect them to be first.
        #
        self.UTILS.getNetworkConnection()
         
        #
        # First, get the name of the app we're going to install.
        #
        self.EME.launch()
        
        self.EME.pickGroup(self._GROUP_NAME)
         
        x = self.UTILS.getElements(DOM.EME.apps, "The first game that is not installed already")[0]
        self._APP_NAME = x.get_attribute("data-name")
        self.UTILS.logResult("info", "App name is <b>%s</b>" % self._APP_NAME)
        self.UTILS.goHome()
 
         
        #
        # Make sure our app isn't installed already.
        #
        self.UTILS.uninstallApp(self._APP_NAME)
        
             
        #
        # Launch the 'everything.me' app.
        #
        self.EME.launch()
         
        #
        # Pick a group.
        #
        self.EME.pickGroup(self._GROUP_NAME)
 
        #
        # Add the app to the homescreen.
        #
        self.UTILS.TEST(self.EME.addAppToHomescreen(self._APP_NAME),
                        "Application '" + self._APP_NAME + "' is added to the homescreen.",
                        True)
        
        #
        # Go back to the homescreen and check it's installed.
        #
        self.UTILS.TEST(self.UTILS.launchAppViaHomescreen(self._APP_NAME), 
                        self._APP_NAME + " is installed.", True)
        
        #
        # Give it 10 seconds to start up, switch to the frame for it and grab a screenshot.
        #
        time.sleep(10)
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame("data-name", self._APP_NAME)
        
        x = self.UTILS.screenShot(self._APP_NAME)
        self.UTILS.logResult("info", "NOTE: For a screenshot of the game running, please see this: " + x)
