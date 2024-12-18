# cumtb_token_api

## TODO

- [ ] 用fastapi重构
- [ ] 限制访问数
- [ ] 解决chrome无头浏览器不正常退出的内存泄露
- [ ] 更改返回json格式,以便于前端程序处理
- [ ] 更换基础镜像,减少docker大小

## 原理说明

使用python的`selenium`库模拟浏览器，且使用了无头模式。通过访问特定的登录页面，当登录成功后，跳转的网址url中含有X_Id_Token，通过处理`driver.current_url`获取X_Id_Token。  

## 使用方法

### 获取程序

**您有如下的方法获取和使用该程序：**
1. 下载release里的docker镜像，然后部署。
2. 下载源码，然后使用`make`命令构建dockerimage
3. 下载源码，直接使用python运行`main.py`

### 如何使用

关于docker，只需要暴露5000到外部端口即可。  

目前只有一个api，返回了爬取其他数据文件必须的`X_Id_Token`。  
api的使用如下：  
方法：Get  
  
```bash
http://ipOrDomain:port/api/token?id=学号&pwd=密码
```
  
返回值是字符串，格式如下：  
`"token...."\n`
