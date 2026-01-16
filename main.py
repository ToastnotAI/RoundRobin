from modules.Scheduler import Scheduler
from modules.Process import Process

processes = [
    Process("Process1", 10),
    Process("Process2", 15),
    Process("Process3", 20),
    Process("Process4", 3),
    Process("Process5", 8)]

scheduler = Scheduler()
for process in processes:
    scheduler.add_process(process)

lastLength = scheduler.size 
while scheduler.get_current() is not None:
    currentProcess = scheduler.get_current()
    print(f"Current Process: {currentProcess}")
    x = input("Press Enter to step through the scheduler, or type 'kill to kill the current process: ")
    if x.lower() == 'kill':
        killed_process = scheduler.kill_current()
        print(f"Killed Process: {killed_process}")
    if scheduler.size != lastLength:
        print(f"\nProcess Complete. {str(scheduler)}\n")
        lastLength = scheduler.size
    

    scheduler.step()

