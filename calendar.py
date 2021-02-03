# calendar api
import event
import os
import time
import json

# memory database variable
events_dict = {}
database_path = 'database.txt'

def init():
	# initalizes the database
	
	global events_dict
	
	json_dict = load_data()
	# iterate over dict { year : dictionary{ jan, feb, .. , dec}
	if json_dict:
		for key,value in json_dict.items():
			event_time = get_time(value["_Event__date"][0],
			value["_Event__date"][1],value["_Event__date"][2],value["_Event__date"][3],
			value["_Event__date"][4],value["_Event__date"][5])
			new_event = event.Event(value["name"], value["location"], event_time)
			events_dict[key] = new_event

def load_data(data_path=database_path):
	# returns data from file as a dictionary
	if os.path.exists(data_path):
		raw_data = open(data_path,'r+').read()
	if not raw_data:
		return None
	return json.loads(raw_data)

def save_data(data_path=database_path):
	# saves data appropriately as json
	data = {}
	for key, value in events_dict.items():
		data[key] = value.__dict__
	open(data_path,'w+').write(json.dumps(data))

def get_time(year, month, day, hour, minute, second):
	# creates an instance of time with specified values
	t = time.struct_time((
	year,
	month,
	day,
	hour,
	minute,
	second,
	3,
	3,
	0
	))
	return t

def add_event_manual(name, location, year, month, day, hour, minute, second):
	event_time = get_time(year,month,day,hour,minute,second)
	new_event = event.Event(name, location, event_time)
	add_event(new_event)

def add_event(new_event):
	# adds an event to the calendar
	try:
		if not new_event:
			raise ValueError
		
		# get event key
		hash = new_event.get_hash()
		
		events_dict[hash] = new_event
		
	except ValueError:
		print("Null event given")
		



def get_event_by_time(data):
	hash = ''
	for i in range(len(data)):
		if not data[i]:
			break
		if i and int(data[i]) < 10:
			hash += '0'
		hash += data[i]
	events = []
	for key, value in events_dict.items():
		if hash in key:
			events.append(value)
	return events
	
	
	
	
	
	
