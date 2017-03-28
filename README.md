## 基于Hololens的4D房产体验平台。
### 一. 业务模块划分
#### 1. 上传模块

> 描述：通过上传指定的模型以及对应的行为参数，来绑定到用户应用上

1. 企业用户注册平台账号
2. 创建房产项目
3. 上传模型以及对应参数
4. 后台存储
5. 生成一个二维码与企业用户[二维码应在一个企业的一个应用范围内具有唯一性]

#### 2. 识别模块
> 描述：用户通过上传二维码的形式，服务器识别二维码，获得指定的数据信息，进而获取模型，之后，把模型和模型必要的参数返回给客户端，客户端进行对应的渲染

1. 用户登录
2. 用户上传二维码照片
3. 服务器识别二维码，得到对应的参数信息[url，or something else]
4. 从数据库中获取对应的模型
5. 反馈给客户端
6. 客户端进行渲染

#### 3. 登录注册模块
> 描述： 为企业提供登录注册的接口，用于身份识别

- **注册**，填写以下信息：
    - username: 唯一性用户名
    - password：密码
    - realname：用于显示的用户真实姓名
    - company：公司名字
- **登录[web]**:填写用户名密码即可。
- **登录[hololens]**:填写用户名，密码，并选择参观的房产模型[app_key]

### 二. 数据字典

#### 1. 用户板块：
- username: 唯一性用户名
- password：密码
- realname：用于显示的用户真实姓名
- company：公司名字
- app:公司开发的应用，一个公司可以有很多应用
- model: 一个应用可以上传多个模型

#### 2. 应用板块：
> 所有的应用板块的参数，以’app_‘开头：

app_id:用来唯一标定一个应用的id
app_name:应用的名称
app_pic_key:应用的图片的oss的key
app_description: 应用的描述信息
app_model_list:应用的模型列表
#### 3. 模型板块：
> 所有的模型板块的参数，都以’model_‘开头：

model_id:用来唯一标定模型的id
model_name:模型的名称，这个名称只是方便用户管理用的
model_para_list:模型可以有多个参数，这个是参数列表
model_key:模型的资源的key，用于访问oss服务器

### 三. 数据存储结构
#### 1. 使用OSS来托管这个过程中的产生的模型资源
**oss.hololens**:
- model_key:由user_id+app_id+time 组成.
- app_pic_key:由user_id+app_id 组成.

#### 2. 使用Mongodb来存储主要数据
**model.detail**
- _id
- name:模型名称
- para_list:参数列表
- model_key:用来获取OSS资源的KEY

**app.info**:
- _id:
- name:应用的名称
- pic_key:应用的图片
- description: 应用的描述
- model_list:{model.detail._id} 应用已经上传的model的id。

#### 3. mysql存储用户账户信息
**user_info_table**
- uid: index
- username: 唯一性用户名
- password：密码
- realname：用于显示的用户真实姓名
- company：公司名字
- app_id_list:用户注册的app，为{app.info._id}的一个数组

#### 4. redis用来进行静态资源的缓存
model_key: para_list.[将资源缓存在redis中，避免多次调用mongodb]

### 四. 系统架构
> 系统使用微服务架构进行体系结构设计，各个服务之间使用REST进行通信

#### 1. 二维码处理服务。
- 根据KEY生成二维码
- 根据二维码生成KEY

#### 2. 静态资源获取服务
- 根据KEY获得资源
    - 获取应用模型资源
    - 获取应用图片资源[2.0]
- 上传资源获得KEY
    - 上传模型资源
    - 上传应用图片资源[2.0]

#### 3. 账户信息管理服务。
- 登录
- 注册
- 创建应用
- 获取应用信息
- 存储模型信息
	- 上传模型资源
	- 得到KEY，
	- 编译KEY，生成二维码
	- 反馈二维码到客户端
- 获取模型信息
	- 客户端扫码
	- 解析二维码，得到KEY
	- 获取授权URL
	- 返回URL给客户端



