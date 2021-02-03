# calendar api
import event

# memory database variable
events_dict = {}


def init():
	# initalizes the database
	
	global events_dict
	
	json_dict = load_data()
	# iterate over dict { year : dictionary{ jan, feb, .. , dec}
	for y_key,m_value in json_dict.items():
		events_dict[y_key] = {}
		for m_key, d_value in value:
			for d_key, h_value in d_value:
				for h_key, min_value in h_value:
					for min_key, s_value in min_value:
						for s_key, data in s_value:
							event_time = get_time(y_key,m_key,d_key,h_key,min_key,s_key)
							event = event.Event(data["name"], data["location", event_time)
							add_event(event)
	

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
		data[account_list[i].uid] = account_list[i].__dict__
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
		
		# make sure the structure is built from bottom to top
		date = event.get_full_date()
		
		if not events_dict.get(date[0]):
			events_dict[date[0]] = {}
		
		year_dict = events_dict[date[0]]		
		if not year_dict.get(date[1]):
			year_dict[date[1]] = {}

		month_dict = year_dict[date[1]]
		if not month_dict.get(date[2]):
			month_dict[date[2]] = {}
			
		day_dict = month_dict[date[2]]
		if not day_dict.get(date[3]):
			day_dict[date[3]] = {}
		
		hour_dict = day_dict[date[3]]
		if not hour_dict.get(date[4]):
			hour_dict[date[4]] = {}
		
		minute_dict = hour_dict[date[4]]
		if not minute_dict.get(date[5]):
			minute_dict[date[5]] = []
		
		events_dict[date[0]][date[1]][date[2]][date[3]][date[4]][date[5]].append(event)
		
	except ValueError:
		print("Null event given")
		



def get_event_by_time(data):
	year_events = []
	for m_key, d_value in events_dict[data[0]]:
			for d_key, h_value in d_value:
				for h_key, min_value in h_value:
					for min_key, s_value in min_value:
						for s_key, data in s_value:
							year_events.append(s_value)
	for i in range(len(data)):
		if not data[i]:
			break
		year_events = filter(lambda x: str(x.get_data(i + 1)) == str(data[i + 1]), year_events)
	
	return year_events
	
	
	
	
	
	
	
