#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import RPi.GPIO as GPIO

# ピン番号
# ボタン : GPIO 20  (ピン番号38)
# LED    : GPIO 16  (ピン番号36)
buttonPin = 20
ledPin = 16

# ボタンをチェックするループの待ち時間
loopWait = 0.1

# ボタンをONと判定する閾値
buttonThreshold=5

# ピンのセットアップ
def setupPins():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN)
    GPIO.setup(ledPin, GPIO.OUT)

# アクションの実行
def doAction():
    GPIO.output(ledPin,GPIO.HIGH)
    sleep(2)
    GPIO.output(ledPin,GPIO.LOW)

# メインループ
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
