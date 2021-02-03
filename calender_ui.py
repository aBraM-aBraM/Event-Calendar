import calendar 
import os

QUIT_VALUE = -1
SKIP_VALUE = -2

menu_str = ["Calendar","=======", "Add Event [0]", "Get Event by Time [1]", "Exit [2]"]
add_event_str = "Add Event"
action_add_str = ["Name: ", "Location: ", "Year: ","Month: ","Day: ","Hour: ","Minute: ","Second: "]
action_time_str = ["Year: ","Month: ","Day: ","Hour: ","Minute: ","Second: "]

def cls():
	os.system('cls')

def between(a, x, z):
	return x >= a and x <= z

def add_event_ui():
	cls()
	print (add_event_str)
	data = ['y','m','d','h','min','s']
	action_step = 0
	while True:
		input_data = input(action_add_str[action_step])
		if input_data == str(QUIT_VALUE):
			# if user wants he can exit to main menu
			return
		if input_data:
			if action_step < 2:
				data[action_step] = input_data
				action_step += 1
			elif input_data.isdigit():
				data[action_step] = input_data
				bool = action_step == 3 and between(1,input_data,12)
				bool = bool or action_step == 4 and between(1, input_data, 31)
				bool = bool or action_step == 5 and between(0, input_data, 23)
				bool = bool or action_step == 6 and between(0, input_data, 59)
				bool = bool or action_step == 7 and between(0, input_data, 61)
				if bool:
					action_step += 1
				else:
					data[action_step] = ''
		if action_step == 8:
			calendar.add_event(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])

def event_by_time_ui():
	action_step = 0
	data = [None,None,None,None,None,None]
	while True:
		cls()
		print("Get Events by Time")
		input_data = input(action_time_str[action_step])
		if input_data == str(QUIT_VALUE):
			# if user wants he can exit to main menu
			return
		if input_data = str(SKIP_VALUE):
			return calendar.get_event_by_time(data)
		if input_data:
			if input_data.isdigit():
				data[action_step] = input_data
				bool = action_step == 1 and between(1,input_data,12)
				bool = bool or action_step == 2 and between(1, input_data, 31)
				bool = bool or action_step == 3 and between(0, input_data, 23)
				bool = bool or action_step == 4 and between(0, input_data, 59)
				bool = bool or action_step == 5 and between(0, input_data, 61)
				if bool:
					action_step += 1
				else:
					data[action_step] = None
		if action_step == 6:
			return calendar.get_event_by_time(data)

def menu_ui():
	
	while True:
		cls()
		print('\n'.join(menu_str))
		input_data = input()
		if input_data == str(QUIT_VALUE):
			break
		if input_data == 0:
			add_event_ui()
		if input_data == 1:
			event_by_time_ui()
		if input_data == 2;
			calendar.save_data()
			break