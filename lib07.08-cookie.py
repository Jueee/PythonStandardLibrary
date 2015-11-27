'''
cookie 模块


'''
# 使用 cookie 模块
import http.cookiejar
import os, time

cookie = http.cookiejar.CookieJar()
cookie['user'] = 'Mimi'
cookie['timestamp'] = time.time()

print(cookie)
