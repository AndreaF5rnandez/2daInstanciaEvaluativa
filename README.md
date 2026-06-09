# Validador de Contraseñas

Proyecto desarrollado para la 2da Instancia Evaluativa de Integración y Entrega Continua.

## ¿Qué hace?

Valida si una contraseña cumple con los requisitos mínimos de seguridad:

- Al menos 8 caracteres
- Al menos una letra mayúscula
- Al menos un número
- Al menos un símbolo especial

## Entornos

- **Frontend (GitHub Pages):** https://andreaf5rnandez.github.io/2daInstanciaEvaluativa/
- **Backend / API (Render):** https://twodainstanciaevaluativa.onrender.com

## Tecnologías utilizadas

- **Lenguaje:** Python con Flask
- **Pruebas:** pytest
- **Servidor de CI/CD:** GitHub Actions
- **Frontend:** GitHub Pages
- **Backend:** Render

## Flujo CI/CD

Cada vez que se sube código a la rama main, GitHub Actions ejecuta automáticamente las pruebas. Si todas pasan, despliega el frontend en GitHub Pages y el backend en Render. Si alguna prueba falla, el despliegue se cancela y el código roto nunca llega a producción.
