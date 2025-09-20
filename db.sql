# 创建数据库
create database qasys;
# 查表
select * from qasys.email_captcha;
select * from qasys.user;
select * from qasys.question;
select * from qasys.answer;
# 删除数据
DELETE FROM qasys.user
WHERE id >= 1;