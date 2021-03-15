from twilio.rest import Client

account_sid = 'ACdd09eaf361100138f6872ab08c9cfb78'
auth_token ='6261a536abd7d88fb8696cd5909b28f8'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="go and learn english",
                     from_='+19045483263',
                     to='+995558400278'
                 )

print(message.sid)