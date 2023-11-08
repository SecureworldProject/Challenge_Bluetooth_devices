# Challenge_Bluetooth

This challenge generates a key depending on the different bluetooth devices nearby. This challenge complements the [parental control blueetooth challenge](https://github.com/SecureworldProject/Challenge_Bluetooth).

It uses bluetooth, in particular `pybluez` library.

## Install pybluez in Windows 10

First, install [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)

Second, download and install windows 10 [build tools](https://www.microsoft.com/es-ES/download/confirmation.aspx?id=48159)

Third, Clone [pybluez repo](https://github.com/pybluez/pybluez)

Fourth, run as administrator, within the repo: `python setup.py install`

ejemplo de configuracion json
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
