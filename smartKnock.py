account_sid='AC9b67feeb945cfc6535b679d7160fd693'
auth_token='4972c6f7fb4c012a8c78131419ec2094'
import os
from twilio.rest import Client
client = Client(account_sid, auth_token)
import RPi.GPIO as GPIO
import time
import sys
from pynput.mouse import Button, Controller
mouse = Controller()

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channels):
    if GPIO.input(channels):
        message = client.messages.create(body='Sounds like someone is at the door!: https://Mani-Amani.github.io', from_=12514510701, to= 14244100143)
        mouse.position = (30, 230)
        mouse.click(Button.left, 2)
        mouse.move(100, 160)
        mouse.click(Button.left, 2)
        mouse.move(1380, -130)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.move(0, 100)
        mouse.click(Button.left, 1)

        mouse.position = (960, 960)

        time.sleep(6)

        mouse.move(0, -200)
        time.sleep(3)
        mouse.move(0, 200)
        time.sleep(2)

        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
    else:
        message = client.messages.create(body='Sounds like someone is at the door!', from_=12514510701, to= 14244100143)
        mouse.position = (30, 230)
        mouse.click(Button.left, 2)
        mouse.move(100, 160)
        mouse.click(Button.left, 2)
        mouse.move(1380, -130)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.move(0, 100)
        mouse.click(Button.left, 1)

        mouse.position = (960, 960)

        time.sleep(35)

        mouse.move(0, -200)
        time.sleep(3)
        mouse.move(0, 200)
        time.sleep(2)

        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
    time.sleep(10)
    os.execl(sys.executable, sys.executable, *sys.argv)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

#if messageSent == False:
    #break

while True:
    time.sleep(1)