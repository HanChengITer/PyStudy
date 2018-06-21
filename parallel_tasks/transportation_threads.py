from threading import Thread
import time, random

class Lighter(Thread):
	# red - 30s
	# yellow - 3s
	# green - 45s
	
	def change_color(self, old_color):
		time_interval, next_color = self.__change_dict[old_color]
		time.sleep(time_interval)
		self.color = next_color
	
	def start_work(self, initial_color):
		self.color = initial_color
		self.__change_dict = {
			# 'r':(30,'g'), 
			# 'y':(3,'r'), 
			# 'g':(45,'y'),
			'r':(4,'g'), 
			'y':(3,'r'), 
			'g':(5,'y'),
		}
		while True:
			self.change_color(self.color)
	
	def run(self):
		self.start_work('g')

class Car():
	def __init__(self, name):
		self.name = name
	
def main():
	lighter = Lighter()
	lighter.setDaemon(True)
	lighter.start()
	# join会让主线程同步阻塞，等待子线程
	# lighter.join()
	
	car_list = []
	brands_list = ['Aston Martin','Land Rover','Mazda','CADILLAC','Maybach',]
	for i in range(100):
		car_list.append(Car(random.choice(brands_list)))
	
	
	for i in range(100):
		car = random.choice(car_list)
		print('{} is preparing to cross the road'.format(car.name))
		print('current lighter color -> ', lighter.color)
		if lighter.color == 'g':
			print('{} please pass'.format(car.name))
		else:
			print('{} please wait'.format(car.name))
		print("")
		time.sleep(1)
	
main()