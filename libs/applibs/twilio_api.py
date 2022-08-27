from twilio.rest import Client

def twilio_send_msg(activerUser,message,phoneNumber):
    account_sid = activerUser["account_sid"]
    auth_token = activerUser["auth_token"]
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message,
                        from_=activerUser["phone_num"],
                        to=phoneNumber,
                        status_callback=activerUser["server_url"]
                    )
    return message.sid
