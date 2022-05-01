from twilio.rest import Client
import datetime

account_sid = '******************'
auth_token = '*********************'
client = Client(account_sid, auth_token)


def send_alert():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    message = client.messages.create(
        from_='whatsapp:+***********',
        body=f'No Face Mask Alert - Camera 0 at {current_time}',
        to='whatsapp:+***********'
    )
