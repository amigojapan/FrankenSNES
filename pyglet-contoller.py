#!./pythonvirtualenv/bin/python3
import pyglet
import serial

# Initialize serial port
# Using a typical Linux serial port; adjust '/dev/ttyUSB0' and baud rate (9600) as needed
ser = serial.Serial('/dev/tty0', 9600)

# Create a Pyglet window with the same dimensions and caption as the original Pygame program
window = pyglet.window.Window(width=400, height=300, caption="Keyboard Event Monitor")

# Set the background color to white, matching the Pygame program's behavior
#window.set_clear_color((1, 1, 1, 1))  # RGBA values for white

# Event handler for key press
@window.event
def on_key_press(symbol, modifiers):
    print(f"Key {symbol} pressed")
    # Send a character 'P' through the serial port on key press
    #65507      left control
    #65513      left alt
    #120 x key
    #121 y key
    #108 l key
    #114 r key
    #65293      enter key
    #32  space key
    #65361 left key
    #65363 right key
    #65362 up key
    #65364 down key
    if(symbol==65507):
        ser.write(b'A')
        print("Left pressed 'A'")
    elif(symbol==65513):
        ser.write(b'B')
        print("Right pressed 'B'")
    elif(symbol==120):
        ser.write(b'X')
        print("Left pressed 'X'")
    elif(symbol==121):
        ser.write(b'Y')
        print("Right pressed 'Y'")
    elif(symbol==65361):
        ser.write(b'L')
        print("Left pressed 'L'")
    elif(symbol==65363):
        ser.write(b'R')
        print("Right pressed 'R'")
    elif(symbol==65362):
        ser.write(b'U')
        print("Up pressed 'U'")
    elif(symbol==65364):
        ser.write(b'D')
        print("Up pressed 'D'")
    elif(symbol==108):
        ser.write(b'Q')
        print("Left pressed 'Q'")
    elif(symbol==114):
        ser.write(b'W')
        print("Right pressed 'W'")
    elif(symbol==65293):
        ser.write(b'S')
        print("Left pressed 'S'")
    elif(symbol==32):
        ser.write(b'Z')
        print("Right pressed 'Z'")

# Event handler for key release
@window.event
def on_key_release(symbol, modifiers):
    print(f"Key {symbol} released")
    # Send a character 'R' through the serial port on key release
    if(symbol==65507):
        ser.write(b'1')
        print("Left pressed '1'")
    elif(symbol==65513):
        ser.write(b'2')
        print("Right pressed '2'")
    elif(symbol==120):
        ser.write(b'3')
        print("Left pressed '3'")
    elif(symbol==121):
        ser.write(b'4')
        print("Right pressed '4'")
    elif(symbol==65361):
        ser.write(b'5')
        print("Left pressed '5'")
    elif(symbol==65363):
        ser.write(b'6')
        print("Right pressed '6'")
    elif(symbol==65362):
        ser.write(b'7')
        print("Up pressed '7'")
    elif(symbol==65364):
        ser.write(b'8')
        print("Up pressed '8'")
    elif(symbol==108):
        ser.write(b'Q')
        print("Left pressed 'O'")
    elif(symbol==114):
        ser.write(b'W')
        print("Right pressed 'I'")
    elif(symbol==65293):
        ser.write(b'S')
        print("Left pressed '9'")
    elif(symbol==32):
        ser.write(b'Z')
        print("Right pressed 'P'")

# Event handler for drawing to keep the window responsive
@window.event
def on_draw():
    pass
##    print("")
##    window.clear()

# Run the Pyglet application
pyglet.app.run()