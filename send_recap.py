import requests
import json
import os
from creds import BOT_TOKEN, ROOM_ID


def read_recap_from_text_file(filename):
    with open(filename, "r") as file:
        return file.read()


def format_recap(recap):
    lines = recap.split("\n")
    formatted_recap = []

    for i, line in enumerate(lines):
        line = line.strip()

        # Add controlled spacing before each line except the first one
        if i > 0 and (lines[i - 1].strip() == "" or lines[i - 1].strip() == "- - -"):
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": " ",  # Single space to maintain some spacing
                    "wrap": True,
                    "spacing": "none",
                }
            )

        if line == "- - -":
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": "───────────────────────",  # Adjusted line length
                    "wrap": True,
                    "spacing": "none",
                    "color": "light",
                }
            )
        elif line.startswith("! "):
            header_text = line[2:].strip()
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": header_text,
                    "weight": "bolder",
                    "size": "medium",
                    "color": "accent",
                    "wrap": True,
                    "spacing": "medium",
                }
            )
        elif line.startswith("$ "):
            header_text = line[2:].strip()
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": header_text,
                    "weight": "bolder",
                    "size": "medium",
                    "color": "warning",
                    "wrap": True,
                    "spacing": "medium",
                }
            )
        elif line.startswith("% "):
            header_text = line[2:].strip()
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": header_text,
                    "weight": "bolder",
                    "size": "medium",
                    "color": "attention",
                    "wrap": True,
                    "spacing": "medium",
                }
            )
        elif line.startswith("* "):
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": f"* {line[2:]}",  # Adding the bullet marker
                    "wrap": True,
                    "spacing": "small",
                    "color": "attention",
                }
            )
        elif line.startswith("- "):
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": f"- {line[2:]}",  # Adding the bullet marker
                    "wrap": True,
                    "spacing": "small",
                }
            )
        elif line.startswith("1. "):
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": line,
                    "wrap": True,
                    "spacing": "small",
                }
            )
        else:
            formatted_recap.append(
                {
                    "type": "TextBlock",
                    "text": line,
                    "wrap": True,
                    "spacing": "small",
                }
            )

    return formatted_recap


# def save_recap_to_file(recap, meeting_name, meeting_date):
#     # Create directories if they don't exist
#     records_dir = "records"
#     meeting_dir = os.path.join(records_dir, meeting_name)
#     recaps_dir = os.path.join(meeting_dir, "recaps")

#     os.makedirs(recaps_dir, exist_ok=True)

#     # Create filename based on meeting name and date with "Recap" in the name
#     filename = f"{meeting_name} {meeting_date} Recap.txt"
#     file_path = os.path.join(recaps_dir, filename)

#     with open(file_path, "w") as file:
#         file.write(recap)


def save_message_id(message_id):
    with open("message_id.txt", "w") as file:
        file.write(message_id)


def send_recap_to_webex(recap):
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
                "text": "Meeting Recap",
                "weight": "bolder",
                "size": "large",
                "color": "attention",
            }
        ]
        + format_recap(recap),
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
        print(f"Recap sent successfully!")
        save_message_id(message_id)
    else:
        print(f"Failed to send recap. Status code: {response.status_code}")
        print("Response:", response.json())


if __name__ == "__main__":
    recap_file = "recap.txt"
    meeting_recap = read_recap_from_text_file(recap_file)

    # Extract meeting name and date from the first two lines
    recap_lines = meeting_recap.split("\n")
    if len(recap_lines) >= 2:
        meeting_name = recap_lines[0].strip().lstrip("! ").strip()
        meeting_date = recap_lines[1].strip()

        # Save the recap to a file
        # save_recap_to_file(meeting_recap, meeting_name, meeting_date)

        print("Sending new message...")
        send_recap_to_webex(meeting_recap)
    else:
        print("The recap file does not contain enough lines.")
