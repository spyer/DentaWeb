pip install gevent
pip install Flask
pip install pyodbc
pip install Pillow

nssm install denta_converter
nssm set denta_converter Application python.exe
nssm set denta_converter AppParameters image_converter.py
nssm start denta_converter

nssm install denta_server
nssm set denta_server Application python.exe
nssm set denta_server AppParameters server.py
nssm start denta_server
