import sqlite3
# 种子URL管理模块
def manage_seed_urls():
    conn = sqlite3.connect('seed_urls.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS seed_urls (url TEXT PRIMARY KEY)')
    c.execute('INSERT OR IGNORE INTO seed_urls (url) VALUES (?)', ('https://www.douban.com/',))
    conn.commit()
    conn.close()

