from multiprocessing import Process, Manager
import time, random

class Car():
	def __init__(self, name):
		self.name = name

def change_color(shared_ns, change_dict):
	time_interval, next_color = change_dict[shared_ns.color]
	time.sleep(time_interval)
	shared_ns.color = next_color
	
def start_work( shared_ns, change_dict):
	while True:
		change_color(shared_ns, change_dict)

# def main():
# The "freeze_support()" line can be omitted if the program
	# 启动进程时，必须在if __name__ == '__main__': 方法中
if __name__ == '__main__':

	change_dict = {
		# 'r':(30,'g'), 
		# 'y':(3,'r'), 
		# 'g':(45,'y'),
		'r':(4,'g'), 
		'y':(3,'r'), 
		'g':(5,'y'),
	}
	
	shared_ns = Manager().Namespace()
	shared_ns.color = 'g'
	
	lighter_process = Process(target=start_work, args=(shared_ns, change_dict) )
	
	lighter_process.start()
	# join会让父进程同步阻塞，等待子进程
	# lighter_process.join()
	# AttributeError: 'ForkAwareLocal' object has no attribute 'connection'
		# https://www.cnblogs.com/wangqiaomei/p/5682669.html
		# 主进程停止了，子进程要访问主进程的变量，则会报此错误
		# 主进程和子进程都在执行，主进程里有个字典，子进程要修改这个字典。
		# 进程和进程之间要通信的话，需要创建连接的。相当于两边都写上一个socket，进程之间通过连接进行操作。
		# 主进程执行到底部，说明执行完了，会把它里面的连接断开了。
		# 主进程把连接断开了，子进程就连接不上主进程。
		# 如果在底部写停10秒，主进程就停止下来，并没有执行完。主进程没有执行完，连接还没有断开，那子进程就可以连接它了。
	
	car_list = []
	brands_list = ['Aston Martin','Land Rover','Mazda','CADILLAC','Maybach',]
	for i in range(100):
		car_list.append(Car(random.choice(brands_list)))
	
	for i in range(100):
		car = random.choice(car_list)
		print('{} is preparing to cross the road'.format(car.name))
		print('current lighter color -> ', shared_ns)
		if shared_ns.color == 'g':
			print('{} please pass'.format(car.name))
		else:
			print('{} please wait'.format(car.name))
		print("")
		time.sleep(1)
	
# main()