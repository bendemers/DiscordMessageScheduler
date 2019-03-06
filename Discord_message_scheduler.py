from dhooks import Webhook
from datetime import date, time, datetime

try:
    schedule_date = input("Welcome to the Discord Message Scheduler! What day would you like the message to be sent? (MM/DD/YYYY): ")
    if not schedule_date:
        raise ValueError('Please enter a value!')
except ValueError as e:
    print(e)

try:
    schedule_time = input("What time would you like the message to be sent? (EST, 0:00-24:00): ")
    if not schedule_time:
        raise ValueError('Please enter a value!')
except ValueError as e:
    print(e)
month, day, year = map(int, schedule_date.split('/'))
hour, minute = map(int, schedule_time.split(':'))
date = datetime(year, month, day, hour, minute)
try:
    message_content = input("What would you like the message to say?: ")
    if not message_content:
        raise ValueError('Please enter a value!')
except ValueError as e:
    print(e)

try:
    WEBHOOK = input("Webhook url?: ")
    if not WEBHOOK:
        raise ValueError('Please enter a value!')
except ValueError as e:
    print(e)

print("Please leave the script running while the message sends!")
while True:
    if date < datetime.now():
        hook = Webhook(WEBHOOK)
        hook.send(message_content)
        print("Message sent to discord!")
        break