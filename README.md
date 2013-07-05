WARNING: USING THESE TESTS WILL RESULT IN ALL DATA BEING REMOVED FROM THE DEVICE!
=================================================================================



#Instructions for setting up and running automated test cases.

<b>1.</b> Clone and install the OWD_TEST_TOOLKIT repository as described in https://github.com/roydude/OWD_TEST_TOOLKIT (this will automatically install this owd_test_cases repo).

<b>2.</b> Once installed, make sure you have the JIRA login details set up in "$HOME/.jira_login":
<pre>
USERNAME <username>
PASSWORD <password>
</pre>

<b>2.</b> To run tests, type:

<pre>
./run_tests.sh
</pre>

... or specify particular test suites, like this:

<pre>
./run_tests.sh {REGRESSION}
</pre>

... or specify particular test numbers, like this:

<pre>
./run_tests.sh 7 8 21 40 41
</pre>

For more details, please refer to the README.md for OWD_TEST_TOOLKIT.

<!--testcoverage-->
TESTS COVERED
=============
<table>
  <tr>
    <th>Test Case</th><th>Description</th>
  </tr>

  <tr>
    <td  align=center>26727</td><td  align=left>Delete a picture just taken</td>
  </tr>

  <tr>
    <td  align=center>26328</td><td  align=left>Make a video recording - verify the recording is successful and added to the gallery</td>
  </tr>

  <tr>
    <td  align=center>26731</td><td  align=left>Delete a video just recorded</td>
  </tr>

  <tr>
    <td  align=center>26327</td><td  align=left>Take a picture with camera - verify the picture is successfully taken and added to the gallery</td>
  </tr>

  <tr>
    <td  align=center>26728</td><td  align=left>Go to Gallery from Camera</td>
  </tr>

  <tr>
    <td  align=center>26711</td><td  align=left>Select multiple pictures and delete them</td>
  </tr>

  <tr>
    <td  align=center>26330</td><td  align=left>Browse photos in gallery - verify you can see each picture of your sdcard</td>
  </tr>

  <tr>
    <td  align=center>26353</td><td  align=left>Import Facebook contacts from contacts app settings</td>
  </tr>

  <tr>
    <td  align=center>26918</td><td  align=left>Unlink all Facebook contacts in the address book in a single step and verify the contacts who was linked to a facebook contacts</td>
  </tr>

  <tr>
    <td  align=center>26907</td><td  align=left>Remove a photo,a phone number, an email, an address and a comment from a contact and restore the phone number and the comment</td>
  </tr>

  <tr>
    <td  align=center>26317</td><td  align=left>Send an email to a contact from the contact details (Contact with multiple emails)</td>
  </tr>

  <tr>
    <td  align=center>23887</td><td  align=left>Accept creating a new contact, editing some other fields</td>
  </tr>

  <tr>
    <td  align=center>26882</td><td  align=left>Search by text string (UPPER CASE) that matches the last name</td>
  </tr>

  <tr>
    <td  align=center>26323</td><td  align=left>Add new contact filling all the fields - verify the contact is added with the correct values for each field</td>
  </tr>

  <tr>
    <td  align=center>26895</td><td  align=left>The &quot;done&quot; button in new contact mode (email parameter)</td>
  </tr>

  <tr>
    <td  align=center>26900</td><td  align=left>Verify that when looking at the details of a contact, the user can make a call to the contact with several phone numbers added</td>
  </tr>

  <tr>
    <td  align=center>26899</td><td  align=left>Delete a contact from the contact details(all the fields filled)</td>
  </tr>

  <tr>
    <td  align=center>26901</td><td  align=left>Search a contact after edit contact name</td>
  </tr>

  <tr>
    <td  align=center>26885</td><td  align=left>Add multiple emails addresses</td>
  </tr>

  <tr>
    <td  align=center>26325</td><td  align=left>Send an sms from a contact detail - Verify the contact receives the SMS</td>
  </tr>

  <tr>
    <td  align=center>26886</td><td  align=left>Configure a contact as a favourite</td>
  </tr>

  <tr>
    <td  align=center>26883</td><td  align=left>Verify that the user can send a SMS from a contact details - SMS conversation doesn&#39;t exist</td>
  </tr>

  <tr>
    <td  align=center>26890</td><td  align=left>Delete all characters to the name and surname fields</td>
  </tr>

  <tr>
    <td  align=center>26874</td><td  align=left>Search by text string that not matches with any contact name/last name</td>
  </tr>

  <tr>
    <td  align=center>26324</td><td  align=left>Edit a contact changing the name and the phone number - verify that the values modified in the contact appear when viewing the updated contact</td>
  </tr>

  <tr>
    <td  align=center>26333</td><td  align=left>Load a website via Cellular Data - verify the site loads in the browser correctly</td>
  </tr>

  <tr>
    <td  align=center>26332</td><td  align=left>Load a website via Wifi - verify the site loads in the browser correctly</td>
  </tr>

  <tr>
    <td  align=center>26329</td><td  align=left>Play the video you recorded, check for video and sound to verify the video could be successfully played</td>
  </tr>

  <tr>
    <td  align=center>26467</td><td  align=left>Clock in different modes (analog, digital)</td>
  </tr>

  <tr>
    <td  align=center>26473</td><td  align=left>Alarm- Delete an alarm</td>
  </tr>

  <tr>
    <td  align=center>26348</td><td  align=left>Add an alarm - verify the alarm was added with the correct date and time</td>
  </tr>

  <tr>
    <td  align=center>26341</td><td  align=left>Receive email via imap with gmail.com - verify the email is received from the correct account the email was sent from</td>
  </tr>

  <tr>
    <td  align=center>26340</td><td  align=left>Send email via imap with gmail.com - verify the email is sent to the respective account</td>
  </tr>

  <tr>
    <td  align=center>26750</td><td  align=left>Basic: Deleting of a e-mail in Inbox</td>
  </tr>

  <tr>
    <td  align=center>26339</td><td  align=left>Receive email via activesync with hotmail.com - verify the email is received from the correct account the email was sent from</td>
  </tr>

  <tr>
    <td  align=center>26338</td><td  align=left>Send email via activesync with hotmail.com - verify the email is sent to the respective account</td>
  </tr>

  <tr>
    <td  align=center>26347</td><td  align=left>Add and view an event to an offline calendar in each calendar view - verify the event is shown on each calendar view with the correct title, location, and event time length</td>
  </tr>

  <tr>
    <td  align=center>26411</td><td  align=left>As a user, I want to be able to enable/disable Data from the utility tray</td>
  </tr>

  <tr>
    <td  align=center>26343</td><td  align=left>With two apps already running, launch the card view, kill one app process, and launch the other - verify the app killed is stopped and the other app starts up</td>
  </tr>

  <tr>
    <td  align=center>26408</td><td  align=left>Activate/Deactivate airplane mode from Utility tray icon</td>
  </tr>

  <tr>
    <td  align=center>26409</td><td  align=left>Open settings app from utility tray</td>
  </tr>

  <tr>
    <td  align=center>26773</td><td  align=left>Verify that the user can uninstall a everything.me app through the grid edit mode</td>
  </tr>

  <tr>
    <td  align=center>26779</td><td  align=left>Verify that if no connection available when selecting a category in everything.me the user will be notified about the need to have a network connection to use this functionality</td>
  </tr>

  <tr>
    <td  align=center>26774</td><td  align=left>Verify that user can click on &quot;Add more categories&quot; in everything.me grid so I am shown again the list and can add more categories</td>
  </tr>

  <tr>
    <td  align=center>26776</td><td  align=left>Verify that when the user navigates to everything.me page, dock is hidden</td>
  </tr>

  <tr>
    <td  align=center>26781</td><td  align=left>Add and remove categories to everything.me grid</td>
  </tr>

  <tr>
    <td  align=center>26345</td><td  align=left>Launch a packaged app - verify the app launches successfully to the correct content</td>
  </tr>

  <tr>
    <td  align=center>26778</td><td  align=left>Verify that when first launch a search-box is shown as well as a list of application categories</td>
  </tr>

  <tr>
    <td  align=center>26346</td><td  align=left>Delete a packaged app - verify the app was successfully removed from the homescreen</td>
  </tr>

  <tr>
    <td  align=center>26777</td><td  align=left>Verify that when the user navigates from everything.me page to the grid, dock is shown again</td>
  </tr>

  <tr>
    <td  align=center>26337</td><td  align=left>Launch market installed hosted app - verify the app is launched successfully from the homescreen</td>
  </tr>

  <tr>
    <td  align=center>26352</td><td  align=left>Install and launch an everything.me app - verify the everything.me app launches successfully to the right web content</td>
  </tr>

  <tr>
    <td  align=center>26840</td><td  align=left>Send a new SMS by entering manually the phone number (contact number)</td>
  </tr>

  <tr>
    <td  align=center>27761</td><td  align=left>Try to send an SMS when in the contact list window the end-user click on back (in contact list window) without selecting the contact.</td>
  </tr>

  <tr>
    <td  align=center>26852</td><td  align=left>Delete a SMS in a conversation with several sms</td>
  </tr>

  <tr>
    <td  align=center>27765</td><td  align=left>Send a new SMS using the search option (in contact list window) in order to select an existing contact</td>
  </tr>

  <tr>
    <td  align=center>27752</td><td  align=left>Receive an SMS with a link to a web site and open it</td>
  </tr>

  <tr>
    <td  align=center>27748</td><td  align=left>Verify the textfield item</td>
  </tr>

  <tr>
    <td  align=center>27756</td><td  align=left>Send a new SMS using the option of reduced list of favourite contacts</td>
  </tr>

  <tr>
    <td  align=center>26404</td><td  align=left>CLONE - Verify that If the contact only has a phone number, that phone number is automatically selected and the user is returned to the compose SMS screenwidth the contacts name filled-in in the To Field..</td>
  </tr>

  <tr>
    <td  align=center>27741</td><td  align=left>Receive a text message from number XXX while we are in the conversation details with that number</td>
  </tr>

  <tr>
    <td  align=center>26864</td><td  align=left>Try send a sms to a contact while airplane is enabled (from sms app - use contact option)</td>
  </tr>

  <tr>
    <td  align=center>26406</td><td  align=left>Press delete all text button in contact name field</td>
  </tr>

  <tr>
    <td  align=center>27750</td><td  align=left>Verify characters in text box above the keyboard when typing a sms</td>
  </tr>

  <tr>
    <td  align=center>27742</td><td  align=left>Write a sms with multiple spaces between words (ex; 1 2 3 4 5)</td>
  </tr>

  <tr>
    <td  align=center>26414</td><td  align=left>Received a SMS with more than 160 characteres</td>
  </tr>

  <tr>
    <td  align=center>26407</td><td  align=left>Verify that If the contact has more than one phone number, it opens a list of numbers. Clicking on a number in the list, returns the user to the compose SMS app with the contacts name filled-in in the To Field.</td>
  </tr>

  <tr>
    <td  align=center>26853</td><td  align=left>Delete all SMS in a conversation with several sms</td>
  </tr>

  <tr>
    <td  align=center>26862</td><td  align=left>Try send a sms creating a new thread while airplane is enabled</td>
  </tr>

  <tr>
    <td  align=center>26865</td><td  align=left>Receive an SMS from a contact with long name</td>
  </tr>

  <tr>
    <td  align=center>27746</td><td  align=left>Verify that If the name of the contact is not empty: The type of the phone and the phone carrier (as defined in the address book) as the secondary header</td>
  </tr>

  <tr>
    <td  align=center>27753</td><td  align=left>Delete a contact and verify that the SMS list now shows the number</td>
  </tr>

  <tr>
    <td  align=center>27736</td><td  align=left>Press delete without any conversation selected</td>
  </tr>

  <tr>
    <td  align=center>26741</td><td  align=left>Email containing a URL</td>
  </tr>

  <tr>
    <td  align=center>26845</td><td  align=left>Add a contact and verify that the SMS list now shows the name</td>
  </tr>

  <tr>
    <td  align=center>26860</td><td  align=left>Send/Receive a new SMS when the conversation thread is empty</td>
  </tr>

  <tr>
    <td  align=center>26859</td><td  align=left>Verify the timestamp (received message) when the SMS has been sent from a different timezone</td>
  </tr>

  <tr>
    <td  align=center>27749</td><td  align=left>Receive an SMS with a phone number and store it</td>
  </tr>

  <tr>
    <td  align=center>26415</td><td  align=left>Send a SMS with more than 160 characteres</td>
  </tr>

  <tr>
    <td  align=center>27763</td><td  align=left>Verify that If the name of the contact is not empty: The name of the contact as the main header</td>
  </tr>

  <tr>
    <td  align=center>26856</td><td  align=left>Try to send empty SMS</td>
  </tr>

  <tr>
    <td  align=center>27764</td><td  align=left>Write and send a sms with line break</td>
  </tr>

  <tr>
    <td  align=center>26403</td><td  align=left>Verify that If the contact has more than one phone number, it opens a list of numbers. Clicking on a number in the list, returns the user to the compose SMS app with the contacts name filled-in in the To Field.(second phone number)</td>
  </tr>

  <tr>
    <td  align=center>27735</td><td  align=left>Verify that If the name of the contact is not empty:  No carrier information is linked to the phone: Phone Number is shown instead of carrier as the secondary header</td>
  </tr>

  <tr>
    <td  align=center>27758</td><td  align=left>Access and exit edit mode</td>
  </tr>

  <tr>
    <td  align=center>26405</td><td  align=left>Press cancel button in the screen for select a contact phone number</td>
  </tr>

  <tr>
    <td  align=center>27754</td><td  align=left>Send an SMS to multiple contacts</td>
  </tr>

  <tr>
    <td  align=center>27743</td><td  align=left>Edit a contact name and verify that the SMS list now shows the new name</td>
  </tr>

  <tr>
    <td  align=center>27759</td><td  align=left>Verify that If the contact has no phone number, a message stating that contact does not have a phone number is open up, and user is returned the contact list.</td>
  </tr>

  <tr>
    <td  align=center></td><td  align=left></td>
  </tr>

  <tr>
    <td  align=center>26839</td><td  align=left>Send a new SMS by entering manually the phone number</td>
  </tr>

  <tr>
    <td  align=center>27745</td><td  align=left>Try to send SMS without any contact</td>
  </tr>

  <tr>
    <td  align=center>26846</td><td  align=left>Delete a sms conversation</td>
  </tr>

  <tr>
    <td  align=center>27760</td><td  align=left>Try to send an SMS when the introduced text has been deleted.</td>
  </tr>

  <tr>
    <td  align=center>27751</td><td  align=left>Try send a sms (after enabled and disabled airplane mode) </td>
  </tr>

  <tr>
    <td  align=center>27744</td><td  align=left>Introduce a valid SMS and click on Back option</td>
  </tr>

  <tr>
    <td  align=center>26847</td><td  align=left>Select some conversations and press delete</td>
  </tr>

  <tr>
    <td  align=center>27762</td><td  align=left>Receive an SMS with a phone number and call to it</td>
  </tr>

  <tr>
    <td  align=center>26851</td><td  align=left>Receive a sms while device is locked(Vibration alert), screen off</td>
  </tr>

  <tr>
    <td  align=center>26857</td><td  align=left>Verify that the SMS conversation window shows the message preview (more than one SMS message in the conversation thread)</td>
  </tr>

  <tr>
    <td  align=center>27740</td><td  align=left>Verify that the SMS conversation window shows the message preview (only one outgoing SMS message in the conversation thread) </td>
  </tr>

  <tr>
    <td  align=center>27739</td><td  align=left>Try send a sms to a phone number (no contact) while airplane is enabled</td>
  </tr>

  <tr>
    <td  align=center>26967</td><td  align=left>Verify that when tapping on the highlighted URL the browser is opened with the selected URL</td>
  </tr>

  <tr>
    <td  align=center>26326</td><td  align=left>Receive a sms with vibration (device unlocked) &amp; confirm notification - verify that the notification is fired and that you can see the message received from the other phone</td>
  </tr>

  <tr>
    <td  align=center>27755</td><td  align=left>Verify that the SMS conversation window shows the message preview (only one incoming SMS message in the conversation thread)</td>
  </tr>

  <tr>
    <td  align=center>26861</td><td  align=left>Verify the Carrier of number from which the contact is sending message to the user</td>
  </tr>

  <tr>
    <td  align=center>26863</td><td  align=left>Try send a sms in an existing thread while airplane is enabled</td>
  </tr>

  <tr>
    <td  align=center>27757</td><td  align=left>Verify The phone number displayed in a conversation</td>
  </tr>

  <tr>
    <td  align=center>27747</td><td  align=left>Verify that  If the name of the contact is empty: Phone Number as the main header.</td>
  </tr>

  <tr>
    <td  align=center>27737</td><td  align=left>Try to send a new SMS using the search option (in contact list window) in order to select an inexisting contact</td>
  </tr>

  <tr>
    <td  align=center>26336</td><td  align=left>Install a market installed hosted app - verify the app is installed with the right icon</td>
  </tr>
</table>
