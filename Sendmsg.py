from twilio.rest import Client 
 
account_sid = 'AC853bf6ab3c5e4a08339c9dbbe906156e' 
auth_token = 'a12e208e050bbe1261ebb9094d3405d6' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='How are you doing',      
                              to='whatsapp:+918114406146' 
                          ) 
 
print(message.sid)