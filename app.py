import streamlit as st
import random
import time
import unicodedata

from streamlit_autorefresh import st_autorefresh

# --- Datos: Paises y Capitales ---
PAISES_CAPITALES = {
    "Afganistan": "Kabul",
    "Albania": "Tirana",
    "Alemania": "Berlin",
    "Andorra": "Andorra la Vieja",
    "Angola": "Luanda",
    "Antigua y Barbuda": "Saint John's",
    "Arabia Saudita": "Riad",
    "Argelia": "Argel",
    "Argentina": "Buenos Aires",
    "Armenia": "Erevan",
    "Australia": "Canberra",
    "Austria": "Viena",
    "Azerbaiyan": "Baku",
    "Bahamas": "Nasau",
    "Bangladesh": "Daca",
    "Barbados": "Bridgetown",
    "Barein": "Manama",
    "Belgica": "Bruselas",
    "Belice": "Belmopan",
    "Benin": "Porto Novo",
    "Bielorrusia": "Minsk",
    "Birmania (Myanmar)": "Naipyido",
    "Bolivia": "Sucre",
    "Bosnia y Herzegovina": "Sarajevo",
    "Botsuana": "Gaborone",
    "Brasil": "Brasilia",
    "Brunei": "Bandar Seri Begawan",
    "Bulgaria": "Sofia",
    "Burkina Faso": "Uagadugu",
    "Burundi": "Gitega",
    "Butan": "Timbu",
    "Cabo Verde": "Praia",
    "Camboya": "Nom Pen",
    "Camerun": "Yaunde",
    "Canada": "Ottawa",
    "Catar": "Doha",
    "Chad": "Yamena",
    "Chile": "Santiago",
    "China": "Pekin",
    "Chipre": "Nicosia",
    "Ciudad del Vaticano": "Ciudad del Vaticano",
    "Colombia": "Bogota",
    "Comoras": "Moroni",
    "Corea del Norte": "Pionyang",
    "Corea del Sur": "Seul",
    "Costa de Marfil": "Yamusukro",
    "Costa Rica": "San Jose",
    "Croacia": "Zagreb",
    "Cuba": "La Habana",
    "Dinamarca": "Copenhague",
    "Dominica": "Roseau",
    "Ecuador": "Quito",
    "Egipto": "El Cairo",
    "El Salvador": "San Salvador",
    "Emiratos Arabes Unidos": "Abu Dabi",
    "Eritrea": "Asmara",
    "Eslovaquia": "Bratislava",
    "Eslovenia": "Liubliana",
    "Espana": "Madrid",
    "Estados Unidos": "Washington D.C.",
    "Estonia": "Tallin",
    "Etiopia": "Adis Abeba",
    "Filipinas": "Manila",
    "Finlandia": "Helsinki",
    "Fiyi": "Suva",
    "Francia": "Paris",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Georgia": "Tiflis",
    "Ghana": "Accra",
    "Granada": "Saint George",
    "Grecia": "Atenas",
    "Guatemala": "Ciudad de Guatemala",
    "Guyana": "Georgetown",
    "Guinea": "Conakri",
    "Guinea-Bisau": "Bisau",
    "Guinea Ecuatorial": "Malabo",
    "Haiti": "Puerto Principe",
    "Honduras": "Tegucigalpa",
    "Hungria": "Budapest",
    "India": "Nueva Delhi",
    "Indonesia": "Yakarta",
    "Irak": "Bagdad",
    "Iran": "Teheran",
    "Irlanda": "Dublin",
    "Islandia": "Reikiavik",
    "Islas Marshall": "Majuro",
    "Islas Salomon": "Honiara",
    "Israel": "Jerusalen",
    "Italia": "Roma",
    "Jamaica": "Kingston",
    "Japon": "Tokio",
    "Jordania": "Aman",
    "Kazajistan": "Astana",
    "Kenia": "Nairobi",
    "Kirguistan": "Biskek",
    "Kiribati": "Tarawa",
    "Kuwait": "Kuwait City",
    "Laos": "Vientian",
    "Lesoto": "Maseru",
    "Letonia": "Riga",
    "Libano": "Beirut",
    "Liberia": "Monrovia",
    "Libia": "Tripoli",
    "Liechtenstein": "Vaduz",
    "Lituania": "Vilna",
    "Luxemburgo": "Luxemburgo",
    "Macedonia del Norte": "Skopie",
    "Madagascar": "Antananarivo",
    "Malasia": "Kuala Lumpur",
    "Malaui": "Lilongue",
    "Maldivas": "Male",
    "Mali": "Bamako",
    "Malta": "La Valeta",
    "Marruecos": "Rabat",
    "Mauricio": "Port Louis",
    "Mauritania": "Nuakchot",
    "Mexico": "Ciudad de Mexico",
    "Micronesia": "Palikir",
    "Moldavia": "Chisinau",
    "Monaco": "Monaco",
    "Mongolia": "Ulan Bator",
    "Montenegro": "Podgorica",
    "Mozambique": "Maputo",
    "Namibia": "Windhoek",
    "Nauru": "Yaren",
    "Nepal": "Katmandu",
    "Nicaragua": "Managua",
    "Niger": "Niamey",
    "Nigeria": "Abuya",
    "Noruega": "Oslo",
    "Nueva Zelanda": "Wellington",
    "Oman": "Mascate",
    "Paises Bajos": "Amsterdam",
    "Pakistan": "Islamabad",
    "Palaos": "Ngerulmud",
    "Palestina": "Jerusalen Este",
    "Panama": "Ciudad de Panama",
    "Papua Nueva Guinea": "Port Moresby",
    "Paraguay": "Asuncion",
    "Peru": "Lima",
    "Polonia": "Varsovia",
    "Portugal": "Lisboa",
    "Reino Unido": "Londres",
    "Republica Centroafricana": "Bangui",
    "Republica Checa": "Praga",
    "Republica del Congo": "Brazzaville",
    "Republica Democratica del Congo": "Kinshasa",
    "Republica Dominicana": "Santo Domingo",
    "Ruanda": "Kigali",
    "Rumania": "Bucarest",
    "Rusia": "Moscu",
    "Samoa": "Apia",
    "San Cristobal y Nieves": "Basseterre",
    "San Marino": "San Marino",
    "San Vicente y las Granadinas": "Kingstown",
    "Santa Lucia": "Castries",
    "Santo Tome y Principe": "Santo Tome",
    "Senegal": "Dakar",
    "Serbia": "Belgrado",
    "Seychelles": "Victoria",
    "Sierra Leona": "Freetown",
    "Singapur": "Singapur",
    "Siria": "Damasco",
    "Somalia": "Mogadiscio",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Suazilandia": "Mbabane",
    "Sudafrica": "Pretoria",
    "Sudan": "Jartum",
    "Sudan del Sur": "Yuba",
    "Suecia": "Estocolmo",
    "Suiza": "Berna",
    "Surinam": "Paramaribo",
    "Tailandia": "Bangkok",
    "Taiwan": "Taipei",
    "Tanzania": "Dodoma",
    "Tayikistan": "Dusambe",
    "Timor Oriental": "Dili",
    "Togo": "Lome",
    "Tonga": "Nukualofa",
    "Trinidad y Tobago": "Puerto Espana",
    "Tunez": "Tunez",
    "Turkmenistan": "Asjabat",
    "Turquia": "Ankara",
    "Tuvalu": "Funafuti",
    "Ucrania": "Kiev",
    "Uganda": "Kampala",
    "Uruguay": "Montevideo",
    "Uzbekistan": "Taskent",
    "Vanuatu": "Port Vila",
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Yemen": "Sana",
    "Yibuti": "Yibuti",
    "Zambia": "Lusaka",
    "Zimbabue": "Harare",
}

# --- Datos: Continentes ---
CONTINENTES = {
    "Europa": [
        "Albania", "Alemania", "Andorra", "Armenia", "Austria", "Azerbaiyan",
        "Belgica", "Bielorrusia", "Bosnia y Herzegovina", "Bulgaria", "Chipre",
        "Ciudad del Vaticano", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia",
        "Espana", "Estonia", "Finlandia", "Francia", "Georgia", "Grecia",
        "Hungria", "Irlanda", "Islandia", "Italia", "Kazajistan", "Letonia",
        "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte", "Malta",
        "Moldavia", "Monaco", "Montenegro", "Noruega", "Paises Bajos", "Polonia",
        "Portugal", "Reino Unido", "Republica Checa", "Rumania", "Rusia",
        "San Marino", "Serbia", "Suecia", "Suiza", "Turquia", "Ucrania",
    ],
    "Asia": [
        "Afganistan", "Arabia Saudita", "Barein", "Bangladesh", "Birmania (Myanmar)",
        "Brunei", "Butan", "Camboya", "Catar", "China", "Corea del Norte",
        "Corea del Sur", "Emiratos Arabes Unidos", "Filipinas", "India",
        "Indonesia", "Irak", "Iran", "Israel", "Japon", "Jordania",
        "Kirguistan", "Kuwait", "Laos", "Libano", "Malasia", "Maldivas",
        "Mongolia", "Nepal", "Oman", "Pakistan", "Palestina", "Singapur",
        "Siria", "Sri Lanka", "Tailandia", "Taiwan", "Tayikistan",
        "Timor Oriental", "Turkmenistan", "Uzbekistan", "Vietnam", "Yemen",
    ],
    "Africa": [
        "Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso", "Burundi",
        "Cabo Verde", "Camerun", "Chad", "Comoras", "Costa de Marfil",
        "Egipto", "Eritrea", "Etiopia", "Gabon", "Gambia", "Ghana",
        "Guinea", "Guinea-Bisau", "Guinea Ecuatorial", "Kenia", "Lesoto",
        "Liberia", "Libia", "Madagascar", "Malaui", "Mali", "Marruecos",
        "Mauricio", "Mauritania", "Mozambique", "Namibia", "Niger", "Nigeria",
        "Republica Centroafricana", "Republica del Congo",
        "Republica Democratica del Congo", "Ruanda", "Santo Tome y Principe",
        "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Sudafrica",
        "Sudan", "Sudan del Sur", "Suazilandia", "Tanzania", "Togo", "Tunez",
        "Uganda", "Yibuti", "Zambia", "Zimbabue",
    ],
    "America": [
        "Antigua y Barbuda", "Argentina", "Bahamas", "Barbados", "Belice",
        "Bolivia", "Brasil", "Canada", "Chile", "Colombia", "Costa Rica",
        "Cuba", "Dominica", "Ecuador", "El Salvador", "Estados Unidos",
        "Granada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica",
        "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru",
        "Republica Dominicana", "San Cristobal y Nieves",
        "San Vicente y las Granadinas", "Santa Lucia", "Surinam",
        "Trinidad y Tobago", "Uruguay", "Venezuela",
    ],
    "Oceania": [
        "Australia", "Fiyi", "Islas Marshall", "Islas Salomon", "Kiribati",
        "Micronesia", "Nauru", "Nueva Zelanda", "Palaos",
        "Papua Nueva Guinea", "Samoa", "Tonga", "Tuvalu", "Vanuatu",
    ],
}

TIEMPO_LIMITE = 10


# --- Funciones auxiliares ---

def normalizar(texto):
    """Normaliza texto: minusculas, sin tildes, sin caracteres especiales."""
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = "".join(c for c in texto if c.isalnum() or c == " ")
    texto = " ".join(texto.split())
    return texto


def obtener_paises_filtrados(continente):
    """Devuelve el subconjunto de PAISES_CAPITALES segun el continente."""
    if continente == "Todos":
        return PAISES_CAPITALES
    # Quitar emoji del nombre de continente si lo tiene
    nombre_limpio = continente.split(" ", 1)[-1] if " " in continente else continente
    paises_cont = CONTINENTES.get(nombre_limpio, [])
    return {p: c for p, c in PAISES_CAPITALES.items() if p in paises_cont}


def obtener_max_preguntas():
    """Devuelve el maximo de preguntas disponibles segun filtro."""
    datos = obtener_paises_filtrados(st.session_state.continente)
    return min(50, len(datos))


def get_jugador_actual():
    """Devuelve el dict del jugador actual en modo multijugador."""
    return st.session_state.jugadores[st.session_state.jugador_actual]


def nueva_pregunta(datos=None):
    """Selecciona una nueva pregunta aleatoria."""
    if datos is None:
        datos = obtener_paises_filtrados(st.session_state.continente)
    items = list(datos.items())

    if not items:
        st.session_state.quiz_terminado = True
        return

    max_preg = min(50, len(items)) if st.session_state.sub_modo == "50" else None

    if st.session_state.sub_modo == "50":
        disponibles = [
            i for i in range(len(items)) if i not in st.session_state.preguntados
        ]
        total = st.session_state.total
        if not disponibles or total >= max_preg:
            st.session_state.quiz_terminado = True
            return
        idx = random.choice(disponibles)
        st.session_state.preguntados.add(idx)
        pais, capital = items[idx]
    else:
        pais, capital = random.choice(items)

    if st.session_state.modo == "capital":
        st.session_state.pregunta = pais
        st.session_state.respuesta_correcta = capital
    else:
        st.session_state.pregunta = capital
        st.session_state.respuesta_correcta = pais

    st.session_state.respondido = False
    st.session_state.feedback = None
    st.session_state.pista_usada = False
    st.session_state.pista_mostrada = False

    if st.session_state.temporizador:
        st.session_state.tiempo_inicio = time.time()


def nueva_pregunta_repaso():
    """Selecciona la siguiente pregunta del repaso de errores."""
    if st.session_state.repaso_indice >= len(st.session_state.repaso_preguntas):
        st.session_state.modo_repaso = False
        return

    pregunta, respuesta = st.session_state.repaso_preguntas[st.session_state.repaso_indice]
    st.session_state.pregunta = pregunta
    st.session_state.respuesta_correcta = respuesta
    st.session_state.respondido = False
    st.session_state.feedback = None
    st.session_state.pista_usada = False
    st.session_state.pista_mostrada = False

    if st.session_state.temporizador:
        st.session_state.tiempo_inicio = time.time()


def registrar_acierto(con_pista=False):
    """Registra un acierto para el jugador actual."""
    if st.session_state.multijugador:
        j = get_jugador_actual()
        if con_pista:
            j["pista"] += 1
        else:
            j["aciertos"] += 1
        j["racha"] += 1
        if j["racha"] > j["racha_max"]:
            j["racha_max"] = j["racha"]
    else:
        if con_pista:
            st.session_state.aciertos_con_pista += 1
        else:
            st.session_state.aciertos += 1
        st.session_state.racha += 1
        if st.session_state.racha > st.session_state.racha_maxima:
            st.session_state.racha_maxima = st.session_state.racha


def registrar_error(pregunta, respuesta_correcta):
    """Registra un error para el jugador actual."""
    if st.session_state.multijugador:
        j = get_jugador_actual()
        j["errores"] += 1
        j["racha"] = 0
        j["errores_lista"].append((pregunta, respuesta_correcta))
    else:
        st.session_state.errores += 1
        st.session_state.racha = 0
        st.session_state.errores_lista.append((pregunta, respuesta_correcta))


def iniciar_juego():
    """Inicia una nueva partida."""
    st.session_state.juego_activo = True
    st.session_state.aciertos = 0
    st.session_state.aciertos_con_pista = 0
    st.session_state.errores = 0
    st.session_state.total = 0
    st.session_state.preguntados = set()
    st.session_state.quiz_terminado = False
    st.session_state.respondido = False
    st.session_state.feedback = None
    st.session_state.racha = 0
    st.session_state.racha_maxima = 0
    st.session_state.errores_lista = []
    st.session_state.pista_usada = False
    st.session_state.pista_mostrada = False
    st.session_state.modo_repaso = False
    st.session_state.repaso_preguntas = []
    st.session_state.repaso_indice = 0
    st.session_state.tiempo_inicio = None

    if st.session_state.multijugador:
        for j in st.session_state.jugadores:
            j["aciertos"] = 0
            j["pista"] = 0
            j["errores"] = 0
            j["racha"] = 0
            j["racha_max"] = 0
            j["errores_lista"] = []
        st.session_state.jugador_actual = 0

    nueva_pregunta()


def calcular_puntuacion(aciertos, pista, errores):
    """Calcula la puntuacion total."""
    return aciertos + pista * 0.5


# --- Configuracion de pagina ---
st.set_page_config(page_title="Quiz de Capitales", layout="centered")

# --- CSS personalizado ---
st.markdown("""
<style>
/* Tarjeta de pregunta */
[data-testid="stHeadingWithActionElements"] h2 {
    background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
    border-radius: 12px;
    padding: 1rem 1.5rem;
    border-left: 4px solid #F97316;
}

/* Barra de timer roja cuando queda poco */
[data-testid="stProgress"] > div > div > div {
    transition: background-color 0.3s ease;
}

/* Metricas estilizadas */
[data-testid="stMetric"] {
    background: #FFFBEB;
    border-radius: 10px;
    padding: 0.8rem;
    box-shadow: 0 1px 3px rgba(120,53,15,0.1);
    border: 1px solid #FDE68A;
}

/* Sidebar titulo */
[data-testid="stSidebar"] [data-testid="stHeadingWithActionElements"] h2 {
    background: none;
    border-left: none;
    padding: 0;
    font-size: 1.3rem;
    color: #EA580C;
}

[data-testid="stSidebar"] hr {
    border-color: #FDE68A;
}
</style>
""", unsafe_allow_html=True)

# --- Inicializar estado ---
if "juego_activo" not in st.session_state:
    st.session_state.juego_activo = False
    st.session_state.modo = "capital"
    st.session_state.sub_modo = "libre"
    st.session_state.continente = "Todos"
    st.session_state.multijugador = False
    st.session_state.temporizador = False
    st.session_state.pregunta = ""
    st.session_state.respuesta_correcta = ""
    st.session_state.respondido = False
    st.session_state.feedback = None
    st.session_state.aciertos = 0
    st.session_state.aciertos_con_pista = 0
    st.session_state.errores = 0
    st.session_state.total = 0
    st.session_state.preguntados = set()
    st.session_state.quiz_terminado = False
    st.session_state.racha = 0
    st.session_state.racha_maxima = 0
    st.session_state.errores_lista = []
    st.session_state.pista_usada = False
    st.session_state.pista_mostrada = False
    st.session_state.modo_repaso = False
    st.session_state.repaso_preguntas = []
    st.session_state.repaso_indice = 0
    st.session_state.tiempo_inicio = None
    st.session_state.jugadores = [
        {"nombre": "Jugador 1", "aciertos": 0, "pista": 0, "errores": 0,
         "racha": 0, "racha_max": 0, "errores_lista": []},
        {"nombre": "Jugador 2", "aciertos": 0, "pista": 0, "errores": 0,
         "racha": 0, "racha_max": 0, "errores_lista": []},
    ]
    st.session_state.jugador_actual = 0
    st.session_state.nombres_configurados = False

# --- Titulo ---
st.title("\U0001f30d Quiz de Capitales del Mundo")

# --- Barra lateral ---
with st.sidebar:
    st.header("\u2699\ufe0f Configuracion")

    modo = st.radio(
        "Modo de juego:",
        ["Adivinar la capital (dado un pais)", "Adivinar el pais (dada una capital)"],
    )

    continente = st.selectbox(
        "Continente:",
        ["Todos", "\U0001f30d Europa", "\U0001f30f Asia", "\U0001f30d Africa", "\U0001f30e America", "\U0001f30f Oceania"],
    )

    jugadores = st.radio(
        "Jugadores:",
        ["Individual", "2 jugadores"],
    )

    sub_modo = st.radio(
        "Tipo de partida:",
        ["Modo libre", "50 preguntas"],
    )

    temporizador = st.checkbox("\u23f1\ufe0f Activar temporizador (10s)")

    st.markdown("---")

    if st.button("\U0001f680 Comenzar partida", type="primary", use_container_width=True):
        st.session_state.modo = "capital" if "capital" in modo else "pais"
        st.session_state.sub_modo = "50" if "50" in sub_modo else "libre"
        st.session_state.continente = continente
        st.session_state.multijugador = jugadores == "2 jugadores"
        st.session_state.temporizador = temporizador
        st.session_state.nombres_configurados = not st.session_state.multijugador
        iniciar_juego()
        st.rerun()

    if st.session_state.juego_activo and not st.session_state.quiz_terminado:
        if st.button("\U0001f6d1 Terminar partida", use_container_width=True):
            if st.session_state.total > 0:
                st.session_state.quiz_terminado = True
            else:
                st.session_state.juego_activo = False
            st.rerun()

    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 0.8em;'>"
        "Desarrollado por <a href='https://github.com/falonso21' "
        "target='_blank' style='color: gray;'>Francisco Alonso</a>"
        "</div>",
        unsafe_allow_html=True,
    )

# --- Autorefresh para temporizador ---
if (st.session_state.juego_activo
        and st.session_state.temporizador
        and not st.session_state.respondido
        and not st.session_state.quiz_terminado
        and st.session_state.tiempo_inicio is not None):
    st_autorefresh(interval=1000, key="timer_refresh")

# --- Contenido principal ---

# Pantalla de bienvenida
if not st.session_state.juego_activo:
    st.markdown(
        """
    ### \U0001f44b Bienvenido al Quiz de Capitales

    Pon a prueba tus conocimientos sobre las capitales del mundo.

    **Modos disponibles:**
    - **Adivinar la capital**: Te damos un pais, adivina su capital
    - **Adivinar el pais**: Te damos una capital, adivina el pais

    **Tipos de partida:**
    - **Modo libre**: Preguntas sin fin para practicar
    - **50 preguntas**: Responde hasta 50 preguntas y obten tu puntuacion

    **Novedades:**
    - **Filtro por continente**: Practica con paises de un continente concreto
    - **Temporizador**: 10 segundos para responder cada pregunta
    - **Pistas**: Usa una pista (vale medio punto) si necesitas ayuda
    - **Racha**: Lleva la cuenta de tus respuestas consecutivas correctas
    - **Multijugador**: Juega con un amigo por turnos
    - **Repaso de errores**: Al terminar, repasa las preguntas que fallaste

    Selecciona tu modo en la barra lateral y pulsa **Comenzar partida**.
    """
    )

# Configuracion de nombres en multijugador
elif st.session_state.multijugador and not st.session_state.nombres_configurados:
    st.subheader("Configuracion de jugadores")
    nombre1 = st.text_input("Nombre del Jugador 1:", value="Jugador 1")
    nombre2 = st.text_input("Nombre del Jugador 2:", value="Jugador 2")
    if st.button("Empezar", type="primary"):
        st.session_state.jugadores[0]["nombre"] = nombre1 if nombre1.strip() else "Jugador 1"
        st.session_state.jugadores[1]["nombre"] = nombre2 if nombre2.strip() else "Jugador 2"
        st.session_state.nombres_configurados = True
        if st.session_state.temporizador:
            st.session_state.tiempo_inicio = time.time()
        st.rerun()

# Modo repaso de errores
elif st.session_state.modo_repaso:
    st.subheader("\U0001f4dd Repaso de errores")

    idx = st.session_state.repaso_indice
    total_repaso = len(st.session_state.repaso_preguntas)

    if idx >= total_repaso:
        st.success("Has terminado el repaso de errores.")
        if st.button("Volver", type="primary"):
            st.session_state.modo_repaso = False
            st.session_state.juego_activo = False
            st.rerun()
    else:
        st.caption(f"Repaso: {idx + 1} de {total_repaso}")

        pregunta = st.session_state.pregunta
        if st.session_state.modo == "capital":
            st.subheader(f"Cual es la capital de {pregunta}?")
        else:
            st.subheader(f"A que pais pertenece la capital {pregunta}?")

        # Timer en repaso
        if st.session_state.temporizador and st.session_state.tiempo_inicio and not st.session_state.respondido:
            transcurrido = time.time() - st.session_state.tiempo_inicio
            restante = max(0, TIEMPO_LIMITE - transcurrido)
            st.progress(restante / TIEMPO_LIMITE)
            st.caption(f"Tiempo restante: {int(restante)}s")

            if restante <= 0:
                correcta = st.session_state.respuesta_correcta
                st.session_state.feedback = (
                    "error",
                    f"\u23f0 Tiempo agotado! La respuesta correcta es: {correcta}",
                )
                st.session_state.respondido = True
                st.rerun()

        if not st.session_state.respondido:
            # Pista en repaso
            if not st.session_state.pista_mostrada:
                if st.button("\U0001f4a1 Pista", key="pista_repaso"):
                    st.session_state.pista_usada = True
                    st.session_state.pista_mostrada = True
                    st.rerun()

            if st.session_state.pista_mostrada:
                primera = st.session_state.respuesta_correcta[0]
                st.info(f"\U0001f4a1 La respuesta empieza por: **{primera}**")

            if st.session_state.temporizador:
                respuesta = st.text_input("Tu respuesta:", placeholder="Escribe aqui...",
                                          key=f"repaso_{idx}")
                submitted = st.button("\u2714\ufe0f Comprobar", type="primary", key=f"btn_repaso_{idx}")
            else:
                with st.form(key=f"form_repaso_{idx}"):
                    respuesta = st.text_input("Tu respuesta:", placeholder="Escribe aqui...")
                    submitted = st.form_submit_button("\u2714\ufe0f Comprobar", type="primary")

            if submitted and respuesta.strip():
                correcta = st.session_state.respuesta_correcta
                if normalizar(respuesta) == normalizar(correcta):
                    st.session_state.feedback = (
                        "success",
                        f"\u2705 Correcto! La respuesta es: {correcta}",
                    )
                else:
                    st.session_state.feedback = (
                        "error",
                        f"\u274c Incorrecto. La respuesta correcta es: {correcta}",
                    )
                st.session_state.respondido = True
                st.rerun()

        if st.session_state.respondido and st.session_state.feedback:
            tipo, msg = st.session_state.feedback
            if tipo == "success":
                st.success(msg)
            else:
                st.error(msg)

            if st.button("\u27a1\ufe0f Siguiente", type="primary", key="sig_repaso"):
                st.session_state.repaso_indice += 1
                if st.session_state.repaso_indice < total_repaso:
                    nueva_pregunta_repaso()
                st.rerun()

# Pantalla de resultados
elif st.session_state.quiz_terminado:
    st.header("\U0001f3c6 Partida terminada")
    st.markdown("---")

    if st.session_state.multijugador:
        j1 = st.session_state.jugadores[0]
        j2 = st.session_state.jugadores[1]

        p1 = calcular_puntuacion(j1["aciertos"], j1["pista"], j1["errores"])
        p2 = calcular_puntuacion(j2["aciertos"], j2["pista"], j2["errores"])

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(j1["nombre"])
            st.metric("Aciertos", j1["aciertos"])
            st.metric("Con pista (x0.5)", j1["pista"])
            st.metric("Errores", j1["errores"])
            st.metric("Puntuacion", f"{p1:.1f}")
            st.metric("Racha maxima", j1["racha_max"])

        with col2:
            st.subheader(j2["nombre"])
            st.metric("Aciertos", j2["aciertos"])
            st.metric("Con pista (x0.5)", j2["pista"])
            st.metric("Errores", j2["errores"])
            st.metric("Puntuacion", f"{p2:.1f}")
            st.metric("Racha maxima", j2["racha_max"])

        st.markdown("---")

        if p1 > p2:
            st.success(f"\U0001f3c6 Ganador: {j1['nombre']} con {p1:.1f} puntos!")
        elif p2 > p1:
            st.success(f"\U0001f3c6 Ganador: {j2['nombre']} con {p2:.1f} puntos!")
        else:
            st.info("\U0001f91d Empate!")

        # Repaso de errores multijugador: combinar errores de ambos
        todos_errores = j1["errores_lista"] + j2["errores_lista"]
        if todos_errores:
            with st.expander(f"📋 Ver fallos ({len(todos_errores)})"):
                for pregunta, correcta in todos_errores:
                    st.markdown(f"- **{pregunta}** → {correcta}")
            if st.button("Repasar errores", type="secondary"):
                # Eliminar duplicados manteniendo orden
                vistos = set()
                unicos = []
                for item in todos_errores:
                    if item not in vistos:
                        vistos.add(item)
                        unicos.append(item)
                st.session_state.repaso_preguntas = unicos
                st.session_state.repaso_indice = 0
                st.session_state.modo_repaso = True
                nueva_pregunta_repaso()
                st.rerun()

    else:
        aciertos = st.session_state.aciertos
        pista = st.session_state.aciertos_con_pista
        errores = st.session_state.errores
        total = st.session_state.total
        puntuacion = calcular_puntuacion(aciertos, pista, errores)
        porcentaje = (puntuacion / total * 100) if total > 0 else 0

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Aciertos", aciertos)
        col2.metric("Con pista (x0.5)", pista)
        col3.metric("Errores", errores)
        col4.metric("Puntuacion", f"{puntuacion:.1f}")

        st.caption(f"Racha maxima: {st.session_state.racha_maxima}")
        st.markdown("---")

        if porcentaje == 100:
            st.balloons()
            st.success("Perfecto! Eres un experto en capitales!")
        elif porcentaje >= 80:
            st.success("Muy bien! Tienes un gran conocimiento de las capitales.")
        elif porcentaje >= 60:
            st.warning("Nada mal, pero aun puedes mejorar.")
        elif porcentaje >= 40:
            st.warning("Necesitas repasar un poco mas.")
        else:
            st.error("Te queda mucho por aprender. Sigue practicando!")

        # Desplegable y boton de repaso de errores
        if st.session_state.errores_lista:
            with st.expander(f"📋 Ver fallos ({len(st.session_state.errores_lista)})"):
                for pregunta, correcta in st.session_state.errores_lista:
                    st.markdown(f"- **{pregunta}** → {correcta}")
            if st.button("Repasar errores", type="secondary"):
                st.session_state.repaso_preguntas = list(st.session_state.errores_lista)
                st.session_state.repaso_indice = 0
                st.session_state.modo_repaso = True
                nueva_pregunta_repaso()
                st.rerun()

    if st.button("Jugar de nuevo", type="primary"):
        st.session_state.juego_activo = False
        st.rerun()

# Quiz activo
else:
    # Mostrar turno en multijugador
    if st.session_state.multijugador:
        j = get_jugador_actual()
        st.info(f"\U0001f3af Turno de **{j['nombre']}**")

        # Marcadores de ambos jugadores
        j1 = st.session_state.jugadores[0]
        j2 = st.session_state.jugadores[1]
        p1 = calcular_puntuacion(j1["aciertos"], j1["pista"], j1["errores"])
        p2 = calcular_puntuacion(j2["aciertos"], j2["pista"], j2["errores"])

        mc1, mc2 = st.columns(2)
        mc1.caption(
            f"**{j1['nombre']}**: {p1:.1f} pts | "
            f"\U0001f525 Racha: {j1['racha']} (Max: {j1['racha_max']})"
        )
        mc2.caption(
            f"**{j2['nombre']}**: {p2:.1f} pts | "
            f"\U0001f525 Racha: {j2['racha']} (Max: {j2['racha_max']})"
        )

    # Marcador individual
    max_preg = obtener_max_preguntas()
    if st.session_state.sub_modo == "50":
        progreso = st.session_state.total / max_preg
        st.progress(progreso)
        caption_text = (
            f"Pregunta {st.session_state.total + 1} de {max_preg}"
        )
    else:
        caption_text = ""

    if not st.session_state.multijugador:
        aciertos = st.session_state.aciertos
        pista_count = st.session_state.aciertos_con_pista
        errores = st.session_state.errores
        punt = calcular_puntuacion(aciertos, pista_count, errores)
        racha = st.session_state.racha
        racha_max = st.session_state.racha_maxima
        stats = (
            f"Puntos: {punt:.1f}  |  "
            f"Aciertos: {aciertos}  |  Con pista: {pista_count}  |  "
            f"Errores: {errores}  |  "
            f"\U0001f525 Racha: {racha} (Max: {racha_max})"
        )
        if caption_text:
            caption_text += f"  |  {stats}"
        else:
            caption_text = stats

    if caption_text and st.session_state.total > 0:
        st.caption(caption_text)

    # Pregunta
    if st.session_state.modo == "capital":
        st.subheader(f"Cual es la capital de {st.session_state.pregunta}?")
    else:
        st.subheader(
            f"A que pais pertenece la capital {st.session_state.pregunta}?"
        )

    # Temporizador
    if st.session_state.temporizador and st.session_state.tiempo_inicio and not st.session_state.respondido:
        transcurrido = time.time() - st.session_state.tiempo_inicio
        restante = max(0, TIEMPO_LIMITE - transcurrido)
        st.progress(restante / TIEMPO_LIMITE)
        st.caption(f"Tiempo restante: {int(restante)}s")

        if restante <= 0:
            correcta = st.session_state.respuesta_correcta
            st.session_state.feedback = (
                "error",
                f"\u23f0 Tiempo agotado! La respuesta correcta es: {correcta}",
            )
            if not st.session_state.modo_repaso:
                registrar_error(st.session_state.pregunta, correcta)
                st.session_state.total += 1
            st.session_state.respondido = True
            st.rerun()

    # Formulario de respuesta
    if not st.session_state.respondido:
        # Boton de pista (antes del formulario)
        if not st.session_state.pista_mostrada:
            if st.button("\U0001f4a1 Pista", key="pista_btn"):
                st.session_state.pista_usada = True
                st.session_state.pista_mostrada = True
                st.rerun()

        if st.session_state.pista_mostrada:
            primera = st.session_state.respuesta_correcta[0]
            st.info(f"\U0001f4a1 La respuesta empieza por: **{primera}**")

        if st.session_state.temporizador:
            # Sin form para que autorefresh funcione
            respuesta = st.text_input(
                "Tu respuesta:", placeholder="Escribe aqui...",
                key=f"resp_{st.session_state.total}_{st.session_state.pregunta}"
            )
            submitted = st.button("\u2714\ufe0f Comprobar", type="primary",
                                  key=f"btn_{st.session_state.total}_{st.session_state.pregunta}")
        else:
            # Con form para poder usar Enter
            with st.form(key=f"form_{st.session_state.total}_{st.session_state.pregunta}"):
                respuesta = st.text_input("Tu respuesta:", placeholder="Escribe aqui...")
                submitted = st.form_submit_button("\u2714\ufe0f Comprobar", type="primary")

        if submitted:
            if respuesta.strip():
                correcta = st.session_state.respuesta_correcta
                if normalizar(respuesta) == normalizar(correcta):
                    st.session_state.feedback = (
                        "success",
                        f"\u2705 Correcto! La respuesta es: {correcta}",
                    )
                    registrar_acierto(con_pista=st.session_state.pista_usada)
                else:
                    st.session_state.feedback = (
                        "error",
                        f"\u274c Incorrecto. La respuesta correcta es: {correcta}",
                    )
                    registrar_error(st.session_state.pregunta, correcta)
                st.session_state.total += 1
                st.session_state.respondido = True
                st.rerun()
            else:
                st.warning("Escribe una respuesta antes de comprobar.")

    # Feedback y boton siguiente
    if st.session_state.respondido and st.session_state.feedback:
        tipo, msg = st.session_state.feedback
        if tipo == "success":
            st.success(msg)
        else:
            st.error(msg)

        max_preg = obtener_max_preguntas()
        if st.session_state.sub_modo == "50" and st.session_state.total >= max_preg:
            if st.button("Ver resultados", type="primary"):
                st.session_state.quiz_terminado = True
                st.rerun()
        else:
            if st.button("\u27a1\ufe0f Siguiente", type="primary"):
                # Cambiar turno en multijugador
                if st.session_state.multijugador:
                    st.session_state.jugador_actual = 1 - st.session_state.jugador_actual
                nueva_pregunta()
                st.rerun()
