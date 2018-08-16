AuditSQL介绍
===============

**AuditSQL(命名确实是个问题，^_^)是一个web版的MySQL数据库审核平台，旨在降低DBA的运维成本。**

**欢迎大家的使用，同时使用中遇到的问题，请指出，谢谢。（不喜勿喷，谢谢）**

## 文档地址
https://github.com/lazzyfu/AuditSQL/wiki

## 开发组件

- Python 3.6
- Django 2.0 
- celery 4.2.0
- django-channels
- AdminLTE

## 核心功能简介（更多功能，请使用时体验）
- 历史工单
  - 生产环境
  - 预发布环境
  - 测试环境
  - 执行任务记录

- SQL审核
  - DML和DDL语法审核

- 工单
  - DML变更工单
  - DDL上线工单
  - 上线版本号

- 数据查询
  - 生产mysql
  - 非生产mysql
  - mongo和redis（xterm）

- 功能
   - SQL审核的流程化，规范化
   - SQL美化功能
   - SQL检测功能
   - 语法高亮功能
   - 注释识别功能
   - SQL语法自动补全(包括表名和列名)

- 执行任务功能
   - 自动分片当前审核内容，并生产SQL执行任务列表
   - 提供回滚，inception执行日志预览功能
   - 提供DDL语句的OSC进度实时显示和停止功能

- 推送
   - 实时钉钉推送
   - 执行任务执行进度的实时显示（websocket）

- 其他
   - 集成LDAP认证登陆
   - 支持修改头像

## 部署：

step1：安装：install.txt

step2：初始化数据：initial_data.txt


## 移除的功能
1. 移除了对mail的推送支持，目前仅支持钉钉推送

2. 移除了和数据库审核系统功能么有关系的功能

3. 移除了注册用户和创建用户的支持，请使用绑定LDAP使用

## 页面展示(随便展示几处)
![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/test_env.png)

![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/staging_env.png)

![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/dml_gongdan.png)

![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/ddl_gongdan.png)

![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/pro_query.png)

![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/offline_query.png)

![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/mongo_query.png)

![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/sys_config.png)

![](https://github.com/lazzyfu/AuditSQL/blob/master/media/png/dingding.png)




## 联系方式

E-mail: 1126227133@qq.com