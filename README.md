# Python-scrapy

## 准备
* [关于Scrapy](http://scrapy-chs.readthedocs.org/zh_CN/1.0/intro/overview.html)

* [安装Scrapy](http://poly.emptystack.net/python/scrapy/installation/)

安装过程有点麻烦，主要我们在安装Python的时候，有可能你系统是64位，但是却安装了32位的Python，导致你后来安装Python的库都选择64位，其实应该是32位。

## 运行

* 下载整个工程

* cd 进入包含spiders文件夹的目录

* cmd中输入：scrapy crawl meizitu

##  [妹子]图片

先看 [妹子图](http://www.meizitu.com/),这么多好看的图,拔下来慢慢玩。
![](http://7xrl8j.com1.z0.glb.clouddn.com/1.jpg)

### Scrapy

一般的写法也可以爬图片，这次为了体验一下 爬虫神奇，选择了 Scrapy 这个大杀器,好处自然多多的，起码不用担心被封，总之很多不必要的麻烦都不用去考虑了,最重要的是它为**爬虫**而生。

### 说明

本来练手 Scrapy 去爬妹子图，google了一下，早就有人写出来了, [地址在这里](https://segmentfault.com/a/1190000003870052),我的爬虫基本上都是 Copy的。但是走了一遍逻辑，分析了页面构造。

### 分析1

* 进入妹子官网，其地址栏 URL 为 meizitu.com:

![](http://7xrl8j.com1.z0.glb.clouddn.com/2.jpg)

没错红色的URL地址，即为第一张那个妹子的**系列图片**,我们肯定要获取这个 URL,点击该 URL，页面如下：

! [](http://7xrl8j.com1.z0.glb.clouddn.com/0.jpg)

没错，这个页面都是这个妹子的图片，查看源码获得图片链接即最后要下载的：

![](http://7xrl8j.com1.z0.glb.clouddn.com/5.jpg)

很容易知道,这就是我们最后要下载的图片链接。

### 分析2

上面说了，我们必须要弄明白怎么从首页跳转到第一个，第二个...页面去，这样才够动态。我们点击第一页，注意不是首页，发现页面结构如下图所示，可以看到每一个妹子都不止一张图片，我们就要获取该妹子的 URL，然后进入其主页，获取图片系列 URL，另外可以看到第一页地址栏的 URL：



![](http://7xrl8j.com1.z0.glb.clouddn.com/3.jpg)

![](http://7xrl8j.com1.z0.glb.clouddn.com/9.jpg)

如上图为首页最下面的连接URL，查看红色部分，发现其为下一个页面的相对URL，补全路径，与我们之前分析的下一个页面 URL 为 “http://www.meizitu.com/a/list_1_1.html” 相同，这样就简单了，我们后面只需要重复前面的动作即可。因为每个页面都会指定下一个页面的 URL。

### 代码

![](http://7xrl8j.com1.z0.glb.clouddn.com/11jpg.jpg)
![](http://7xrl8j.com1.z0.glb.clouddn.com/12.jpg)

仓库代码解释更为详细。



### 结果

我是好孩子，就下几张而已。

![](http://7xrl8j.com1.z0.glb.clouddn.com/7.jpg)
