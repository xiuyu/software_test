import requests,time,threading,json

THREAD_NUM = 100  # 并发线程总数
ONE_WORKER_NUM = 100  # 每个线程的循环次数
LOOP_SLEEP = 0  # 每次请求时间间隔(秒)
ERROR_NUM = 0  # 出错数

class press (object):
    headers = {
        "Content-type":"application/json"
    }
    def __init__(self,url,userName = "",password = ""):
        self.url = url
        self.userName = userName
        self.password = password
        self.session = requests.Session()
        self.session.headers = self.headers


    def testinterface(self):
        '''压测接口'''
        global ERROR_NUM
        try:
            data = {"userName": self.userName, "password": self.password}
            res = self.session.post(self.url,json.dumps(data))
            print(res.json())
            if res.json().get('code') != "0000":
                ERROR_NUM += 1
        except Exception as e:
            print(e)
            ERROR_NUM += 1

    def testonework(self):
        '''一次并发处理单个任务'''
        i = 0
        while i < ONE_WORKER_NUM:
            i += 1
            self.testinterface()
            time.sleep(LOOP_SLEEP)

    def run(self):
        '''使用多线程进程并发测试'''
        t1 = time.time()
        threads = []

        for i in range(THREAD_NUM):
            t = threading.Thread(target=self.testonework, name="T" + str(i))
            t.setDaemon(True)
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()


        t2 = time.time()

        print("===============压测结果===================")
        print("URL:", self.url)
        print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
        print("总耗时(秒):", t2 - t1)
        print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
        print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
        print("错误数量:", ERROR_NUM)



