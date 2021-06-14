import subprocess as sp 

programname = 'Notepad.exe'
filename = 'Mynotes.txt'

sp.Popen([programname,filename])
