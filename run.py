from email.email import Email
from prime.prime import Prime
import prime.constans as c


#Triggering the entire project
#Do this by python run.py

def run():
    p = Prime(start = c.START, finish = c.FINISH)
    prettier = p.Prettify()
    print(prettier)
    NewEmail = Email()
    NewEmail.to = 'mahdlooyi@gmail.com'
    NewEmail.subject = f'Prime Numbers execution between {c.START} to {c.FINISH}'
    NewEmail.body = prettier
    NewEmail.Send()
 

if __name__ == '__main__':
    run()