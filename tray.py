import PyQt6.QtGui,PyQt6.QtWidgets,subprocess

class Tray:
  def __init__(self,name,icon,interval=1):
    self.application=PyQt6.QtWidgets.QApplication([])
    self.icon=PyQt6.QtWidgets.QSystemTrayIcon()
    self.menu=PyQt6.QtWidgets.QMenu()
    self.timer=PyQt6.QtCore.QTimer()
    self.said=False
    self.name=name
    self.icon.activated.connect(lambda:self.menu.popup(PyQt6.QtGui.QCursor.pos()))
    self.icon.setIcon(PyQt6.QtGui.QIcon(icon))
    self.icon.setContextMenu(self.menu)
    self.timer.timeout.connect(self.update)
    self.timer.setInterval(interval*1000)

  def say(self,message,force=False):
    if force or message!=self.said:
      subprocess.run(['notify-send',self.name,message])
      self.said=message
      self.icon.setToolTip(message)
      print(message)

  def update(self):
    raise Exception('Unimplemented update method.')
    
  def start(self):
    q=PyQt6.QtGui.QAction()
    q.triggered.connect(self.application.quit) 
    q.setText('Quit') 
    self.menu.addAction(q)
    self.application.setQuitOnLastWindowClosed(False) 
    self.update()
    self.icon.setVisible(True)
    self.timer.start()
    self.application.exec() 
