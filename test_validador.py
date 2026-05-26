import pytest
from validador import validar_contrasena

def test_contrasena_valida():
    resultado = validar_contrasena("Segura@123")
    assert resultado["valida"] == True
    assert resultado["errores"] == []

def test_contrasena_muy_corta():
    resultado = validar_contrasena("Ab@1")
    assert resultado["valida"] == False
    assert "Debe tener al menos 8 caracteres" in resultado["errores"]

def test_sin_mayuscula():
    resultado = validar_contrasena("segura@123")
    assert resultado["valida"] == False
    assert "Debe tener al menos una mayuscula" in resultado["errores"]

def test_sin_numero():
    resultado = validar_contrasena("Segura@abc")
    assert resultado["valida"] == False
    assert "Debe tener al menos un numero" in resultado["errores"]

def test_sin_simbolo():
    resultado = validar_contrasena("Segura1234")
    assert resultado["valida"] == False
    assert "Debe tener al menos un simbolo especial" in resultado["errores"]

def test_multiples_errores():
    resultado = validar_contrasena("abc")
    assert resultado["valida"] == False
    assert len(resultado["errores"]) == 4