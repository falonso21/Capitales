import streamlit as st
import random
import unicodedata

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


def normalizar(texto):
    """Normaliza texto: minusculas, sin tildes, sin caracteres especiales."""
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = "".join(c for c in texto if c.isalnum() or c == " ")
    texto = " ".join(texto.split())
    return texto


def nueva_pregunta():
    """Selecciona una nueva pregunta aleatoria."""
    items = list(PAISES_CAPITALES.items())

    if st.session_state.sub_modo == "50":
        disponibles = [
            i for i in range(len(items)) if i not in st.session_state.preguntados
        ]
        if not disponibles or st.session_state.total >= 50:
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


def iniciar_juego():
    """Inicia una nueva partida."""
    st.session_state.juego_activo = True
    st.session_state.aciertos = 0
    st.session_state.errores = 0
    st.session_state.total = 0
    st.session_state.preguntados = set()
    st.session_state.quiz_terminado = False
    st.session_state.respondido = False
    st.session_state.feedback = None
    nueva_pregunta()


# --- Configuracion de pagina ---
st.set_page_config(page_title="Quiz de Capitales", layout="centered")

# --- Inicializar estado ---
if "juego_activo" not in st.session_state:
    st.session_state.juego_activo = False
    st.session_state.modo = "capital"
    st.session_state.sub_modo = "libre"
    st.session_state.pregunta = ""
    st.session_state.respuesta_correcta = ""
    st.session_state.respondido = False
    st.session_state.feedback = None
    st.session_state.aciertos = 0
    st.session_state.errores = 0
    st.session_state.total = 0
    st.session_state.preguntados = set()
    st.session_state.quiz_terminado = False

# --- Titulo ---
st.title("Quiz de Capitales del Mundo")

# --- Barra lateral ---
with st.sidebar:
    st.header("Configuracion")

    modo = st.radio(
        "Modo de juego:",
        ["Adivinar la capital (dado un pais)", "Adivinar el pais (dada una capital)"],
    )

    sub_modo = st.radio(
        "Tipo de partida:",
        ["Modo libre", "50 preguntas"],
    )

    st.markdown("---")

    if st.button("Comenzar partida", type="primary", use_container_width=True):
        st.session_state.modo = "capital" if "capital" in modo else "pais"
        st.session_state.sub_modo = "50" if "50" in sub_modo else "libre"
        iniciar_juego()
        st.rerun()

    if st.session_state.juego_activo and not st.session_state.quiz_terminado:
        if st.button("Terminar partida", use_container_width=True):
            if st.session_state.sub_modo == "50" and st.session_state.total > 0:
                st.session_state.quiz_terminado = True
            else:
                st.session_state.juego_activo = False
            st.rerun()

# --- Contenido principal ---
if not st.session_state.juego_activo:
    st.markdown(
        """
    ### Bienvenido al Quiz de Capitales

    Pon a prueba tus conocimientos sobre las capitales del mundo.

    **Modos disponibles:**
    - **Adivinar la capital**: Te damos un pais, adivina su capital
    - **Adivinar el pais**: Te damos una capital, adivina el pais

    **Tipos de partida:**
    - **Modo libre**: Preguntas sin fin para practicar
    - **50 preguntas**: Responde 50 preguntas y obtén tu puntuacion

    Selecciona tu modo en la barra lateral y pulsa **Comenzar partida**.
    """
    )

elif st.session_state.quiz_terminado:
    # --- Pantalla de resultados ---
    st.header("Partida terminada")
    st.markdown("---")

    aciertos = st.session_state.aciertos
    total = st.session_state.total
    errores = st.session_state.errores
    porcentaje = (aciertos / total * 100) if total > 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Aciertos", aciertos)
    col2.metric("Errores", errores)
    col3.metric("Porcentaje", f"{porcentaje:.1f}%")

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

    if st.button("Jugar de nuevo", type="primary"):
        st.session_state.juego_activo = False
        st.rerun()

else:
    # --- Quiz activo ---

    # Marcador
    if st.session_state.sub_modo == "50":
        progreso = st.session_state.total / 50
        st.progress(progreso)
        st.caption(
            f"Pregunta {st.session_state.total + 1} de 50  |  "
            f"Aciertos: {st.session_state.aciertos}  |  "
            f"Errores: {st.session_state.errores}"
        )
    else:
        if st.session_state.total > 0:
            st.caption(
                f"Aciertos: {st.session_state.aciertos}  |  "
                f"Errores: {st.session_state.errores}"
            )

    # Pregunta
    if st.session_state.modo == "capital":
        st.subheader(f"Cual es la capital de {st.session_state.pregunta}?")
    else:
        st.subheader(
            f"A que pais pertenece la capital {st.session_state.pregunta}?"
        )

    # Formulario de respuesta
    if not st.session_state.respondido:
        with st.form(key=f"form_{st.session_state.total}_{st.session_state.pregunta}"):
            respuesta = st.text_input("Tu respuesta:", placeholder="Escribe aqui...")
            submitted = st.form_submit_button("Comprobar", type="primary")

            if submitted:
                if respuesta.strip():
                    correcta = st.session_state.respuesta_correcta
                    if normalizar(respuesta) == normalizar(correcta):
                        st.session_state.feedback = (
                            "success",
                            f"Correcto! La respuesta es: {correcta}",
                        )
                        st.session_state.aciertos += 1
                    else:
                        st.session_state.feedback = (
                            "error",
                            f"Incorrecto. La respuesta correcta es: {correcta}",
                        )
                        st.session_state.errores += 1
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

        if st.session_state.sub_modo == "50" and st.session_state.total >= 50:
            if st.button("Ver resultados", type="primary"):
                st.session_state.quiz_terminado = True
                st.rerun()
        else:
            if st.button("Siguiente", type="primary"):
                nueva_pregunta()
                st.rerun()
