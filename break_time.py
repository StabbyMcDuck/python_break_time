import time
import webbrowser

count = 0
total_breaks = 3

while (count < total_breaks):
  time.sleep(10)
  print 'Time to take a break!'
  webbrowser.open("https://youtu.be/sOS9aOIXPEk")
  count = count + 1
