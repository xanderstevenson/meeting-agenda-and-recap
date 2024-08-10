
# Webex Meeting Agenda and Recap

## Installation

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/xanderstevenson/webex-meeting-agenda-and-recap.git
cd webex-meeting-agenda-and-recap
```
<br>

> **Note:** Optional: In VS Code you can open all files in this repo with this command
```bash
code .
```
> **Note:** You'll then see the file manager on the left-hand side. After this, simply choose **Terminal > New Terminal** from the VS Code menu to open a new Terminal.
<br>


### **Step 2**: Create and activate a Python virtual environment

- Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
- Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```
<br>



### **Step 3**: Install Dependencies

```bash
pip3 install -r requirements.txt
```
<br>
<br>



<br>


### **Step 3**: create the Webex Bot

- Go to https://developer.webex.com/my-apps and 'Create a New App'

- Choose 'Create a Bot'

- Fill out the required fields and click 'Add Bot'

- Save the Bot Token, Bot Name, Bot Username, and Bot ID 

- Determine the ID of the room you want to send the message to b first sending a message in that room
and then going to https://developer.webex.com/docs/api/v1/rooms/list-rooms
type 'lastactivity' in the 'sortBy' field and click send. Copy that RoomID to creds.py

- Copy the Room ID, along with the Bot Token, Name, Username, and Bot ID to .creds.py and rename it as creds.py

<br>


## Usage

- Fill in the agenda.txt or recap.txt and run the appropriate script:

```bash
python3 send_agenda.py
```

or

```bash
python3 send_recap.py
```


<br>



## Message Formatting / Editing

- Regualar Webex markdown is enabled within the agenda message (see [Webex App | Markdown formats](https://help.webex.com/en-us/article/n7i55j5/Webex-App-%7C-Markdown-formats) for examples), but the following have been specially formatted

```
! represents the accent header (blue)
$ represents the warning header (orange)
% represents the attention header (reddish)
* represents the attention bullet point (reddish)
```

- The nesting of bullet points doens't function like it would normmally in markdown in Webex messaging.

- Once an agenda is sent, it cannot be edited as described [here](https://developer.webex.com/docs/api/v1/messages/edit-a-message) because it uses and adaptive card, which is treated an an attachment, this preventing editing.
If you don't like an agenda, you should delete it from the space manually and send a new message.

- The message is sensitive to spaces, so if you place a lot of lines between points, it will render a lot of space in the message.



