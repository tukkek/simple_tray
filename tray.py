import PyQt6.QtGui,PyQt6.QtWidgets,subprocess

class Tray:
  def __init__(self,name,icon,interval=1):
    self.application=PyQt6.QtWidgets.QApplication([])
    self.icon=PyQt6.QtWidgets.QSystemTrayIcon()
    self.menu=PyQt6.QtWidgets.QMenu()
    self.timer=PyQt6.QtCore.QTimer()
    self.said=False
    self.name=name
    self.status=self.act('')
    self.icon.activated.connect(lambda:self.menu.popup(PyQt6.QtGui.QCursor.pos()))
    self.icon.setIcon(PyQt6.QtGui.QIcon(icon))
    self.icon.setContextMenu(self.menu)
    self.timer.timeout.connect(self.update)
    self.timer.setInterval(interval*1000)
    self.separators=[]#disappear if trashed ¯\_(ツ)_/¯

  def say(self,message,force=False):
    if message==self.said and not force:
      return False
    subprocess.run(['notify-send',self.name,message])
    self.said=message
    self.icon.setToolTip(message)
    print(message)
    self.status.setText(message) 
    return True

  def update(self):
    raise Exception('Unimplemented update method.')
  
  def act(self,label):
    action=PyQt6.QtGui.QAction()
    action.setText(label) 
    self.menu.addAction(action)
    return action
    
  def start(self):
    quit=self.act('Quit')
    quit.triggered.connect(self.application.quit)
    self.application.setQuitOnLastWindowClosed(False) 
    self.update()
    self.icon.setVisible(True)
    self.timer.start()
    self.application.exec() 

  def separate(self):
    self.separators.append(self.act(''))
