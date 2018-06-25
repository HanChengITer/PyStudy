import asyncio, time, random

class Lighter():
	def __init__(self, initial_color):
		self.color = initial_color
	
	@asyncio.coroutine
	def start_work(self):
		__change_dict = {
			# 'r':(30,'g'), 
			# 'y':(3,'r'), 
			# 'g':(45,'y'),
			'r':(4,'g'), 
			'y':(3,'r'), 
			'g':(5,'y'),
		}
		while True:
			time_interval, next_color = __change_dict[self.color]
			yield from asyncio.sleep(time_interval)
			self.color = next_color


class Car():
	def __init__(self, name):
		self.name = name

@asyncio.coroutine
def car_comming(lighter):
	car_list = []
	brands_list = ['Aston Martin','Land Rover','Mazda','CADILLAC','Maybach',]
	for i in range(100):
		car_list.append(Car(random.choice(brands_list)))
	
	for i in range(100):
		current_car = random.choice(car_list)
		print(current_car.name, lighter.color)
		car_run(current_car, lighter.color)
		yield from asyncio.sleep(1)

		
def car_run(current_car, current_color):
	print('current color ->', current_color)
	if current_color == 'g':
		print('{} please pass'.format(current_car.name))
	else:
		print('{} please wait'.format(current_car.name))
	print("")

def main():
	lighter = Lighter(initial_color='g')

	loop = asyncio.get_event_loop()
	
	tasks = [
		asyncio.ensure_future(lighter.start_work()),
		asyncio.ensure_future(car_comming(lighter)),
		
	]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
	
main()