import time


class Event:
	
	def __init__(self, name, location, date = time.time()):
		self.name = name
		self.location = location
		self.__date = date


	def get_year_date():
		return [get_year(), get_month(), get_day()]
	
	def get_full_date():
		return [get_year(), get_month(), get_day(), get_hour(), get_minute(), get_second()]
	
	def get_year():
		return time.tm_year
	
	def get_month():
		return time.tm_mon
		
	def get_day():
		return time.tm_mday
	
	def get_hour():
		return time.tm_hour
		
	def get_minute():
		return time.tm_min

	def get_second():
		return time.tm_sec
	
	def get_hash():
		hash = str(get_year())
		if int(get_month) < 10:
			hash += '0'
		hash += str(get_month())
		if int(get_day()) < 10:
			hash += '0'
		hash += str(get_day())
		
		if int(get_hour()) < 10:
			hash += '0'
		hash += str(get_hour())
		if int(get_minute()) < 10:
			hash += '0'
		hash += str(get_minute())
		if int(get_second()) < 10:
			hash += '0'
		hash += str(get_second())
		return hash
		
	def get_data(index):
		return get_full_date()[index]
		
	def get_str():
		return '\n'.join(name,location, self.__date.strftime("%m/%d/%Y, %H:%M:%S"))