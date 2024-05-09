# Simple Tray

Make simple Python applications that live in the system tray!

## Dependencies

Run `pip install pyqt5`.

## Usage 
```py
import tray

class Tray(tray.Tray):
  def update(self):#called once on start() then again every tick
    #your code
    say='Update tooltip and send system notification'
    self.say(say,force=False)#without force, ignore if same as previous message

t=Tray('Application name','icon.webp',1*60)#update every minute
t.start()
```
