from modules.Scheduler import Scheduler
from modules.Process import Process

processes = [
    Process("Process1", 10),
    Process("Process2", 15),
    Process("Process3", 20),
    Process("Process4", 5),
    Process("Process5", 8)]

scheduler = Scheduler()
for process in processes:
    scheduler.add_process(process)

lastLength = scheduler.processList.size 
while scheduler.get_current() is not None:
    if scheduler.processList.size != lastLength:
        print(f"\nProcess Complete. {str(scheduler)}\n")
        lastLength = scheduler.processList.size
    currentProcess = scheduler.get_current()
    print(f"Current Process: {currentProcess}")

    scheduler.step()

