##多线程和队列的使用
翻译文章[原文链接](http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/)

本文详细讲解一下python线程的异步机制，我们将会学习到下面这些方向：锁，释放锁，信号量，条件，事件和队列，同样，我们将要探索一下python在网络应用中的机制

本文的源码可以从githua上下载到[下载地址](github.com/laurentluce/python-tutorials under threads/)

首先，我们看看简单的项目使用线程模块使用非同步运行

##线程

我们想写一个获取一些网络地址的内容使用一些url，并且把获取到的内容写入文件。我么可以使用简单的方法，这里我们不得不使用线程完成。我们将创建两个线程，各自处理每一个url

注意：最好的方式在这里将url的结果集放入队列，但是当前的这个例子练习线程和开始整项目。

定义类 FetchUrls ，他的基类是线程类，这个类处理在列表中的url地址，返回结果，将返回的结果写入到文件当中。

###代码查看sample_thread_fetch_url.py文件
这里有个问题是两个线程同时在写文件，结果会造成巨大的混乱。我们需要一种方式去让仅仅有一个线程在写文件，在同一时间。要做这些，我们使用一种同步的方式例如锁。

##锁

锁有两种状态：上锁和解锁，下面这个两个方法完成请求锁和释放锁acquire()和release()，使用场景如下：
  . 如果状态是解锁状态：调用acquire()，来改变状态和上锁
  . 如果状态是上锁状态：调用acquire()阻塞，直到其他的线程调用release()
  . 如果状态是解锁状态：调用release()将会返回一个RuntimeError的执行错误
  . 如果状态是上锁状态：调用release()来改变状到unlocked()

解决我们这个问题，连个线程同时向一个文件写东西，我们加上一个锁在类FetchUrls的构造函数，我们使用这个锁来保护文件写入操作。我仅仅做一些变动，这些代码就会变成线程加上锁的集合了

####代码查看sample_thread_fetch_url_lock.py

文件写入操作现在被一个锁保护起来，我们不能两个线程写文件在同一个时间

当前的代码在
