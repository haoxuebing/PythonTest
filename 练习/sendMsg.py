from twilio.rest import Client
account_sid = "ACbbf6745b63dda09d9a0df810c25c598c"
auth_token  = "f38d6744e5961282f285dabfa11a408e"
client = Client(account_sid, auth_token)
message = client.messages.create(
# 这里中国的号码前面需要加86
to="+8617611222100",
from_="+18646531906",
body="Hello from Python!")
print(message.sid)





