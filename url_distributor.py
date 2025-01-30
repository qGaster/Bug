import multiprocessing
# URL分发模块
def url_distributor(url_queue, result_queue, stop_event):
    while not stop_event.is_set():
        try:
            url = url_queue.get(timeout=1)
            result_queue.put(url)
        except multiprocessing.queues.Empty:
            continue