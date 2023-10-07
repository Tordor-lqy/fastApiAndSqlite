# fastApiAndSqlite

## 简介
一个关于fastApi的demo
这个demo我为了足够轻量，所以数据库使用sqlite

## 启动
### python 要求
安装python 版本 > 3.6 即可

### 启动虚拟环境
* windows
  启动对应目录下的activate.bat即可
  
  ```shell
  /your/path/Script/activate.bat
  ```
当命令行前出现了项目名(fastApiAndSqlite)即代表成功进入虚拟环境 
  
### 安装依赖

在虚拟环境中执行以下指令即可

```cmd
pip install -r requirements.txt
```

### 启动项目

在虚拟环境中执行以下指令

```shell
uvicorn main:app --reload
```
如果出现以下信息 则说明成功
```shell
INFO:     Will watch for changes in these directories: ['D:\\CODE\\PYTHON\\PYWEB\\fastApiAndSqlite']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [19440] using WatchFiles
INFO:     Started server process [6620]
INFO:     Waiting for application startup.
```
浏览器访问 http://127.0.0.1:8000 即可
