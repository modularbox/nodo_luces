# nodo_luces
Programa en python, para la configuración de las luces.

Instalar dependencias 
pip3 install requeriments.txt

Instalar PyDMXControl
Sustutuir VERSION la version que tengas de python
Despues ir a la carpeta /usr/local/lib/python[VERSION]/dist-packages/PyDMXControl/web/_routes.py
Y en el archivo ir a routes = Blueprint(''), __name__, url_prefix='/')
Y modificarlo por
Y en el archivo ir a routes = Blueprint('dmx'), __name__, url_prefix='/')

Archivo para que el programa se ejecute, cuando se inicie la maquina
En lugar, poner el lugar donde estara la maquina
echo "[Unit]
Description=Iniciar luces

[Service]
ExecStart=/usr/bin/python3 /nodo_luces/luces_sockets.py lugar
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=programa

[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/auto-restart.service

# Programar el python para que se ejecute al inicio
systemctl daemon-reload
systemctl enable auto-restart.service
systemctl start auto-restart.service
systemctl status auto-restart.service
/usr/bin/python3 /nodo_luces/luces_sockets.py ermita


Despues ir a la carpeta /usr/local/lib/python3.10/dist-packages/PyDMXControl/web/_routes.py