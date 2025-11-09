#Conversione delle temperature
zero_assoluto = float(-273.15)
temp_Celsius = float(input("inserisci la temperatura in gradi Celsius:"))
if(temp_Celsius>zero_assoluto):
    conversione_in_Fahrenheit = temp_Celsius*(9/5)+32
    print("la temperatura inserita equivale a",conversione_in_Fahrenheit,"gradi Fahrenheit")
    conversione_in_Kelvin = temp_Celsius + 273.15
    print("la temperatura inserita equivale a",conversione_in_Kelvin,"Kelvin")
else:
    print("Errore")