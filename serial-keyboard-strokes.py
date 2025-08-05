import tkinter as tk
import serial
import serial.tools.list_ports

class SerialKeyboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Serial Keyboard Sender")
        
        # Find available serial ports
        self.ports = [port.device for port in serial.tools.list_ports.comports()]
        if not self.ports:
            print("No serial ports found!")
            self.serial_port = None
        else:
            # Use first available port
            try:
                self.serial_port = serial.Serial(self.ports[0], 9600, timeout=1)
                print(f"Connected to {self.ports[0]}")
            except serial.SerialException:
                print("Failed to connect to serial port")
                self.serial_port = None

        # Initialize set for pressed keys
        self.pressed_keys = set()

        # Create text entry
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(padx=10, pady=10)
        
        # Bind keyboard events
        self.entry.bind("<KeyPress>", self.on_key_down)
        self.entry.bind("<KeyRelease>", self.on_key_up)
        
        # Status label
        self.status = tk.Label(root, text="Type in the box above")
        self.status.pack(pady=5)
        
        # Focus on entry
        self.entry.focus_set()

    def on_key_down(self, event):
        if event.char and event.char not in self.pressed_keys:
            self.pressed_keys.add(event.char)
            if self.serial_port and self.serial_port.is_open:
                message = f"DOWN:{event.char}\n"
                try:
                    self.serial_port.write(message.encode())
                    print(f"DOWN:{event.char}")
                    self.status.config(text=f"Sent DOWN: {event.char}")
                except serial.SerialException:
                    print("Serial write error")
                    self.status.config(text="Serial write error")
        # Ignore repeat events

    def on_key_up(self, event):
        if event.char and event.char in self.pressed_keys:
            self.pressed_keys.remove(event.char)
            if self.serial_port and self.serial_port.is_open:
                message = f"UP:{event.char}\n"
                try:
                    self.serial_port.write(message.encode())
                    print(f"UP:{event.char}")
                    self.status.config(text=f"Sent UP: {event.char}")
                except serial.SerialException:
                    print("Serial write error")
                    self.status.config(text="Serial write error")

    def __del__(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialKeyboardApp(root)
    root.mainloop()
