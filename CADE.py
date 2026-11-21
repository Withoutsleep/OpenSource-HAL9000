import requests
import random
import time
import configuration_reader

IP_PC = configuration_reader.get_config("ip_pc")
SERVER_URL = f"http://{IP_PC}:5000/hablarespontaneo"


while True:
	Tiempo_Espera=random.randint(1200, 1900) #Punto exacto para que HAL no moleste (por tiempos)
	print(f"Tiempo de espera para interactuar: {Tiempo_Espera}")
	time.sleep(Tiempo_Espera)
	#Inicia el evento de interacción espontanea
	try:
    		payload = {"activar": True}
    		# timeout ajustable, si quieres
    		response = requests.post(SERVER_URL, json=payload, timeout=5)

    		if response.status_code == 200:
      			print("Señal enviada con éxito:", response.json())
    		else:
      			print(f"El servidor respondió con el código de estado: {response.status_code}")

	except requests.exceptions.RequestException as e:
    		print(f"Error de conexión con el servidor: {e}")
