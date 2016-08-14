from datetime import datetime

# file settings
#create empty log file and locate below
LOG_FILENAME = 'location'

#create empty pymailer.csv file and locate below

CSV_RETRY_FILENAME = 'location'

#locate the folder for save the stat files

STATS_FILE = 'location/pymailer-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

# smtp settings
SMTP_HOST = 'xyz'
SMTP_PORT = '465' #465 for SSL, smtplib.SMTP_SSL() or without SSL, smtplib.SMTP() in pymailer.py 
#login detail
EMAIL = 'xyz@xyz.com' #email of sender
PASS = '' #password for email id

# the address and name the email comes from
FROM_NAME = 'xyz' #name of Sender 
FROM_EMAIL = 'xyz@xyz.com' #same as EMAIL above

# test recipients list when -t option
TEST_RECIPIENTS = [
    {'name': 'Name', 'email': 'test@testemail.com'},
]
