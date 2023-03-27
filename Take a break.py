import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
i = 0
while i < 3 :
    time.sleep(2*60*60)
    webbrowser.open("www.youtube.com/watch?v=dQw4w9WgXcQ")
    i+=1