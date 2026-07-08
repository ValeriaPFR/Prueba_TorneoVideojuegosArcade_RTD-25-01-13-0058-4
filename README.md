# Sistema de Gestión de Torneo - Pixeles Retro 🎮

[cite_start]Este programa en Python permite administrar de forma completa un torneo de videojuegos clásicos en el arcade **Pixeles Retro**[cite: 127]. [cite_start]El sistema gestiona la inscripción de jugadores [cite: 136][cite_start], la creación de parejas competitivas [cite: 137][cite_start], el registro de los partidos [cite: 138] [cite_start]y la generación automática de estadísticas de rendimiento y tablas de posiciones[cite: 139].

[cite_start]Proyecto desarrollado para la evaluación final del módulo de **Fundamentos de Ciencias de Datos**[cite: 99, 123].

---

## 🛠️ Características Principales

* [cite_start]**Control de Inscripciones:** Registro de participantes con validación en tiempo real[cite: 148, 152].
* **Visualización Dinámica:** Lista exclusiva de jugadores que muestra de forma automática si están libres o a qué pareja pertenecen.
* [cite_start]**Formación de Parejas:** Creación de equipos de 2 jugadores asegurando nombres únicos y control de duplicados (un jugador no puede estar en dos equipos a la vez)[cite: 165, 168, 172].
* [cite_start]**Módulo de Partidas:** Registro de enfrentamientos asignando 3 puntos reglamentarios al equipo ganador[cite: 178, 182].
* [cite_start]**Analítica de Datos:** Uso del módulo nativo `statistics` de Python para calcular promedios, medianas, modas y variabilidad de los puntajes del torneo[cite: 185, 186].

---

## 🛡️ Guía de Pruebas de Robustez (Manejo de Errores)

Para evidenciar la estabilidad del programa, el sistema ha sido diseñado para resistir entradas incorrectas sin interrumpir su ejecución. A continuación se documenta el comportamiento del software ante equivocaciones del usuario:

### 1. Validación al Registrar un Jugador
* **Equivocación A (Nombre vacío):** Si presionas Enter sin escribir nada, el sistema lo detecta inmediatamente.
  * *Mensaje en terminal:* `❌ El nombre no puede quedar en blanco. Por favor, escribe uno.`
* **Equivocación B (Nombre repetido):** Si intentas registrar a alguien que ya existe (ej. "Alex"), el sistema bloquea el ingreso (no distingue entre mayúsculas y minúsculas).
  * *Mensaje en terminal:* `❌ Ese nombre ya está registrado. Intenta con otro o agrega un apellido.`
* [cite_start]**Equivocación C (Edad fuera de rango):** Si ingresas una edad menor a 12 o mayor a 70 años[cite: 153].
  * *Mensaje en terminal:* `❌ Lo siento, la edad debe estar entre los 12 y los 70 años para participar.`
* [cite_start]**Equivocación D (Tipo de dato inválido en edad o nivel):** Si por error escribes letras en lugar de números enteros[cite: 110].
  * *Mensaje en terminal:* `❌ Por favor, ingresa la edad usando solo números enteros.`

### 2. Validación al Formar Equipos
* [cite_start]**Equivocación A (Falta de jugadores):** Si intentas armar una pareja pero no hay al menos 2 personas registradas y libres en el sistema[cite: 110].
  * *Mensaje en terminal:* `❌ No hay suficientes jugadores libres para armar un equipo.`
* [cite_start]**Equivocación B (Nombre de equipo duplicado):** Si intentas usar un nombre que otra pareja ya registró[cite: 110].
  * *Mensaje en terminal:* `❌ Ese nombre ya está ocupado por otra pareja. Elige uno diferente.`

### 3. Validación al Anotar Partidas
* **Equivocación A (Jugar contra sí mismo):** Si seleccionas el mismo equipo para ocupar el puesto del Equipo A y del Equipo B.
  * *Mensaje en terminal:* `❌ Un equipo no puede jugar contra sí mismo. Elige un rival diferente.`

---

## 📂 Archivos del Repositorio

* `gestion_torneo.py`: Script principal en Python que contiene todo el código, el menú interactivo y la lógica de validaciones.
* `README.md`: Documentación e instrucciones del sistema.

---

## 🔧 Instrucciones de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/ValeriaPFR/Desafio5_Final_PixelesRetro.git](https://github.com/ValeriaPFR/Desafio5_Final_PixelesRetro.git)
