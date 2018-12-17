# 手写体数字识别的学生在线实验平台说明文档

## 1. 开发环境

Python解释器版本：3.6.x

依赖库：`django` `pillow` `tensorflow` 

IDE：PyCharm

## 2. 开发说明

### 2.1 代码结构

![directory](img/directory)

一个django项目下可以创建多个app以划分不同的功能。目前已经创建好了两个app，一个是api，负责后端接口；一个是page，负责前端渲染。也就是项目目录下的api和page文件夹。

static文件夹存储静态资源，也就是bootstrap模板的资源。

templates文件夹中是前端的html代码。

AiLab文件夹中则是与项目相关的配置文件。


### 2.2 手写体识别

### 2.3 前端展示

### 2.4 运行项目

首先把项目clone到本地，然后用PyCharm打开项目文件夹，如果PyCharm识别出这是一个Django项目（需要PyCharm Professional），如下图所示

![pycharm](img/pycharm)

此时可以直接点击图中绿色的运行按钮，就可以把项目跑起来。

如果PyCharm没有识别出这是一个Django项目也没关系，在下方Terminal中输入`python manage.py runserer`然后回车也可以把项目跑起来。

项目跑起来之后，在浏览器中访问 127.0.0.1:8000 即可访问项目主页。

如果项目启动失败，可能是由于项目所需的包没有安装，可以在PyCharm中检查一下。

## 3. 使用说明

### 3.1 用户登录

### 3.2 题目选择

### 3.3 手写体识别

### 3.4 模型调试

### 3.5 查看排名
