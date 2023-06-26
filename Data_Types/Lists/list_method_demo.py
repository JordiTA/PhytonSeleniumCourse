

countries = [ "Spain", "Mexico", "India", "Peru", "Germany"]
num_countries = len(countries)  # Cuantos elementos tiene una lista
print(num_countries)

# print(type(countries))  type --> te dice de que tipo son las variables

print('-------------------------------------') # Separator

countries.append("China")   # Añadir elemento al final de una lista
print(countries)

print('-------------------------------------') # Separator

countries.pop()             # Quitar el ultimo elemento de la lista
print(countries)

print('-------------------------------------') # Separator

countries.append("Canada")
print(countries)
extract = countries.pop()   # Se puede hacer un pop pero guardarse el valor que quitas de la list
print(countries)
print(extract)

print('-------------------------------------') # Separator

countries.remove('Peru')    # Eliminar un elemento en concreto (No funciona con posiciones de la list).
print(countries)