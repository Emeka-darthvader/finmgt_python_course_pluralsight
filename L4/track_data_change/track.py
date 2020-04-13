import urllib2
import smtplib
import email.utils
from email.mime.text import MIMEText 
import ssl

#for fetching data/ the csv file
def fetchData():
    url='https://www.quandl.com/api/v3/datasets/LBMA/GOLD.csv?api_key=iepxUmawinikJosTbAVe'
    params='&end_date=2018-12-31&rows=1&column_index=1&exclude_column_names=true'
    #gcontext = ssl.SSLContext()  ssl.PROTOCOL_TLS_CLIENT
    #gcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    gcontext = ssl.create_default_context()
    csv = urllib2.urlopen(url + params,context=gcontext)
    r=csv.read()
    d= r.split(',')
    return d

#function that reads the csv file returned
#check if price is different from forecast
# if price is less than forecast value, an email is sent
def processData(fcv,d):
    for l in d:
        if not '-' in l:
            gp = float(l)
            if gp < fcv:
                print gp
                sendMail(str(gp))
        return

#function to send email

def sendMail(gp):
    sender=''
    receiver =''
    sndpwd=''

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,sndpwd)

    msg=MIMEText('Gold price has changed from forecast to'+gp)
    msg['To']=email.utils.formataddr(('Recipient',receiver))
    msg['From']=email.utils.formataddr(('Author',sender))
    msg['subject'] = 'Gold Price changed'

    try:
        sender.sendmail(sender,[receiver],msg.as_string())
    finally:
        server.quit()
    return


d = fetchData()
processData(2000,d)


