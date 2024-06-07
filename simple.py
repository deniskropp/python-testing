from jobsNqueues import Queue, Job

queue = Queue()
queue.push(Job(print, 'hello', end='\n'))
queue.push(Job(print, 'world', end='\n'))

while (not queue.empty()):
    job = queue.pop()
    job.run()
