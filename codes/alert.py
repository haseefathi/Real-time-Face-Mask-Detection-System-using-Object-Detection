from twilio.rest import Client
import datetime

account_sid = 'AC7794fc5f48e1453642a2e7e5628c8086'
auth_token = '413044b6a8c546d9ca77d074bfb4e73b'
client = Client(account_sid, auth_token)


def send_alert():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'No Face Mask Alert - Camera 0 at {current_time}',
        to='whatsapp:+16462919529'
    )
