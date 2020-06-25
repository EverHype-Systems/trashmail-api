# Trashmail-API
Manage and check entered email addresses with our Python API-wrapper for trashmail-api.de. GDPR compliant. 

Please download or clone this repository and put it into your project folders.

How to use:
```python
# IMPORT TRASHMAIL CLASS
from trashmail_api.trashmail import TrashMail

# DEFINE YOUR API TOKEN
# CAN BE FOUND ON https://trashmail-api.de/dashboard/profile
API_TOKEN = 'putYourTokenHere'

# INITALIZE CLASS OBJECT
trashmail = TrashMail(API_TOKEN)

# CHECK ONE MAIL PROVIDED E.G FROM USER
# OPTIONALLY YOU CAN MAKE THIS REQUEST GDPR compliant
# md5 = TRUE/FALSE -> TRUE::GDPR compliant // FALSE::Sending raw mail
print(trashmail.check_mail('provided@mail.com', md5=True)

# ADD E-MAILS TO YOUR ACCOUNT LIST
# PLEASE READ COMMENTS IN CLASS
# PUT YOUR MAILS IN AN ARRAY
mails = [
  "item1.com",
  "item2.com",
  ...,
  "item3000.com"
]
print(trashmail.add_mails(mails)
```

And so on. Please read the comments in the class file (trashmail_api/trashmail.py). If you have any questions, feel free to open an issue.

