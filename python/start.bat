@ECHO OFF
cd /d %~dp0
START cmd.exe /k "env\Scripts\activate & python manage.py runserver"