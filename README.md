# DentaWeb
DentaWeb:  
1. Finds .bmp images from EasyDent v4 folder.   
2. Converts them into jpeg.  
3. Queries EasyDent v4 database (sql server) for patient names  
4. Serves them running Flask via Gevent
  
   
To install on windows you need to:  
1. Install Python 3.6 and insure 
2. Install libraries (Flask, Pollow, gevent, pyodbc)  
```
pip install -r requirements.txt  
```
3. Configure values folders, SQLServer connection string in **denta_config.ini**  
4. Install Windows services to run scripts. For example using nssm: (http://nssm.cc)  
```
nssm install denta_server
nssm set denta_server Application python.exe
nssm set denta_server AppParameters server.py

nssm install denta_converter
nssm set denta_converter Application python.exe
nssm set denta_converter AppParameters image_converter.py
```
