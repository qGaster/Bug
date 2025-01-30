import get_random_proxy, multiprocessing, requests
# 数据爬取模块
def data_crawler(result_queue, data_queue, stop_event):
    while not stop_event.is_set():
        try:
            url = result_queue.get(timeout=1)
            proxy = get_random_proxy()
            try:
                response = requests.get(url,proxies=proxy, timeout=10)
                print(response.status_code)
                if response.status_code == 200:
                    data_queue.put(response.text)
            except Exception as e:
                print(f"Error crawling {url}: {e}")
        except multiprocessing.queues.Empty:
            continue