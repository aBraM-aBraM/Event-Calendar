import time


class Event:
	
	def __init__(self, name, location, date):
		self.name = name
		self.location = location
		self.__date = date


	def get_full_date(self):
		return [self.get_year(), self.get_month(), self.get_day(), self.get_hour(), self.get_minute(), self.get_second()]
	
	def get_year(self):
		return self.__date.tm_year
	
	def get_month(self):
		return self.__date.tm_mon
		
	def get_day(self):
		return self.__date.tm_mday
	
	def get_hour(self):
		return self.__date.tm_hour
		
	def get_minute(self):
		return self.__date.tm_min

	def get_second(self):
		return self.__date.tm_sec
	
	def get_hash(self):
		hash = str(self.get_year())
		if int(self.get_month()) < 10:
			hash += '0'
		hash += str(self.get_month())
		if int(self.get_day()) < 10:
			hash += '0'
		hash += str(self.get_day())
		
		if int(self.get_hour()) < 10:
			hash += '0'
		hash += str(self.get_hour())
		if int(self.get_minute()) < 10:
			hash += '0'
		hash += str(self.get_minute())
		if int(self.get_second()) < 10:
			hash += '0'
		hash += str(self.get_second())
		hash += '|'
		hash += self.name
		hash += '|'
		hash += self.location
		return hash
		
	def get_data(self, index):
		return get_full_date()[index]
		
	def get_str(self):
		return '\n'.join([self.name,self.location, '/'.join(self.get_full_date())])