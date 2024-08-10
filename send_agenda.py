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
        elif line.startswith("! "):
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
        elif line.startswith("$ "):
            header_text = line[2:].strip()
            formatted_agenda.append(
                {
                    "type": "TextBlock",
                    "text": header_text,
                    "weight": "bolder",
                    "size": "medium",
                    "color": "warning",
                }
            )
        elif line.startswith("% "):
            header_text = line[2:].strip()
            formatted_agenda.append(
                {
                    "type": "TextBlock",
                    "text": header_text,
                    "weight": "bolder",
                    "size": "medium",
                    "color": "attention",
                }
            )
        elif line.startswith("* "):
            formatted_agenda.append(
                {
                    "type": "TextBlock",
                    "text": f"* {line[2:]}",  # Adding the bullet marker
                    "wrap": True,
                    "spacing": "none",
                    "color": "attention",  # Apply reddish color
                }
            )
        elif line.startswith("- "):
            formatted_agenda.append(
                {
                    "type": "TextBlock",
                    "text": f"- {line[2:]}",  # Adding the bullet marker
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
        print(f"Agenda sent successfully!")
        save_message_id(message_id)
    else:
        print(f"Failed to send agenda. Status code: {response.status_code}")
        print("Response:", response.json())


if __name__ == "__main__":
    agenda_file = "agenda.txt"
    meeting_agenda = read_agenda_from_text_file(agenda_file)
    print("Sending new message...")
    send_agenda_to_webex(meeting_agenda)
