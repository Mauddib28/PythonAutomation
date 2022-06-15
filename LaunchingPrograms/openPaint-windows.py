#! python3

import subprocess

paintProc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')

paintProc.poll() == None

paintProc.wait() 	# Doesn't reutnr unitl MS Paint closes

paintProc.poll()
