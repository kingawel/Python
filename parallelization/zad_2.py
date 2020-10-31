from random import randint
import threading
import time
class Philosopher(threading.Thread):

	def __init__(self, name, leftFork, rightFork): #constructor
		print("Philosopher {} came".format(name))
		threading.Thread.__init__(self, name = name)
		self.rightFork = rightFork
		self.leftFork = leftFork
	def run(self):
		print("{} IS thinking\n".format(threading.currentThread().getName()))
		while True:
			time.sleep(randint(1,9)) #random time while philosopher is thinking
			print("{} STOP thinking\n".format(threading.currentThread().getName()))
			self.leftFork.acquire() #acquire() changes state from unlocked to locked - let philosoph to take fork
			time.sleep(randint(1,9))
			try:
				print("{} TOOK left fork\n".format(threading.currentThread().getName()))			
				self.rightFork.acquire() 
				try:
					print("{} TOOK two fork, he is EATING\n".format(threading.currentThread().getName()))
				finally:
					self.rightFork.release() #release () changes state to unlocked
					print("{} PUT AWAY right fork\n".format(threading.currentThread().getName()))
			finally:
				self.leftFork.release()
				print("{} PUT AWAY left fork\n".format(threading.currentThread().getName()))

fork1 = threading.RLock()
fork2 = threading.RLock()
fork3 = threading.RLock()
fork4 = threading.RLock()
fork5 = threading.RLock()

ph1 = Philosopher("John", fork1, fork2)
ph2 = Philosopher("Paul", fork2, fork3)
ph3 = Philosopher("Tom", fork3, fork4)
ph4 = Philosopher("Jacob", fork4, fork5)
ph5 = Philosopher("Philip", fork5, fork1)

ph1.start()
ph2.start()
ph3.start()
ph4.start()
ph5.start()





