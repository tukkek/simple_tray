# Simple Tray

## Usage 
```py
import tray

class Tray(tray.Tray):
  '''
  called once on start()
  then again every tick
  '''
  def update(self):
    # your code
    say='Update tooltip and send system notification'
    self.say(say,force=False) #without force, ignore if same as previous message

t=Tray('Application name','icon.webp',1*60) #update every minute
t.start()
```
