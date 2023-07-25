api/twilio_api.py:

```python
from twilio.rest import Client

class TwilioAPI:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, to_number, message):
        message = self.client.messages.create(
            body=message,
            from_="YOUR_TWILIO_PHONE_NUMBER",
            to=to_number
        )
        return message.sid
```

Please note that you need to replace "YOUR_TWILIO_PHONE_NUMBER" with your actual Twilio phone number.