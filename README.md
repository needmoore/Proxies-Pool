# Welcome Proxies-Pool

## Project introduction：

> It is a project based on asynchronous and thread pool to quickly obtain agents and build free agent pool，can quickly get agents and detect availability from the network. And the agent weight score，It can help Crawlers to break through the ban of IP and obtain data quickly, safely and stably
>
> His main architecture includes Crawler、Tester、Storager and API

## How to use it?

> #### Use requirements(You have to be satisfied)
>
> You have to Successfully established python, Redis（python >= 3.6；Redis can be used normally！！！）
>
> #### IP proxies-pool architecture
>
> It has four main modules and three environments
>
> Modules: Crawler、Testing、storage，API
>
> Env： environment of Run，you can setting  dev、test、prod，(default = dev)
>
> #### You can use it like this, clone to your server
>
> ```python
> # Installation dependency
> pip install -r requirements.txt
> ```
>
> 1. Direct use of commands（Must be in the same directory）
>
> ```python
> python run.py
> # At this point, visit localhost:637
> localhost:637/random ：The proxy is taken out randomly
> localhost:637/count：Number of Proxies pool
> ```
>
> 2. If you know the architecture, you can use it separately(You have to go into the processors)
>
> ```
> python run.py --processor getter
> python run.py --processor tester
> python run.py --processor server
> ```
>
> 

## Settings：

> - CYCLE_TESTER: Run cycle, how often does the test run，(default = 20 s )
> - CYCLE_GETTER: Run cycle, how often does the crawl ，(default = 100s)
> - TEST_URL：https://www.baidu.com    (default)
> - TEST_TIMEOUT:  default = 10 s 
> - TEST_BATCH: Number of asynchronous detections (default = 50 ) 
> - TEST_VALID_STATUS: Test valid status code
> - API_HOST: default = 0.0.0.0
> - API_PORT: default =  637
> - API_THREADED： default = true