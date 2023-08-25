from datetime import datetime
from datetime import timedelta


class VaccinationEstimation:
    def __init__(self, population, vaccinated, doses_per_person, vaccination_rate):
        self.population = population
        self.vaccinated = vaccinated
        self.doses_per_person = doses_per_person
        self.vaccination_rate = vaccination_rate
    
    def calculate_vaccination_coverage(self, target_percentage):
        target_vaccinated = self.population * target_percentage / 100
        remaining_vaccinated = max(0, target_vaccinated - self.vaccinated)
        
        days_needed = remaining_vaccinated / (self.vaccination_rate * self.doses_per_person)
        date_reached = (datetime.now() + timedelta(days=days_needed)).date()
        
        return remaining_vaccinated, date_reached
    
    def calculate_vaccine_purchase(self, months):
        doses_needed = (self.population - self.vaccinated) * self.doses_per_person
        doses_per_month = doses_needed / months
        return doses_per_month, doses_needed

# Datos de ejemplo
population = 12000000  # Población de Bolivia
vaccinated = 3000000   # Personas vacunadas con al menos una dosis
doses_per_person = 2   # Dosis requeridas para inmunización completa
vaccination_rate = 50000 / 30  # Tasa de vacunación diaria (ejemplo: 50000 dosis al mes)

# Crear una instancia de la clase
estimator = VaccinationEstimation(population, vaccinated, doses_per_person, vaccination_rate)

# Calcular la cobertura de vacunación
target_percentage = 70  # Porcentaje objetivo de población vacunada
remaining_vaccinated, date_reached = estimator.calculate_vaccination_coverage(target_percentage)

# Calcular la compra de vacunas
months = 6  # Plazo en meses
doses_per_month, doses_needed = estimator.calculate_vaccine_purchase(months)

# Resultados
print(f"Fecha estimada de cobertura del {target_percentage}%: {date_reached}")
print(f"Vacunas necesarias mensualmente para alcanzar el objetivo en {months} meses: {doses_per_month}")
print(f"Vacunas necesarias a partir de hoy para alcanzar el objetivo: {doses_needed}")

# ejecucion del codigo con grafica 