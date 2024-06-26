import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'C:\Users\moesios\Desktop\EXT-DOMs+CONTORNO\MATRIZES AMOSTRAIS - Copia_.xlsx'
df_viagens_validas = pd.read_excel(file_path, sheet_name='VIAGENS VÁLIDAS')

print(df_viagens_validas.head())

df_viagens_validas['Hora_inicio'] = pd.to_datetime(df_viagens_validas['Hora_inicio'], format='%H:%M:%S').dt.hour
vdms_por_hora = df_viagens_validas.groupby('Hora_inicio').size()

def definir_periodo(hora):
    if 6 <= hora < 12:
        return 'Manhã'
    elif 12 <= hora < 18:
        return 'Tarde'
    elif 18 <= hora < 24:
        return 'Noite'
    else:
        return 'Madrugada'

df_viagens_validas['Periodo'] = df_viagens_validas['Hora_inicio'].apply(definir_periodo)
vdms_por_periodo = df_viagens_validas.groupby('Periodo').size()

volumes_por_modo_hora = df_viagens_validas.groupby(['MODO', 'Hora_inicio']).size().unstack(fill_value=0)

viagens_por_hora_motivo = df_viagens_validas.groupby(['MOTIVO VIAGEM', 'Hora_inicio']).size().unstack(fill_value=0)


plt.figure(figsize=(12, 6))
vdms_por_hora.plot(kind='bar', color='skyblue')
plt.title('VDMs por Hora')
plt.xlabel('Hora do Dia')
plt.ylabel('Número de Viagens')
plt.grid(True)


plt.figure(figsize=(8, 6))
vdms_por_periodo.plot(kind='bar', color='lightgreen')
plt.title('VDMs por Período')
plt.xlabel('Período do Dia')
plt.ylabel('Número de Viagens')
plt.grid(True)


plt.figure(figsize=(14, 8))
sns.heatmap(volumes_por_modo_hora, cmap='YlGnBu', annot=True, fmt='d')
plt.title('Volumes de Veículos por Modo e Hora')
plt.xlabel('Hora do Dia')
plt.ylabel('Modo Principal')


plt.figure(figsize=(14, 8))
sns.heatmap(viagens_por_hora_motivo, cmap='YlOrRd', annot=True, fmt='d')
plt.title('Distribuição das Viagens por Hora e Motivo')
plt.xlabel('Hora do Dia')
plt.ylabel('Motivo da Viagem')
plt.show()
