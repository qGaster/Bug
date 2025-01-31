import multiprocessing
import time
import url_queue_manager
import manage_seed_urls
import url_distributor
import data_crawler
import data_parser
import data_storer
def main():
    url_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()
    data_queue = multiprocessing.Queue()
    parsed_data_queue = multiprocessing.Queue()
    stop_event = multiprocessing.Event()

    manage_seed_urls()
    url_queue_manager(url_queue)

    with multiprocessing.Pool(processes=4) as pool:
        # 分发URL
        pool.apply_async(url_distributor, (url_queue, result_queue, stop_event))
        # 爬取数据
        pool.apply_async(data_crawler, (result_queue, data_queue, stop_event))
        # 解析数据
        pool.apply_async(data_parser, (data_queue, parsed_data_queue, stop_event))
        # 存储数据
        pool.apply_async(data_storer, (parsed_data_queue, stop_event))
        time.sleep(10)  # 给足够的时间让进程工作
        stop_event.set()
        pool.close()
        pool.join()
if __name__ == '__main__':
    main()
