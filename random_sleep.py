from time import sleep

def delay(seconds):
	print(f"Sleeping for {seconds} second(s)")
	sleep(seconds)
	
def main():
	for i in range(0,5):
		print(i)
		delay(seconds=2)
	
if __name__ == "__main__":
	main()