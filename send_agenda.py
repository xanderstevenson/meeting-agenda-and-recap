import requests
import json
import os
from creds import BOT_TOKEN, ROOM_ID


def read_agenda_from_text_file(filename):
    with open(filename, "r") as file:
        return file.read()


def format_agenda(agenda):
    lines = agenda.split("\n")
    formatted_agenda = []

    for line in lines:
        line = line.strip()

        if line == "- - -":
            formatted_agenda.append(
                {
                    "type": "TextBlock",
                    "text": "",
                    "wrap": True,
                    "separator": True,
                    "color": "light",
                }
            )
        elif line.startswith("# "):
            header_text = line[2:].strip()
            formatted_agenda.append(
                {
                    "type": "TextBlock",
                    "text": header_text,
                    "weight": "bolder",
                    "size": "medium",
                    "color": "accent",
                }
            )
        elif line.startswith("* "):
            formatted_agenda.append(
                {
                    "type": "TextBlock",
                    "text": f"* {line[2:]}",  # Adding the bullet marker
                    "wrap": True,
                    "spacing": "none",
                }
            )
        elif line.startswith("1. "):
            formatted_agenda.append(
                {"type": "TextBlock", "text": line, "wrap": True, "spacing": "none"}
            )
        else:
            formatted_agenda.append({"type": "TextBlock", "text": line, "wrap": True})

    return formatted_agenda


def save_message_id(message_id):
    with open("message_id.txt", "w") as file:
        file.write(message_id)


def load_message_id():
    if os.path.exists("message_id.txt"):
        with open("message_id.txt", "r") as file:
            return file.read().strip()
    return None


def send_agenda_to_webex(agenda):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {BOT_TOKEN}",
        "Content-Type": "application/json",
    }

    adaptive_card = {
        "type": "AdaptiveCard",
        "body": [
            {
                "type": "TextBlock",
                "text": "Meeting Agenda",
                "weight": "bolder",
                "size": "large",
                "color": "good",
            }
        ]
        + format_agenda(agenda),
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.0",
    }

    payload = {
        "roomId": ROOM_ID,
        "text": "",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": adaptive_card,
            }
        ],
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        message_id = response.json().get("id")
        print(f"Agenda sent successfully! Message ID: {message_id}")
        save_message_id(message_id)
        return message_id
    else:
        print(f"Failed to send agenda. Status code: {response.status_code}")
        print("Response:", response.json())
        return None


def edit_agenda_message(message_id, new_agenda):
    url = f"https://webexapis.com/v1/messages/{message_id}"
    headers = {
        "Authorization": f"Bearer {BOT_TOKEN}",
        "Content-Type": "application/json",
    }

    # Fetch the existing message to check if it has attachments
    get_url = url
    get_response = requests.get(get_url, headers=headers)
    if get_response.status_code == 200:
        existing_message = get_response.json()
        if existing_message.get("attachments"):
            print("Cannot edit message with attachments.")
            return

    # Prepare the new adaptive card
    adaptive_card = {
        "type": "AdaptiveCard",
        "body": [
            {
                "type": "TextBlock",
                "text": "Meeting Agenda",
                "weight": "bolder",
                "size": "large",
                "color": "good",
            }
        ]
        + format_agenda(new_agenda),
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.0",
    }

    payload = {
        "roomId": ROOM_ID,
        "text": "",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": adaptive_card,
            }
        ],
    }

    response = requests.put(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Agenda updated successfully!")
    else:
        print(f"Failed to update agenda. Status code: {response.status_code}")
        print("Response:", response.json())


if __name__ == "__main__":
    agenda_file = "agenda.txt"
    meeting_agenda = read_agenda_from_text_file(agenda_file)

    action = (
        input(
            "Do you want to send a new message or edit the last message? (new/edit): "
        )
        .strip()
        .lower()
    )

    if action == "edit":
        message_id = load_message_id()
        if message_id:
            print(f"Editing existing message ID: {message_id}")
            edit_agenda_message(message_id, meeting_agenda)
        else:
            print("No existing message ID found. Please send a new message first.")
    elif action == "new":
        print("Sending new message...")
        send_agenda_to_webex(meeting_agenda)
    else:
        print("Invalid option. Please enter 'new' or 'edit'.")
