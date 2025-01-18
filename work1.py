from random import randint
from queue import Queue
from time import sleep

q = Queue()

def generate_request():
    num = randint(1, 100)
    application = f"Заявка {num}"
    q.put(application)
    print(f"Нова заяква створена {application}")
     
def process_request():
    if not q.empty():
        curr_q = q.get()
        sleep(1)
        print(f"Обробляється заявка {curr_q}...")
    else:
        print("Черга пуста")
            
def main():
    print("Система обробки заявок запущена. Натисніть Ctrl+C для завершення.")
    try:
        while True:
            generate_request()
            sleep(2)
            process_request()       
    except KeyboardInterrupt:
        print("\n Система обробки заявок зупинена.")

           
if __name__ == "__main__":
    main()        

