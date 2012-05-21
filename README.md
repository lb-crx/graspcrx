# crx 原件下载器!

## 使用

### 在线直问

- 访问 http://graspcrx.sinaapp.com
- 将具体的 chrome 插件链接提交
- 就会跳转到下载页面, 右击另存,就可以随时使用[猎豹](http://liebao.cn) 打开完成插件安装了!

### 书签自动

- 访问 http://graspcrx.sinaapp.com
- 将 "[抓CRX]" 链接,拖到书签栏
- 然后,想下载插件时

    - 只要,进入具体的 chrome 插件页面
    - 再点击 "[抓CRX]" 
    - 就会跳转到下载页面, 右击另存,就可以随时使用[猎豹](http://liebao.cn) 打开完成插件安装了!



## 原因

[猎豹](http://liebao.cn) 内测期间官方释放的插件不多,于是热情的 fans 们疯狂下载原厂插件来测试

- 但是! web store 中,并没有插件的 .crx 原件下载链接
- 于是: 

    - [下载Chrome的CRX扩展文件包（新手看） - 扩展插件区 - 猎豹浏览器官方论坛](http://bbs.liebao.cn/thread-11492-1-1.html)

- 进一步:

    - [How to View the Source Code of a Chrome Extension](http://www.labnol.org/software/view-source-of-chrome-extension/21284/)
    - 囧的是,这里的 书签工具,依赖外国的服务! 速度慢不説,界面还是E文的!
    - 不爽直!


## 所以!

- 基于国产云服务 [Sina App Engine](http://sae.sina.com.cn/?m=devcenter)
- 使用 [Bottle](http://bottlepy.org/) 快速山寨了个相同的服务!


