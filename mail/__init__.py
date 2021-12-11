# %%
def mail(accuracy='Accuracy',recall='Recall',precision='Precision'):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    
    content = MIMEMultipart()
    content['subject'] = 'Training Result'
    content['from'] = 'joyce.sendresult@gmail.com'
    content['to'] = 'joyce.sendresult@gmail.com'
    content.attach(MIMEText(accuracy+','+recall+','+precision))

    with smtplib.SMTP(host='smtp.gmail.com',port='587') as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('joyce.sendresult@gmail.com','rtnvukziqcztsgfz')
            smtp.send_message(content)
            print('Complete!')
        except Exception as e:
            print('Error message:',e)
    





# %%
