#!/usr/bin/python3
'''
Hope you find what you're looking for
'''
import smtplib, ssl
import requests
PORT=587
########GLOBALS#############
glogin='--'
gpass='--'
dlogin='temperature86@sharklasers.com'
dpass='ppXavier5'
#########
def sendEmail(content):
    mesg = """\
Subject: dNoty

{}

    """.format(content)
    try:
        sess=smtplib.SMTP('smtp.gmail.com',587)
        sess.starttls()
        sess.login(glogin,gpass)
        sess.sendmail(glogin,glogin,mesg)
    except Exception as e:
        print('Not Sent: ',e)
    finally:
        sess.quit()
        print('Saw Something...')

sendEmail('TEst')
