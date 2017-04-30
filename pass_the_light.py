import radio
import random
from microbit import display, Image, button_a, sleep

# my_id is the id of this microbit.  Call id is the next microbit in the ordinal sequence
my_id = 'four'
call_id = 'one'
everyone_called = 'fire'

# Create the "flash" animation frames. Can you work out how it's done?
myflash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    # Button A sends a call to the next microbit in sequence.  Used to kick off program
    if button_a.was_pressed():
        radio.send(call_id)
    # Button B sends a call out to all other microbits to light up.
    if button_b.was_pressed():
        radio.send(everyone_called)
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == my_id or incoming == everyone_called:
        incoming = 'nothing'
        sleep(random.randint(50, 350))
        display.show(myflash, delay=100, wait=False)
        sleep(1000)
        radio.send(call_id)

