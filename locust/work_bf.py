#!/usr/bin/python3
 
import sys, time, json, _thread
import http.client, urllib.parse
import requests

host = 'http://dlshop.weitshop.cn/?r=h5&shopid=7&from=h5#/shop/appGoods/list'

thread_count = 100  #并发数量
now_count = 0
error_count = 0
begin_time = ''
 
lock_obj = _thread.allocate()
 
def test_http_engine():
  global now_count
  global error_count
  global thread_count
  global begin_time
  conn = None
  if now_count == 0:
    begin_time = int(round(time.time() * 1000))
  try:
    response = requests.get(url=host)
    data = response.read()
    print (data)
 
    if json.dumps(response.status) != '200':
      error_count += 1;
      print ('error count: ' + str(error_count))
 
    sys.stdout.flush()
    now_count += 1
    if now_count == thread_count:
      print ('### error count: ' + str(error_count) + ' ###')
      print ('### begin time : ' + str(begin_time))
      print ('### end time  : ' + str(int(round(time.strftime() * 1000))))
 
  except Exception as e:
    print (e)
  finally:
    if conn:
      conn.close()
 
def test_thread_func():
  global now_count
  global lock_obj
  cnt = 0
 
  lock_obj.acquire()
  print ('')
  print ('=== Request: ' + str(now_count) + ' ===')
 
  cnt += 1
  test_http_engine()
  sys.stdout.flush()
  lock_obj.release()
 
 
def test_main():
  global thread_count
  for i in range(thread_count):
    _thread.start_new_thread(test_thread_func, ())

if __name__=='__main__':
  test_main()
  while True:
    time.sleep(5)