import multiprocessing, BeautifulSoup
# 数据解析模块
def data_parser(data_queue, parsed_data_queue, stop_event):
    while not stop_event.is_set():
        try:
            data = data_queue.get(timeout=1)
            soup = BeautifulSoup(data, 'html.parser')
            text = soup.get_text()
            parsed_data_queue.put(text)
        except multiprocessing.queues.Empty:
            continue