# Tareas (para mañana)

- [ ] **Buscar un servidor real para desplegarlo**
  - **Objetivo**: que el portfolio quede público con un dominio y HTTPS.
  - **Opciones típicas**:
    - VPS (Ubuntu) + Nginx + Gunicorn + Postgres
    - PaaS (Render / Fly.io / Railway) + Postgres administrado
  - **Datos a definir**: dominio, presupuesto, si Postgres será administrado o en el mismo servidor.

- [ ] **Mejorar edición de datos (CV y Contacto) de forma dinámica**
  - **Objetivo**: editar CV/Contacto desde el admin (sin tocar templates).
  - **Idea**: crear un modelo `Profile` (único) con campos como:
    - nombre, bio, email, teléfono/whatsapp
    - instagram_url, otros links (ArtStation/Behance)
    - texto CV (rich text simple o markdown)
  - **Luego**: actualizar las vistas/templates para leer esos campos desde la DB.

