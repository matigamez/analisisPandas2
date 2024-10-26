import pandas as pd

df = pd.read_csv("./data/Datos_tienda.csv")

# Mostrar las primeras 10 filas del DataFrame
print(df.head(10))

# Mostrar las últimas 5 filas del DataFrame
print(df.tail(5))

# Obtener información general sobre el DataFrame
print(df.info())

# Generar estadísticas descriptivas
print(df.describe())

# Identificar valores nulos en cada columna
print(df.isnull().sum())

# Manejar valores nulos, si es que hay, en "Ingreso" rellenando con la media
df['Ingreso'].fillna(df['Ingreso'].mean(), inplace=True)

# Interpolar valores faltantes linealmente
df.interpolate(method='linear', inplace=True)

# Convertir la columna 'Fecha' a formato de fecha
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

# Convertir la columna 'Ingreso' a numérico
df['Ingreso'] = pd.to_numeric(df['Ingreso'], errors='coerce')

# Eliminar duplicados
df.drop_duplicates(inplace=True)

# Crear nuevas columnas
df['Ingresos_Calculados'] = df['Ventas'] * df['Precio']

# Normalizar y estandarizar la columna de Ingreso
df['Ingreso_Normalizado'] = (df['Ingreso'] - df['Ingreso'].min()) / (df['Ingreso'].max() - df['Ingreso'].min())
df['Ingreso_Estandarizado'] = (df['Ingreso'] - df['Ingreso'].mean()) / df['Ingreso'].std()

# Clasificar en categorías
df['Categoria_Ingreso'] = pd.cut(df['Ingreso'], bins=[0, 1000, 5000, 10000], labels=['Bajo', 'Medio', 'Alto'])

# Agrupación y agregación
ventas_por_producto = df.groupby('Productos')['Ingreso'].sum()
ventas_por_tienda = df.groupby('Tienda')['Ingreso'].sum()

# Resumen por tienda usando agregación múltiple
resumen_tienda = df.groupby('Tienda').agg({
    'Ingreso': ['sum', 'mean', 'count', 'min', 'max', 'std', 'var']
})

#funcion para aplicar descuento
def aplicar_descuento(fila):
    if fila['Ingreso'] > 5000:
        return fila['Ingreso'] * 0.9  # Aplicar un 10% de descuento
    else:
        return fila['Ingreso']

df['Ingreso_Con_Descuento'] = df.apply(aplicar_descuento, axis=1)



print(ventas_por_producto)
print(ventas_por_tienda)
print(resumen_tienda)
