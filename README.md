# Flask问答网站(QA-sys)

## 技术栈
- **后端框架**: Flask 3.1.2
- **数据库**: 
  - SQLAlchemy 2.0
  - PyMySQL
- **扩展组件**:
  - Flask-WTF (表单处理)
  - Flask-Mail (邮件服务)
  - Flask-Migrate (数据库迁移)

## 核心功能
1. 用户注册/登录（含邮箱验证）
2. 问题发布与管理
3. 回答功能
4. 数据库迁移管理

## 安装运行
### 1. 克隆项目
```cmd
```
### 2. 配置环境`config.py`
1.配置数据库连接（本项目使用MySQL）
2.配置邮箱（请登录各邮箱平台开通相关服务）
### 3. 安装依赖
```cmd
pip install -r requirements.txt
```
### 4. 初始化数据库
```SQL
create database qasys;
```
### 5. 启动服务
```cmd
python app.py
```