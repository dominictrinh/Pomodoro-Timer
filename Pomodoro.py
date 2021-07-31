import tkinter as tk
from tkinter import messagebox

import time
import datetime
from datetime import date, time, datetime, timedelta

#grabs current time
current_time = datetime.now()

#pomodoro time
pomodoro_time = 25*60

#the difference between current time and pomodoro time, delta
difference_time = timedelta(0, pomodoro_time)

#time when the pomodoro ends
end_time = current_time + difference_time

#break time
break_time = 5*60

#final time
final_timme = current_time + timedelta(0, pomodoro_time + break_time)

#the gui we will be using, which is a message box
root = tk.Tk()
root.withdraw()
messagebox.showinfo("The pomodoro clock has begun,", "\nThe current time is " + current_time.strftime("%I:%M") + "\n Timer has been set for 25 minutes.")

#keep track of the pomodoros and the breaks we have gone through
total_pomodoros = 0
total_breaks = 0

while (True):

	#the logic of our timer is stored in a while loop
	#if the current time is less than our end time, that means we are still in the pomodoro cycle
	if current_time < end_time:
		print("Pomodoro in progress.")

	#if we are still in our pomodoro cycle, and less than the final time of our cycle + breaks, combined, we are in a break
	elif end_time <= current_time <= final_time:
		print("in break")
		if total_breaks == 0:
			print("if break")

			#alarm sound
			for i in range(3):
				pass

			print("Break in progress.")
			total_breaks += 1
	#first cycle is done, prompts user if they would like to go through one again
	else:
		print("Finished")

		#reset our breaks
		total_breaks = 0


		#asks if the user would like to go through another cycle
		answer = messagebox.askyesno("The pomodoro cycle has finished, would you like to go again?")
		total_pomodoros += 1

		#check to see if user said yes or no, and respond accordingly
		if answer == True:
			current_time = dt.datetime.now()
			end_time = current_time + difference_time
			final_timme = current_time + dt.timedelta(0, pomodoro_time + break_time)
			continue 

		elif answer == False:
			messagebox.showinfo("The pomodoro cycle has finished.")
			break_time

	#updates the timer
	time.sleep(1)
	current_time = dt.datetime.now()
	display = current_time.strftime("%H:%M")






