def validar_contrasena(contrasena):
    errores = []

    if len(contrasena) < 8:
        errores.append("Debe tener al menos 8 caracteres")

    
        errores.append("Debe tener al menos una mayuscula")

    if not any(c.isdigit() for c in contrasena):
        errores.append("Debe tener al menos un numero")

    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in contrasena):
        errores.append("Debe tener al menos un simbolo especial")

    if errores:
        return {"valida": False, "errores": errores}

    return {"valida": True, "errores": []}