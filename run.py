from email.email import Email
from prime.prime import Prime
import prime.constans as c


# Triggering the entire project
# Do this by python run.py

def run():
    p = Prime(start=c.START, finish=c.FINISH)
    prettier = p.prettify()
    print(prettier)
    new_email = Email()
    new_email.to = 'mahdlooyi@gmail.com'
    new_email.subject = f'Prime Numbers execution between {c.START} to {c.FINISH}'
    new_email.body = prettier
    new_email.send()


if __name__ == '__main__':
    run()

