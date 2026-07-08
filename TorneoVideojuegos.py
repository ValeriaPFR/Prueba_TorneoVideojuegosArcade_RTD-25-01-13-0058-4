"""
Prueba Final: Sistema de Gestión de Torneo de Videojuegos Retro
Curso: Fundamentos de Ciencias de Datos
Estudiante: Valeria Fariña Rebolledo
OTEC: Nueva CIASPO
"""

import statistics

# =====================================================================
# CAJAS DE ALMACENAMIENTO PARA GUARDAR LA INFORMACIÓN
# =====================================================================
# Aquí se guarda la lista de todas las personas inscritas
participantes = []  

# Aquí se guardan los equipos creados junto con sus puntajes 
equipos = {}        

# Aquí se guarda el registro de qué equipos jugaron y quién ganó
historial_partidas = []  


# =====================================================================
# 1. ENTRADA Y VALIDACIÓN DE DATOS 
# =====================================================================
def registrar_participante():
    """
    Pide los datos de un jugador, revisa que todo esté bien escrito
    y lo guarda en la lista del torneo[cite: 148].
    """
    print("\n--- REGISTRO DE NUEVO JUGADOR ---")
    
    # --- Preguntar el nombre ---
    while True:
        nombre = input("¿Cómo se llama el jugador?: ").strip()
        # Revisa que no se haya dejado el espacio vacío 
        if nombre:
            # Revisa que el nombre no se repita con otro ya inscrito
            duplicado = any(p['nombre'].lower() == nombre.lower() for p in participantes)
            if not duplicado:
                break  # Todo bien, avanza al siguiente paso
            else:
                print("❌ Ese nombre ya está registrado. Intenta con otro o agrega un apellido.")
        else:
            print("❌ El nombre no puede quedar en blanco. Por favor, escribe uno.")

    # --- Preguntar la edad ---
    while True:
        try:
            edad = int(input("¿Qué edad tiene? (Debe tener entre 12 y 70 años): "))  
            # Revisa que la edad esté dentro de los límites del torneo 
            if 12 <= edad <= 70:
                break  # Edad correcta, avanza al siguiente paso
            else:
                print("❌ Lo siento, la edad debe estar entre los 12 y los 70 años para participar.")
        except ValueError:
            # Si el usuario escribe letras en vez de números, muestra este aviso
            print("❌ Por favor, ingresa la edad usando solo números enteros.")

    # --- Preguntar el nivel de experiencia ---
    while True:
        try:
            print("¿Cuál es su nivel de experiencia jugando?")
            nivel = int(input("Elige un número del 1 (Principiante) al 5 (Experto): "))  
            # Revisa que el número elegido sea del 1 al 5 
            if 1 <= nivel <= 5:
                break  # Nivel correcto, avanza al siguiente paso
            else:
                print("❌ Opción inválida. Recuerda elegir un número del 1 al 5.")
        except ValueError:
            # Si el usuario escribe letras en vez de números, muestra este aviso
            print("❌ Por favor, ingresa solo un número del 1 al 5.")

    # --- Guardar al jugador ---
    # Junta los tres datos del jugador y los mete en la lista general 
    nuevo_jugador = {"nombre": nombre, "edad": edad, "nivel": nivel}
    participantes.append(nuevo_jugador)
    print(f"✅ ¡Genial! {nombre} ha sido registrado con éxito.")


# =====================================================================
# SECCIÓN EXTRA: LISTAR JUGADORES CON SU ASIGNACIÓN DE EQUIPO
# =====================================================================
def listar_jugadores():
    """
    Muestra en la pantalla la lista de todas las personas anotadas hasta ahora,
    indicando a qué pareja pertenecen o si todavía están libres.
    """
    print("\n==================================================")
    print("         JUGADORES INSCRITOS EN EL TORNEO         ")
    print("==================================================")
    
    # Revisa si la lista está vacía para avisarle al usuario
    if not participantes:
        print("Aún no se ha registrado ningún jugador en la base de datos.")
    else:
        # Muestra a los jugadores uno por uno colocándoles un número al lado 
        for idx, p in enumerate(participantes, start=1):
            
            # Buscamos si el jugador actual está en algún equipo registrado
            equipo_actual = "Ninguno (Disponible) 🟢"
            for nombre_eq, info_eq in equipos.items():
                if p["nombre"] in info_eq["jugadores"]:
                    equipo_actual = f"{nombre_eq} 🔵"
                    break  # Si ya lo encontramos, dejamos de buscar en los demás equipos
            
            # Imprimimos la fila con toda la información limpia y alineada 
            print(f"[{idx}] {p['nombre']:15} | Edad: {p['edad']} años | Nivel: {p['nivel']}/5 | Equipo: {equipo_actual}")
            
    print("==================================================")


# =====================================================================
# 2. GESTIÓN DE PARTICIPANTES Y EQUIPOS 
# =====================================================================
def formar_equipo():
    """
    Junta a dos jugadores que estén libres y les crea un equipo con nombre propio[cite: 165].
    """
    print("\n--- FORMACIÓN DE EQUIPOS (PAREJAS 2X2) ---")
    
    # --- Buscar quiénes ya tienen equipo ---
    jugadores_en_equipos = []
    for eq in equipos.values():
        jugadores_en_equipos.extend(eq["jugadores"])
        
    # Deja en esta lista solo a los que no se han sumado a ninguna pareja 
    jugadores_libres = [p for p in participantes if p["nombre"] not in jugadores_en_equipos]
    
    # Si queda menos de 2 personas libres, no se puede armar una pareja nueva
    if len(jugadores_libres) < 2:
        print("❌ No hay suficientes jugadores libres para armar un equipo.")
        print(f"Faltan integrantes (jugadores disponibles: {len(jugadores_libres)}). Necesitas mínimo 2.")
        return

    # --- Pedir el nombre del equipo ---
    while True:
        nombre_equipo = input("¿Qué nombre le pondrán al equipo?: ").strip()
        if not nombre_equipo:
            print("❌ El nombre del equipo no puede quedar vacío.")
        # Revisa que ninguna otra pareja se llame igual 
        elif nombre_equipo.lower() in [key.lower() for key in equipos.keys()]:
            print("❌ Ese nombre ya está ocupado por otra pareja. Elige uno diferente.")
        else:
            break

    # --- Elegir al integrante 1 ---
    print("\nJugadores disponibles que no tienen equipo:")
    for idx, jug in enumerate(jugadores_libres, start=1):
        print(f"[{idx}] {jug['nombre']} (Nivel: {jug['nivel']})")

    ...
    while True:
        try:
            sel1 = int(input("Escribe el número del PRIMER jugador para el equipo: "))
            if 1 <= sel1 <= len(jugadores_libres):
                jugador1 = jugadores_libres[sel1 - 1]  # Guarda al primer elegido
                break
            else:
                print("❌ El número elegido no está en la lista.")
        except ValueError:
            print("❌ Por favor, escribe el número que aparece al lado del jugador.")

    # --- Elegir al integrante 2 ---
    # Saca al primer elegido de la lista para que no se elija a sí mismo 
    jugadores_restantes = [j for j in jugadores_libres if j != jugador1]
    print("\nJugadores que quedan disponibles:")
    for idx, jug in enumerate(jugadores_restantes, start=1):
        print(f"[{idx}] {jug['nombre']} (Nivel: {jug['nivel']})")

    while True:
        try:
            sel2 = int(input("Escribe el número del SEGUNDO jugador para el equipo: "))
            if 1 <= sel2 <= len(jugadores_restantes):
                jugador2 = jugadores_restantes[sel2 - 1]  # Guarda al segundo elegido
                break
            else:
                print("❌ El número elegido no está en la lista.")
        except ValueError:
            print("❌ Por favor, escribe el número que aparece al lado del jugador.")

    # --- Guardar la pareja ---
    # Registra el nuevo equipo en el sistema empezando con 0 puntos 
    equipos[nombre_equipo] = {
        "jugadores": [jugador1["nombre"], jugador2["nombre"]],
        "puntos": 0
    }
    print(f"✅ ¡Pareja creada! El equipo '{nombre_equipo}' quedó formado por {jugador1['nombre']} y {jugador2['nombre']}.")


# =====================================================================
# 3. REGISTRO Y ANÁLISIS DE PARTIDAS 
# =====================================================================
def registrar_partida():
    """
    Permite elegir qué equipos jugaron, quién ganó y le suma sus 3 puntos[cite: 178, 182].
    """
    print("\n--- ANOTAR RESULTADO DE PARTIDA ---")
    
    # Revisa que existan al menos 2 parejas para poder jugar un partido
    if len(equipos) < 2:
        print("❌ Se necesitan al menos 2 equipos registrados para poder jugar una partida.")
        return

    # Muestra los equipos actuales en pantalla 
    lista_nombres_equipos = list(equipos.keys())
    print("Equipos inscritos en el torneo:")
    for idx, eq_name in enumerate(lista_nombres_equipos, start=1):
        print(f"[{idx}] {eq_name} ({equipos[eq_name]['puntos']} pts)")

    # --- Elegir el Equipo A ---
    while True:
        try:
            sel_a = int(input("Elige el número del EQUIPO A: "))
            if 1 <= sel_a <= len(lista_nombres_equipos):
                equipo_a = lista_nombres_equipos[sel_a - 1]
                break
            else:
                print("❌ El número seleccionado no es válido.")
        except ValueError:
            print("❌ Por favor, introduce solo el número de la lista.")

    # --- Elegir el Equipo B ---
    while True:
        try:
            sel_b = int(input("Elige el número del EQUIPO B (que no sea el mismo equipo A): "))
            if 1 <= sel_b <= len(lista_nombres_equipos):
                equipo_b = lista_nombres_equipos[sel_b - 1]
                # Evita que un equipo juegue contra sí mismo
                if equipo_b != equipo_a:
                    break
                else:
                    print("❌ Un equipo no puede jugar contra sí mismo. Elige un rival diferente.")
            else:
                print("❌ El número seleccionado no es válido.")
        except ValueError:
            print("❌ Por favor, introduce solo el número de la lista.")

    # --- Elegir quién ganó (BLOQUE CORREGIDO) ---
    print(f"\n¿Qué equipo ganó el juego entre '{equipo_a}' y '{equipo_b}'?")
    print(f"[1] {equipo_a}")
    print(f"[2] {equipo_b}")
    
    while True:
        op_ganador = input("Selecciona el ganador escribiendo 1 o 2: ").strip()
        if op_ganador == "1":
            ganador = equipo_a
            break
        elif op_ganador == "2":
            ganador = equipo_b
            break
        else:
            print("❌ Opción incorrecta. Escribe 1 si ganó el primer equipo o 2 si ganó el segundo.")

    # --- Sumar puntos y guardar registro ---
    # Le suma los 3 puntos ganados al puntaje de ese equipo 
    equipos[ganador]["puntos"] += 3
    
    # Guarda los detalles del juego en el cuaderno de bitácora del torneo 
    partida_info = {"encuentro": f"{equipo_a} vs {equipo_b}", "ganador": ganador}
    historial_partidas.append(partida_info)
    print(f"✅ ¡Puntaje actualizado! Se sumaron 3 puntos al equipo '{ganador}'.")


def mostrar_analisis_estadistico():
    """
    Saca cuentas automáticas sobre los puntajes usando funciones matemáticas.
    """
    print("\n========================================")
    print("         ESTADÍSTICAS DEL TORNEO        ")
    print("========================================")
    
    # Si no hay equipos creados, avisa para evitar un error de cálculo matemático
    if not equipos:
        print("Aviso: No hay equipos creados para calcular estadísticas.")
        print("========================================")
        return

    # Saca todos los puntajes de los equipos y los pone en una lista limpia
    puntajes = [eq["puntos"] for eq in equipos.values()]

    # Saca el puntaje promedio de todos los equipos
    promedio_puntos = statistics.mean(puntajes)
    
    # Encuentra el puntaje que quedó exactamente al medio de la lista
    mediana_puntos = statistics.median(puntajes)
    
    # Busca el puntaje que más se repite. Si todos son diferentes, muestra un aviso.
    try:
        moda_puntos = statistics.mode(puntajes)
    except statistics.StatisticsError:
        moda_puntos = "No hay un único puntaje repetido"

    # La cuenta de variedad requiere que jueguen al menos 2 equipos
    if len(puntajes) >= 2:
        desviacion_puntos = statistics.stdev(puntajes)
        txt_desviacion = f"{desviacion_puntos:.1f}"  # Lo deja con un solo decimal
    else:
        txt_desviacion = "Se necesitan al menos 2 equipos para este cálculo"

    # Muestra los resultados finales en pantalla ordenados y con un decimal 
    print(f"Promedio de puntos general    : {promedio_puntos:.1f}")
    print(f"Puntaje del centro (Mediana)  : {mediana_puntos:.1f}")
    
    if isinstance(moda_puntos, (int, float)):
        print(f"Puntaje más común (Moda)      : {moda_puntos:.1f}")
    else:
        print(f"Puntaje más común (Moda)      : {moda_puntos}")
        
    print(f"Variabilidad de puntos        : {txt_desviacion}")
    print("========================================")


# =====================================================================
# 4. REPORTES Y CIERRE 
# =====================================================================
def generar_reportes_completos():
    """
    Muestra los resúmenes finales de todo el torneo en la pantalla.
    """
    print("\n==================================================")
    print("        REPORTE OFICIAL - PIXELES RETRO           ")
    print("==================================================")

    # --- Sección 1: Jugadores ---
    print("\n--- JUGADORES REGISTRADOS ---")
    if not participantes:
        print("Aún no se ha registrado ningún jugador.")
    else:
        for idx, p in enumerate(participantes, start=1):
            print(f"[{idx}] {p['nombre']:18} | Edad: {p['edad']} años | Nivel: {p['nivel']}/5")

    # --- Sección 2: Parejas ---
    print("\n--- EQUIPOS Y SUS INTEGRANTES ---")
    if not equipos:
        print("Aún no se han formado equipos.")
    else:
        for name, info in equipos.items():
            print(f"• Pareja: {name:15} | Jugadores: {info['jugadores'][0]} y {info['jugadores'][1]}")

    # --- Sección 3: Tabla de Posiciones ---
    print("\n--- TABLA DE POSICIONES (RANKING ACTUAL) ---")
    if not equipos:
        print("No hay datos para mostrar en la tabla de posiciones.")
    else:
        # Ordena la lista de equipos de mayor a menor según los puntos que tengan
        ranking_ordenado = sorted(equipos.items(), key=lambda item: item[1]["puntos"], reverse=True)
        
        for lugar, (nombre_eq, datos_eq) in enumerate(ranking_ordenado, start=1):
            pts = datos_eq["puntos"]
            # Clasifica el desempeño del equipo según sus puntos ganados
            if pts >= 6:
                rendimiento = "Excelente"
            elif 1 <= pts < 6:
                rendimiento = "Bueno"
            else:
                rendimiento = "En desarrollo"
                
            print(f"Puesto {lugar}: {nombre_eq:12} -> {pts} Puntos | Desempeño: {rendimiento}")
            
    print("\n==================================================")


# =====================================================================
# MENÚ DE CONTROL PRINCIPAL DEL PROGRAMA
# =====================================================================
def menu():
    """
    Mantiene la lista de opciones en la pantalla y se queda esperando 
    a que el usuario elija qué quiere hacer.
    """
    while True:
        print("\n========================================")
        print("    SISTEMA DE GESTIÓN 'PIXELES RETRO'  ")
        print("========================================")
        print("1. Registrar un Jugador")
        print("2. Información de Todos los Jugadores")
        print("3. Armar un Equipo (Pareja)")
        print("4. Anotar Resultado de una Partida")
        print("5. Ver Estadísticas Generales")
        print("6. Ver Reportes y Tabla de Posiciones")
        print("7. Salir")
        print("========================================")
        
        opcion = input("Elige una opción (1 al 7): ").strip()
        
        # Revisa qué número se presionó y ejecuta esa acción
        if opcion == "1":
            registrar_participante()
        elif opcion == "2":
            listar_jugadores()
        elif opcion == "3":
            formar_equipo()
        elif opcion == "4":
            registrar_partida()
        elif opcion == "5":
            mostrar_analisis_estadistico()
        elif opcion == "6":
            generar_reportes_completos()
        elif opcion == "7":
            print("\n¡Gracias por usar el sistema! Saliendo del programa...")
            break  # Rompe la espera y apaga el programa por completo
        else:
            print("❌ Opción no válida. Por favor, escribe un número del 1 al 7.")


# Esta línea le dice a la computadora que empiece el programa corriendo el menú
if __name__ == "__main__":
    menu()