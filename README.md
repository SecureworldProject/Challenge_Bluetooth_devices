# Challenge_Bluetooth

Es challenge genera una clave en función de los distintos dispositivos bluetooth cercanos. Este challenge complementa el [parental control blueetooth challenge](https://github.com/SecureworldProject/Challenge_Bluetooth). Permite ser utilizado para comprobar situaciones de aislamiento. Por ejemplo, algunos documentos necesitan una certificación de seguridad para ser abiertos, por lo que en ocasiones se requiere que el ordenador esté totalmente aislado. 

Usa bluetooth, en particular la librería `pybluez`.

## Instalar la librería pybluez en Windows 10

Primero instala [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)

Segundo, descarga e instala las builds de Windows 10 [build tools](https://www.microsoft.com/es-ES/download/confirmation.aspx?id=48159)

Tercer, clona [pybluez](https://github.com/pybluez/pybluez)

Cuarto, como administrador, dentro del repositorio: `python setup.py install`

Ejemplo de configuracion json
```json
{
	"FileName": "bluetooth_devices_challenge.dll",
	"Description": "Challenge that generates a key using a list of bluetooth devices as input",
	"Props": {
		"validity_time": 3600,
		"refresh_time": 3000
	},
	"Requirements": "none"
}
```

## Funcionamiento

Todas las funciones y la lógica del challenge se encuentran en el fichero bluetooth_devices_challenge.py, el cual es un programa en python que contiene toda la lógica del challenge. La función principal dentro del fichero que gestiona toda la lógica del challenge es bluetooth.discover_devices(), la cual devuelve la lista de dispositivos que se encuentran dentro del rango del ordenador y tienen el Bluetooth activado. Asimismo, toda la lógica del challenge se ejecuta dentro de la función executeChallenge( ).

Primero se llama a bluetooth.discover_devices(), mediante la cual se obtiene la lista de dispositivos cercanos que tienen el Bluetooth activado. A la hora de llamar al método, es importante especificar como parámetro de la función: lookup_names=True, ya que esto hace que se devuelvan los nombres de los dispositivos. En base a esa lista se genera un array que contiene todos los dispositivos. Dicho array se concatena y a partir de la concatenación se genera una clave. Por el contrario, si no hay ningún dispositivo con el Bluetooth activo dentro del rango, la clave será '0000'.

Es aplicable a PCs personales y/o servidores. El contexto de seguridad requiere que existan varios dispositivos en la zona de operación donde se encuentra el equipo. El ejemplo puede ser algo similar al anterior.
