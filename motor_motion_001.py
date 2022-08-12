import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
l_f=gpio.setup(12,OUT)
l_b=gpio.setup(13,OUT)
E_l=gpio.setup(6,OUT)
r_f=gpio.setup(20,OUT)
r_b=gpio.setup(21,OUT)
E_r=gpio.setup(26,OUT)

def move_forward():
    gpio.output(E_l, gpio.HIGH)
    gpio.output(E_r, gpio.HIGH)
    gpio.output(l_f, gpio.HIGH)
    gpio.output(r_f, gpio.HIGH)

def move_backward():
    gpio.output(E_l, gpio.HIGH)
    gpio.output(E_r, gpio.HIGH)
    gpio.output(l_b, gpio.HIGH)
    gpio.output(r_b, gpio.HIGH)

def turn_left():
    gpio.output(E_l, gpio.HIGH)
    gpio.output(E_r, gpio.HIGH)
    gpio.output(l_f, gpio.LOW)
    gpio.output(r_f, gpio.HIGH)

def hard_left():
    gpio.output(E_l, gpio.HIGH)
    gpio.output(E_r, gpio.HIGH)
    gpio.output(l_b, gpio.HIGH)
    gpio.output(r_f, gpio.HIGH)

def turn_right():
    gpio.output(E_l, gpio.HIGH)
    gpio.output(E_r, gpio.HIGH)
    gpio.output(l_f, gpio.HIGH)
    gpio.output(r_f, gpio.LOW)

def hard_right():
    gpio.output(E_l, gpio.HIGH)
    gpio.output(E_r, gpio.HIGH)
    gpio.output(l_f, gpio.HIGH)
    gpio.output(r_b, gpio.HIGH)

def left_reverse():
    gpio.output(E_l,gpio.HIGH)
    gpio.output(E_r,gpio.HIGH)
    gpio.output(l_b, gpio.LOW)
    gpio.output(r_b, gpio.HIGH)

def hard_left_reverse():
    gpio.output(E_l,gpio.HIGH)
    gpio.output(E_r,gpio.HIGH)
    gpio.output(l_f,gpio.HIGH)
    gpio.output(r_b,gpio.HIGH)

move_forward()
time.sleep(3)
turn_left()
time.sleep(2)
move_forward()
time.sleep(2)
turn_right()
