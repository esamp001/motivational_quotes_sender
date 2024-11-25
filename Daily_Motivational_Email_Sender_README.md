
# Daily Motivational Email Sender

This Python script sends a random motivational quote to a specified recipient via email every minute. It reads quotes from a text file and sends an email containing the quote to the recipient at regular intervals.

## Features
- Sends a random quote from a list of quotes stored in `quotes.txt`.
- Automatically sends the email every minute.
- Configurable email details like sender and receiver email addresses.
- Sends emails using Gmail's SMTP server.

## Requirements
- Python 3.x
- `pytz` library for timezone handling
- `smtplib` and `email.mime` libraries for email sending
- A Gmail account (used for sending the emails)

### Installation

To use this script, you'll need to install the required Python libraries. You can do this using `pip`:

```bash
pip install pytz
```

## Setup

1. Clone or download the repository.
2. Create a file called `quotes.txt` in the same directory as the script. This file should contain a list of motivational quotes, each on a new line.
3. Update the following variables in the script with your own information:
   - `my_email`: Your Gmail address.
   - `my_password`: Your Gmail app-specific password (use a generated app password if you have two-factor authentication enabled).
   - `receiver_email`: The recipient's email address (where the quotes will be sent).

   **Note**: Do not expose your Gmail password in public repositories or scripts. Use environment variables or a secrets manager to keep it secure.

## Usage

Run the script as follows:

```bash
python send_daily_email.py
```

The script will:
1. Select a random quote from `quotes.txt`.
2. Send the selected quote via email to the specified recipient every minute.
3. Repeat indefinitely, sending a new quote every minute.

## Notes

- The email is sent using Gmail's SMTP server (`smtp.gmail.com`).
- The time zone for the script is set to `Asia/Manila`. Modify the `time_zone` variable if you are located in a different time zone.
- Make sure you have internet access for the script to work properly.
- If you're using two-factor authentication with your Gmail account, you need to generate an app-specific password for the script.

## Troubleshooting

- **Email not sending**: Make sure your Gmail account allows less secure apps or use an app-specific password if two-factor authentication is enabled.
- **Quotes not being sent**: Ensure the `quotes.txt` file exists and contains at least one quote.
- **Errors in time**: The script uses `datetime` and `timedelta` to schedule email sending based on the time zone, so make sure the time zone is correctly set.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
