import sqlite3, multiprocessing
# 数据存储模块
def data_storer(parsed_data_queue, stop_event):
    conn = sqlite3.connect('parsed_data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS parsed_data (id INTEGER PRIMARY KEY, data TEXT)')
    while not stop_event.is_set():
        try:
            data = parsed_data_queue.get(timeout=1)  # 增加超时机制，避免死锁
            c.execute('INSERT INTO parsed_data (data) VALUES (?)', (data,))
            conn.commit()
        except multiprocessing.queues.Empty:
            continue
    conn.close()
