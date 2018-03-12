import time
import sched


# 第一个工作函数
# 第二个参数 @starttime 表示任务开始的时间
# 很明显参数在建立这个任务的时候就已经传递过去了，至于任务何时开始执行就由调度器决定了
def worker(msg, starttime):
    print(u"任务执行的时刻", time.time(), "传达的消息是", msg, '任务建立时刻', starttime)

if __name__=='__main__':
    # 创建一个调度器示例
    # 第一参数是获取时间的函数，第二个参数是延时函数
    # print(u'----------  两个简单的例子  -------------')
    # print(u'程序启动时刻：', time.time())
    s = sched.scheduler(time.time, time.sleep)
    # s.enter(1, 1, worker, ('hello', time.time()))
    # s.enter(30, 1, worker, ('world', time.time()))
    # s.run()  # 这一个 s.run() 启动上面的两个任务
    # print(u'睡眠２秒前时刻：', time.time())
    # time.sleep(2)
    # print(u'睡眠２秒结束时刻：', time.time())

    # 　重点关注下面２个任务，建立时间，启动时间
    # ２个任务的建立时间都很好计算，但有没有发现 "hello world [3]"　的启动时间比建立时间晚　１３　秒，
    # 这不就是２个 sleep　的总延时吗？所以说启动时间并不一定就是 delay　能指定的，还需要看具体的程序环境，
    # 如果程序堵塞的很厉害，已经浪费了一大段的时间还没有到 scheduler 能调度这个任务，当 scheduler 能调度这个
    # 任务的时候，发现 delay 已经过去了， scheduler 为了弥补“罪过”，会马上启动这个任务。

    # 任务 "hello world [15]" 就是一个很好的例子，正常情况下，程序没有阻塞的那么厉害，在scheduler　能调度这个任务的时候
    # 发现 delay 还没到就等待，如果 delay　时间到了就可以在恰好指定的延时调用这个任务。
    print(u'\n\n----------  两个复杂的例子  -------------')
    s.enter(3, 1, worker, ('hello world [3]', time.time()))
    print(u'睡眠７秒前时刻：', time.time())
    time.sleep(7)
    print(u'睡眠７秒结束时刻：', time.time())

    s.enter(15, 1, worker, ('hello world [15]', time.time()))
    print(u'睡眠６秒前时刻：', time.time())
    time.sleep(6)
    print(u'睡眠６秒结束时刻：', time.time())

    s.run()  # 过了2秒之后，启动另外一个任务

    print(u'程序结束时刻', time.time())




