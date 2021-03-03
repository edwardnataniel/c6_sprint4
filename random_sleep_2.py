import random
from time import sleep

random.seed(1)

def delay():
	sec = random.randint(1, 5)
	print(f"Sleeping for {sec} second(s)")
	sleep(sec)
	
	
def main():
	for i in range(0,5):
		print(i)
		delay()
	
if __name__ == "__main__":
	main()