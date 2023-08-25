import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from VaccinationEstimation import VaccinationEstimation

# Generar datos de ejemplo desde 2021 hasta la fecha actual
start_date = datetime(2021, 1, 1)
end_date = datetime.now()
days_range = (end_date - start_date).days

dates = [start_date + timedelta(days=i) for i in range(days_range)]
temperatures = np.random.randint(0, 30, size=days_range)

# Crear un DataFrame con los datos
data = {'Date': dates, 'Temperature': temperatures}
df = pd.DataFrame(data)

# Mostrar los primeros registros del DataFrame
print(df.head())

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Temperature'], marker='o')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# listo el codigo cumplido