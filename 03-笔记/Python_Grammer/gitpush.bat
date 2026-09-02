@echo off
chcp 65001 >nul
echo 正在进入项目目录...
cd /d "E:\My_Files\4_专业资料\Git_Backup\My_github\08_Python"

echo 正在添加所有更改...
git add .

echo 正在提交更改...
git commit -m "update git notes"

echo 正在推送到远程仓库...
git push origin main

echo.
echo 操作成功！
pause