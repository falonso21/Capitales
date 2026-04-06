# Quiz de Capitales del Mundo

Aplicacion web interactiva para poner a prueba tus conocimientos sobre las capitales del mundo. Construida con Streamlit.

## Funcionalidades

- **Dos modos de juego**: Adivinar la capital (dado un pais) o adivinar el pais (dada una capital)
- **Filtro por continente**: Europa, Asia, Africa, America, Oceania o todos
- **Dos tipos de partida**: Modo libre (sin fin) o 50 preguntas con puntuacion final
- **Temporizador**: 10 segundos por pregunta (opcional)
- **Pistas**: Muestra la primera letra de la respuesta a cambio de medio punto
- **Racha**: Contador de respuestas consecutivas correctas
- **Multijugador**: Modo para 2 jugadores por turnos
- **Repaso de errores**: Al terminar una partida, repasa las preguntas que fallaste

## Requisitos

- Python 3.9+
- Dependencias en `requirements.txt`

## Instalacion

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uso

```bash
streamlit run app.py
```

## Autor

Desarrollado por [Francisco Alonso](https://github.com/falonso21)
