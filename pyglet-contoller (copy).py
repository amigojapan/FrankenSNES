import pyglet

# Create a Pyglet window with the same dimensions and caption as the original Pygame program
window = pyglet.window.Window(width=400, height=300, caption="Keyboard Event Monitor")

# Set the background color to white, matching the Pygame program's behavior
#window.set_clear_color((1, 1, 1, 1))  # RGBA values for white

# Event handler for key press
@window.event
def on_key_press(symbol, modifiers):
    print(f"Key {symbol} pressed")

# Event handler for key release
@window.event
def on_key_release(symbol, modifiers):
    print(f"Key {symbol} released")

# Event handler for drawing to keep the window responsive
@window.event
def on_draw():
	pass
##	print("")
##    window.clear()

# Run the Pyglet application
pyglet.app.run()
