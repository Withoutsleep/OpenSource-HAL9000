#Lector de configuración para HAL9000 - Withoutsleep_dev
def get_config(configuracion_solicitada):
    print(configuracion_solicitada)
    diccionario_conf = {}
    try:
        with open('.halconfig/hal.conf', 'r', encoding='utf-8') as f:
            for linea in f:
                linea=linea.strip()
                if not linea or linea.startswith('#'):
                    continue
                if '=' in linea:
                    try:
                        key, value_raw=map(str.strip, linea.split('=', 1))
                        diccionario_conf[key]=value_raw
                    except:
                	    print("ERROR")
        print(diccionario_conf[configuracion_solicitada])
        return diccionario_conf[configuracion_solicitada]
    except FileNotFoundError:
        print("ERROR: El archivo de configuración no se ha encontrado (ruta: .halconfig/hal.conf)")
        return "ERROR"
