import pandas as pd
from datetime import datetime
import numpy as np 
import re
import os
import timeit

start = timeit.default_timer()
fecha = datetime.today().strftime('%Y%m%d')
num_format = re.compile("^[\-]?[0-9]*\.?[0-9]+$")



# #--------------------------farm plots---------------------------------------------------------------------------------------------------------------
path = r'E:\DATA\OneDrive - CGIAR\PROYECTOS\Boyaca\DATOS\AEPS\BD SISTEMAS AGRÍCOLAS-SOCIOECONÓMICOS- CLIMÁTICO\BD CLIMÁTICAS'
files = os.listdir(path)
files_xlsm = [f for f in files if f[-4:] == 'xlsm']

#Data frame
df = pd.DataFrame()

for f in files_xlsm:
	path_ = os.path.join(path, f)
	data = pd.read_excel(path_, 'PRINCIPAL', skiprows=2)
	#data["ext_id_fram"] = "ESTACION-CLIMATICA-FINCA-" + data.iloc[:, 0].astype(str)
	data["ext_id_fram"] = data.iloc[:, 0]
	data["ext_id_plot"] = data.iloc[:, 0]
	data["name"] = 'Estacion Climatica # '  + data.iloc[:, 0].astype(str)	
	df = df.append(data)

f = {'name': df["name"], 'latitude': df["Latitud"],'ext_id' : df['ext_id_fram'], 'farmer': 1,'longitude': df["Longitud"]}
far_farms = pd.DataFrame(f)
far_farms.to_csv('far_farms.csv', index=False)


p = {'farm': df['ext_id_fram'], 'name': df["name"], 'latitude': df["Latitud"], 'altitude': df['Altura'], 'ext_id': df ['ext_id_plot'], 'longitude': df["Longitud"]}
far_plots = pd.DataFrame(p)

far_plots.to_csv('far_plots.csv', index=False)

print(far_plots)

# #--------------------------farm plots---------------------------------------------------------------------------------------------------------------

start = timeit.default_timer()

path = r'E:\DATA\OneDrive - CGIAR\PROYECTOS\Boyaca\DATOS\AEPS\BD SISTEMAS AGRÍCOLAS-SOCIOECONÓMICOS- CLIMÁTICO\BD CLIMÁTICAS'
files = os.listdir(path)
files_xlsm = [f for f in files if f[-4:] == 'xlsm']

#Data frame
df = pd.DataFrame()

for f in files_xlsm:
	path_ = os.path.join(path, f)
	if f == '1. BD-CLIMÁTICOS-MOTAVITA.xlsm':	
		data = pd.read_excel(path_, sheet_name = ['ESTACIÓN 3', 'ESTACIÓN 4'])
		data['ESTACIÓN 3']['estacion'] = 3
		data['ESTACIÓN 4']['estacion'] = 4
		df = df.append(data['ESTACIÓN 3'])
		df = df.append(data['ESTACIÓN 4'])
		

	if f == '2. BD-CLIMÁTICOS-SAMACÁ.xlsm':
		data = pd.read_excel(path_, sheet_name = ['ESTACIÓN 9', 'ESTACIÓN 7', 'ESTACIÓN 6'])
		data['ESTACIÓN 9']['estacion'] = 9
		data['ESTACIÓN 7']['estacion'] = 7
		data['ESTACIÓN 6']['estacion'] = 6
		df = df.append(data['ESTACIÓN 9'])
		df = df.append(data['ESTACIÓN 7'])
		df = df.append(data['ESTACIÓN 6'])

	if f == '3. BD-CLIMÁTICOS-SIACHOQUE.xlsm':
		data = pd.read_excel(path_, sheet_name = ['ESTACIÓN 12', 'ESTACIÓN 16'])
		data['ESTACIÓN 12']['estacion'] = 12
		data['ESTACIÓN 16']['estacion'] = 16
		df = df.append(data['ESTACIÓN 12'])
		df = df.append(data['ESTACIÓN 16'])

	if f == '4. BD-CLIMÁTICOS-SORACÁ.xlsm':
		data = pd.read_excel(path_, sheet_name = ['ESTACIÓN 1', 'ESTACIÓN 2'])
		data['ESTACIÓN 1']['estacion'] = 1
		data['ESTACIÓN 2']['estacion'] = 2
		df = df.append(data['ESTACIÓN 1'])
		df = df.append(data['ESTACIÓN 2'])

	if f == '5. BD-CLIMÁTICOS-TOCA.xlsm':
		data = pd.read_excel(path_, sheet_name = ['ESTACIÓN 5', 'ESTACIÓN 15'])
		data['ESTACIÓN 5']['estacion'] = 5
		data['ESTACIÓN 15']['estacion'] = 15		
		df = df.append(data['ESTACIÓN 5'])
		df = df.append(data['ESTACIÓN 15'])

	if f == '6. BD-CLIMÁTICOS-TUNJA.xlsm':
		data = pd.read_excel(path_, sheet_name = ['ESTACIÓN 13', 'ESTACIÓN 14'])
		data['ESTACIÓN 13']['estacion'] = 13
		data['ESTACIÓN 14']['estacion'] = 14
		df = df.append(data['ESTACIÓN 13'])
		df = df.append(data['ESTACIÓN 14'])

	if f == '7. BD-CLIMÁTICOS-VENTAQUEMADA.xlsm':
		data = pd.read_excel(path_, sheet_name = ['ESTACIÓN 11', 'ESTACIÓN 10', 'ESTACIÓN 8','ESTACIÓN 7'])
		data['ESTACIÓN 11']['estacion'] = 11
		data['ESTACIÓN 10']['estacion'] = 10
		data['ESTACIÓN 8']['estacion'] = 8
		data['ESTACIÓN 7']['estacion'] = 7
		df = df.append(data['ESTACIÓN 11'])
		df = df.append(data['ESTACIÓN 10'])
		df = df.append(data['ESTACIÓN 8'])
		df = df.append(data['ESTACIÓN 7'])



#df['ext_id_event']= 'EVENTO-CLIMA-ESTA-' + df['estacion'].astype(str)  + '-' + df['Fecha'].astype(str) + '-' + df['Hora'].astype(str) 
#df["ext_id_plot"] = "ESTACION-CLIMATICA-LOTE-" + df['estacion'].astype(str) 
# df['ext_id_event'] = df.index




df['ext_id_event'] = range(0, df.shape[0])



df['ext_id_plot'] = df['estacion']


# far_production_events
# far_production_events = pd.DataFrame({'technical' : 1, 'ext_id' : df['ext_id_event'], 'plot': df['ext_id_plot'], 'form' : 2})
far_production_events = pd.DataFrame({'technical' : 1, 'ext_id' : df['ext_id_event'], 'plot': df['ext_id_plot'], 'form' : 2, 'enable':1})
# far_production_events = pd.DataFrame({'technical' : 1, 'ext_id' : df['ext_id_event'], 'plot': df['estacion'], 'form' : 2, 'farm':df['estacion']})



far_production_events.to_csv('far_production_events.csv', index=False)



df.columns =df.columns.str.strip()

##--------------------far_responses_numeric
## variables
temperatura_externa = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Temperatura externa (°C)'], 'question': 127, 'fixed_value':df['Temperatura externa (°C)'] , 'raw_units': 'Grados_celsius', 'validated' : 1})
temperatura_alta = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Temperatura alta (°C)'], 'question': 128, 'fixed_value':df['Temperatura alta (°C)'] , 'raw_units': 'Grados_celsius', 'validated' : 1})
temperatura_baja = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Temperatura baja (°C)'], 'question': 129, 'fixed_value':df['Temperatura baja (°C)'] , 'raw_units': 'Grados_celsius', 'validated' : 1})
humedad_relativa_exter = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Humedad relativa externa(%)'], 'question': 130, 'fixed_value':df['Humedad relativa externa(%)'] , 'raw_units': '0_100', 'validated' : 1})
punto_rocio = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Punto de rocío (°C)'], 'question': 131, 'fixed_value':df['Punto de rocío (°C)'] , 'raw_units': 'Grados_celsius', 'validated' : 1})
velocidad_viento = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Velocidad del viento (m/s)'], 'question': 132, 'fixed_value':df['Velocidad del viento (m/s)'] , 'raw_units': 'metros_segundo', 'validated' : 1})
recorrido_viento = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Recorrido del viento (m)'], 'question': 134, 'fixed_value':df['Recorrido del viento (m)'] , 'raw_units': '', 'validated' : 1})
velocidad_vientoalta = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Velocidad alta (m/s)'], 'question': 135, 'fixed_value':df['Velocidad alta (m/s)'] , 'raw_units': 'metros_segundo', 'validated' : 1})
sensa_termica = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Sensación termica (°C)'], 'question': 137, 'fixed_value':df['Sensación termica (°C)'] , 'raw_units': 'Grados_celsius', 'validated' : 1})
indice_calor = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Indice de calor (°C)'], 'question': 138, 'fixed_value':df['Indice de calor (°C)'] , 'raw_units': 'Grados_celsius', 'validated' : 1})
indice_temphumed = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Indice temperatura - humedad - viento'], 'question': 139, 'fixed_value':df['Indice temperatura - humedad - viento'] , 'raw_units': '', 'validated' : 1})
indice_temphumedsol = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Indice temperatura - humedad - sol - viento'], 'question': 140, 'fixed_value':df['Indice temperatura - humedad - sol - viento'] , 'raw_units': '', 'validated' : 1})
presion_atmos = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Presión Atmosférica (milibares)'], 'question': 141, 'fixed_value':df['Presión Atmosférica (milibares)'] , 'raw_units': 'milibares', 'validated' : 1})
precipi = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Precipitación (mm)'], 'question': 142, 'fixed_value':df['Precipitación (mm)'] , 'raw_units': 'mm', 'validated' : 1})
tasadePPTi = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Tasa de PPT (mm/hr)'], 'question': 143, 'fixed_value':df['Tasa de PPT (mm/hr)'] , 'raw_units': '(mm/hr)', 'validated' : 1})
radiacisolar_watt = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Radiación solar (watts/m^2)'], 'question': 144, 'fixed_value':df['Radiación solar (watts/m^2)'] , 'raw_units': 'watts/m^2', 'validated' : 1})
radiacisolar_lang = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Energia solar (langleys)'], 'question': 145, 'fixed_value':df['Energia solar (langleys)'] , 'raw_units': 'langleys', 'validated' : 1})
radiacisolaralta_lang = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Radiación solar alta (langleys)'], 'question': 146, 'fixed_value':df['Radiación solar alta (langleys)'] , 'raw_units': 'langleys', 'validated' : 1})
gradosdias_calor = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Grados días (calor)'], 'question': 147, 'fixed_value':df['Grados días (calor)'] , 'raw_units': '', 'validated' : 1})
gradosdias_frio = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Grados días (frío)'], 'question': 148, 'fixed_value':df['Grados días (frío)'] , 'raw_units': '', 'validated' : 1})
temp_consola = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Temperatura consola (°C)'], 'question': 149, 'fixed_value':df['Temperatura consola (°C)'] , 'raw_units': 'Grados_celsius', 'validated' : 1})
hr_consola = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Humedad relativa consola (%)'], 'question': 150, 'fixed_value':df['Humedad relativa consola (%)'] , 'raw_units': '0_100', 'validated' : 1})
puntorocio_consola = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Punto de rocío consola'], 'question': 151, 'fixed_value':df['Punto de rocío consola'] , 'raw_units': '', 'validated' : 1})
indicacalor_consola = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Indice de calor consola (°C)'], 'question': 152, 'fixed_value':df['Indice de calor consola (°C)'] , 'raw_units': 'Grados_celsius', 'validated' : 1})
grados_enfriament = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Grados días de enfriamiento'], 'question': 153, 'fixed_value':df['Grados días de enfriamiento'] , 'raw_units': '', 'validated' : 1})
densidad_aire = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Densidad del aire'], 'question': 154, 'fixed_value':df['Densidad del aire'] , 'raw_units': '', 'validated' : 1})
evotranpir = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Evapotranspiración (mm)'], 'question': 155, 'fixed_value':df['Evapotranspiración (mm)'] , 'raw_units': 'mm', 'validated' : 1})
muestravelocvient = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Muestra de velocidad del viento'], 'question': 156, 'fixed_value':df['Muestra de velocidad del viento'] , 'raw_units': 'mm', 'validated' : 1})
canalvientos = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Canal datos viento'], 'question': 157, 'fixed_value':df['Canal datos viento'] , 'raw_units': '', 'validated' : 1})
minutos = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Minutos'], 'question': 158, 'fixed_value':df['Minutos'] , 'raw_units': 'Minutos', 'validated' : 1})
intervaloarchivo = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Intervalo archivo ()'], 'question': 159, 'fixed_value':df['Intervalo archivo ()'] , 'raw_units': '', 'validated' : 1})


frames = [temperatura_externa, temperatura_alta, temperatura_baja, humedad_relativa_exter,punto_rocio, velocidad_viento, recorrido_viento, velocidad_vientoalta, sensa_termica, 
         indice_calor, indice_temphumed, indice_temphumedsol,presion_atmos, precipi, tasadePPTi, radiacisolar_watt, radiacisolar_lang, radiacisolaralta_lang, gradosdias_calor,
		   gradosdias_frio, temp_consola, hr_consola, puntorocio_consola,indicacalor_consola,grados_enfriament,densidad_aire , evotranpir, muestravelocvient, canalvientos, minutos,
		   intervaloarchivo ]

far_responses_numeric = pd.concat(frames)
far_responses_numeric = far_responses_numeric.replace("---", "")
far_responses_numeric = far_responses_numeric.replace("------", "")



far_responses_numeric.to_csv('far_responses_numeric.csv', index=False)

#------- far text----------------------------------
direccion_viento = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Dirección del viento'], 'question': 133, 'fixed_value':df['Dirección del viento'] , 'validated' : 1})
tendenc_direcc = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Tendencia de dirección'], 'question': 136, 'fixed_value':df['Tendencia de dirección'], 'validated' : 1})
hora =pd.DataFrame( {'event' : df['ext_id_event'], 'raw_value' : df['Hora'].astype(str), 'question': 133, 'fixed_value':df['Hora'].astype(str) , 'validated' : 1})

frames_ = [direccion_viento ,tendenc_direcc, hora]
far_responses_text = pd.concat(frames_)

print(far_responses_text)

far_responses_text.to_csv('far_responses_text.csv', index=False)
#------- far date----------------------------------


fecha = pd.DataFrame({'event' : df['ext_id_event'], 'raw_value' : df['Fecha'].astype(str), 'question': 125, 'fixed_value':df['Fecha'].astype(str), 'validated' : 1})

#frames_aux = [fecha  ,hora]
# far_responses_date = pd.concat(frames_aux)
far_responses_date = fecha

far_responses_date.to_csv('far_responses_date.csv', index=False)

print(far_responses_date)



stop = timeit.default_timer()

print('Time: ', stop - start) 

