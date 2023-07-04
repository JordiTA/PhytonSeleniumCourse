

full_name = ' Jordi Tomas. '
name_s = full_name.split()  # Separa en una lista los strings por los espacios.
print(name_s)

print('-------------------------------------') # Separator

ssn = "111-22-3333"
ssn_s = ssn.split('-')      # Puede separar por el caracter o conjunto de caracteres que digamos.
print(ssn)
print(ssn_s)

print('-------------------------------------') # Separator

print(full_name)
name_clean = full_name.strip()  #Strip recorta por delante y por detras los espacios.
print(name_clean)
name_clean = name_clean.strip('.')  # O tambien cualquier caracter.
print(name_clean)

print('-------------------------------------') # Separator

print(name_clean.upper())   # MAYUSCULAS
print(name_clean.lower())   # minusculas

print('-------------------------------------') # Separator

url = 'https://web.com/'
is_home = url.endswith('.com/')         # Acaba por ... (Retorna boolean)
is_absolute = url.startswith('https')   # Empieza por...(Retorna boolean)
print(is_home)
print(is_absolute)

print('-------------------------------------') # Separator

info = "This%20is%20url%20encoded."
clean_info = info.replace("%20", " ")   # Reemplaza
print(clean_info)