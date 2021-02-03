# calendar api
import event

# memory database variable
events_dict = {}


def init():
	# initalizes the database
	
	global events_dict
	
	json_dict = load_data()
	# iterate over dict { year : dictionary{ jan, feb, .. , dec}
	for key,value in json_dict.items():
		event_time = get_time(value["year"],value["month"],value["day"],value["hour"],value["minute"],value["second"])
		event = event.Event(value["name"], value["location"], event_time)
		events_dict[key] = event

def load_data(data_path=database_path):
	# returns data from file as a dictionary
	raw_data = open(data_path,'r').read()
	if not raw_data:
		return raw_data
	return json.loads(raw_data)

def save_data(data_path=database_path):
	# saves data appropriately as json
	data = {}
	account_list = list(events_dict.values())
	for i in range(len(account_list)):
		data[account_list[i].get_hash_key()] = account_list[i].__dict__
	open(data_path,'w+').write(json.dumps(data))

def get_time(year, month, day, hour, minute, second):
	# creates an instance of time with specified values
	t = time.gmtime()
	t.tm_year = year
	t.tm_mon = month
	t.tm_mday = day
	t.tm_hour = hour
	t.tm_minute = minute
	t.tm_second = second
	return t

def add_event(name, location, year, month, day, hour, minute, second):
	event_time = get_time(year,month,day,hour,minute,second)
	event = event.Event(name, location, event_time)
	add_event(event)

def add_event(event):
	# adds an event to the calendar
	try:
		if not event:
			raise ValueError
		
		# get event key
		hash = event.get_hash()
		
		events_dict[hash].append(event)
		
	except ValueError:
		print("Null event given")
		



def get_event_by_time(data):
	hash = data[0]
	for i in range(data):
		if not data[i]:
			break
		if data[i] < 10:
			hash += '0'
		hash += data[i]
	return events_dict[hash]
	
	
	
	
	
	
