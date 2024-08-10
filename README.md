# Webex Meeting Agenda and Recap

## Overview

This is a pair of Python scripts which post neat, organized meeting agendas and recaps to a Webex space of your choice. I wrote this because I was tired of manually formatting meeting agendas and recaps from text documents to Webex messages. I hope this will make managing your meetings a more pleasurable experience.

<br>

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



### **Step 4**: create the Webex Bot

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

![image](https://github.com/user-attachments/assets/025bc15b-c289-46ee-a1dd-99597fd87297)


or

```bash
python3 send_recap.py
```

![image](https://github.com/user-attachments/assets/ef085469-53ed-4fcc-813b-d5fc97c6bb5a)




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


### Notes

- The creds.py file is already in the .gitignore so it won't be pushed to GitHub but you should also add any other files to the .gitignore you don't want published to GitHub, should you choose to fork this repo.

- You won't be able to post messages to a room until you've added your Bot to that Room

- You will want to create or use a practice room to send drafts of your agenda/recap to to see if you like it before sending it to the official room
