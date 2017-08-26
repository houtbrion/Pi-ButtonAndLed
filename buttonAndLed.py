#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

# ピン番号
# ボタン : GPIO 21  (ピン番号40)
# LED    : GPIO 20  (ピン番号38)
buttonPin = 21
ledPin = 20

# ボタンをチェックするループの待ち時間
loopWait = 0.05
# ボタンをONと判定する閾値
buttonThreshold=10

# ピンのセットアップ
def setupPins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN)
    GPIO.setup(ledPin, GPIO.OUT)

# アクションの実行
def doAction():
    GPIO.output(ledPin,GPIO.HIGH)
    sleep(1)
    GPIO.output(ledPin,GPIO.LOW)


if __name__ == "__main__":
    setupPins()
    buttonCounter=0
    while True:
        if 0==GPIO.input(buttonPin):
            buttonCounter=0
        else:
            buttonCounter+=1
        if buttonCounter >= buttonThreshold:
            buttonCounter=0
            doAction()
        sleep(loopWait)
