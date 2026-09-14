# Gestión de gastos

Programa de terminal en Python puro (sin librerías externas) para registrar y analizar gastos personales. Este proyecto fue realizado para practicar mis habilidades con el lenguaje Python, además de poder diseñar un programa de terminal que resuelva un problema real.

---

### Funcionalidades actuales

- Agregar un gasto (descripción, categoría, monto, fecha automática)
- Ver todos los gastos cargados
- Ver el total gastado
- Ver el total gastado por categoría
- Exportar los gastos a un archivo CSV

---

### Cómo ejecutarlo

No necesita librerías externas, solo Python instalado (usa la librería estándar: `datetime` y `csv`).

```bash
python ProcesadorGastos.py
```

---

### Ejemplo de uso

```
=============== Procesador de gastos ===============
1. Agregar gasto
2. Ver todos los gastos
3. Ver total gastado
4. Ver total por categoría
5. Exportar archivo
6. Salir
Elegí una opción:
```

---

### Objetivos

- Poder agregar más funcionalidades al programa
- A futuro hacer una app móvil/web

---

### Estado del proyecto

En progreso. Este README se irá actualizando a medida que se agreguen nuevas funcionalidades, módulos o características.

---

### Tareas pendientes

- [ ] Guardar y cargar los gastos desde un archivo para que persistan entre ejecuciones
- [ ] Permitir editar o eliminar un gasto ya cargado
- [ ] Agregar más categorías o validación de categorías
