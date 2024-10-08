# Meeting Agenda and Recap

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/xanderstevenson/meeting-agenda-and-recap)

## Overview

This is a pair of Python scripts which use Adaptive Cards to post neat, organized meeting agendas and recaps to a Webex space of your choice. It also saves records of the agendas and recaps you send, storing them in folders and files named after the meeting name and date. 

I wrote this because I love automation and considered this to be a much smoother process than manually formatting meeting agendas and recaps from text documents to Webex messages. I hope this will help make managing *your* meetings a more pleasurable experience.

<br>

## Installation

### **Step 1**: Clone the parent repo and cd into this demo

```bash
git clone https://github.com/xanderstevenson/meeting-agenda-and-recap.git
cd meeting-agenda-and-recap
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



### **Step 4**: create the Webex Bot

- Go to https://developer.webex.com/my-apps and 'Create a New App'

- Choose 'Create a Bot'

- Fill out the required fields and click 'Add Bot'

- Save the Bot Token, Bot Name, Bot Username, and Bot ID 

- Determine the ID of the room you want to send the message to by first sending a message in that room
and then going to https://developer.webex.com/docs/api/v1/rooms/list-rooms
type 'lastactivity' in the 'sortBy' field and click send. Save the RoomID of the space you want to send the message to, along with a practice space to test messages.

- Copy the Room ID, along with the Bot Token, Name, Username, and Bot ID to .creds.py and rename it as creds.py

<br>


## Usage

- Rename **agenda-example.txt** to **agenda.txt**
- Rename **recap-example.txt** to **recap.txt**
- Fill in the agenda.txt or recap.txt and run the appropriate script:

```bash
python3 send_agenda.py
```

![image](https://github.com/xanderstevenson/meeting-agenda-and-recap/blob/main/images/agneda.png)


or

```bash
python3 send_recap.py
```

![image](https://github.com/xanderstevenson/meeting-agenda-and-recap/blob/main/images/recap.png)




<br>



## Message Formatting / Editing

- Regualar Webex markdown is enabled within the agenda message (see [Webex App | Markdown formats](https://help.webex.com/en-us/article/n7i55j5/Webex-App-%7C-Markdown-formats) for examples), but the following have been specially formatted

```
! represents the accent header (blue)
$ represents the warning header (orange)
% represents the attention header (reddish)
* represents the attention bullet point (reddish)
```

- The nesting of bullet points doens't function like it would normally in markdown in Webex messaging.

- Once an agenda is sent, it cannot be edited as described [here](https://developer.webex.com/docs/api/v1/messages/edit-a-message) because it uses an adaptive card, which is treated an an attachment, thus preventing editing. If you don't like an agenda, you should delete it from the space manually and send a new message.

- It looks best on both mobile and desktop if you follow the line spacing protocol demonstrated in agenda.txt and recap.txt. Just keep one empty line of space to seperate points.

- You don't need to add an empty line after - - - as it will add one by default.

<br>

## Keeping Records of Agendas and Recaps

I've added a functionality to the **send_agenda.py** and **send_recap.py** scripts so that when they are ran, it will save the agenda or recap in a folder named after the meeting. For example, based on [agenda-example.txt](https://github.com/xanderstevenson/meeting-agenda-and-recap/blob/main/agenda-example.txt) and [recap-example.txt](https://github.com/xanderstevenson/meeting-agenda-and-recap/blob/main/recap-example.txt) in this repo, it creates files called:

**records/Apple IIc Engineering Connect/agendas/Apple IIc Engineering Connect 19 August, 1987 Agenda.txt**

and 

**records/Apple IIc Engineering Connect/recaps/Apple IIc Engineering Connect 19 August, 1987 Recap.txt**

> Note: I've commented out the functions an commands in both scripts (send_agenda.py and send_recap.py) as I don't want to keep records of my meetings, but you can un-comment them and they will run as expected.

<br>

## Notes

- The creds.py file and the /records/ directory are already in the [.gitignore](https://github.com/xanderstevenson/meeting-agenda-and-recap/blob/main/.gitignore) so they won't be pushed to GitHub, but you should also add any other files to the .gitignore you don't want published to GitHub, should you choose to fork this repo. **I recommend *at least* adding *agenda.txt* and *recap.txt* to the .gitignore**

- You won't be able to post messages to a room until you've added your Bot to that Room

- You will want to create or use a practice room to send drafts of your agenda/recap to to see if you like it before sending it to the official room
