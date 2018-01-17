Установка:
1. Установить python 3.6 и убедиться, что он прописан в %PATH%
#################################################################
2. Установить библиотеки 
pip install gevent
pip install Flask
pip install pyodbc
pip install Pillow

#################################################################
3. Установить сервисы с помощью 
nssm install denta_server
nssm set denta_server Application python.exe
nssm set denta_server AppParameters server.py

nssm install denta_imge
nssm set denta_server Application python.exe
nssm set denta_server AppParameters image_converter.py