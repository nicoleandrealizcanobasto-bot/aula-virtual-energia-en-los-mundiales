import streamlit as st

# Configuración del Aula Virtual
st.set_page_config(page_title="Aula Virtual: Energía en el Mundial", page_icon="🎓", layout="wide")

# Fondo de estrellas brillantes garantizado con CSS avanzado
st.markdown("""
    <style>
    /* Fondo general de la aplicación */
    .stApp {
        background: linear-gradient(to bottom, #050814, #121A2F) !important;
    }
    
    /* Capas de estrellas brillantes usando múltiples gradientes */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 40px 70px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 90px 40px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 160px 120px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(1.5px 1.5px at 230px 180px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 300px 250px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 380px 80px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(2.5px 2.5px at 450px 300px, #ffffff, rgba(0,0,0,0));
        background-repeat: repeat;
        background-size: 400px 400px;
        opacity: 0.8;
        z-index: 1;
        pointer-events: none;
        animation: twinkle 4s infinite alternate;
    }

    @keyframes twinkle {
        0% { opacity: 0.3; }
        100% { opacity: 1; }
    }

    /* Forzar transparencia en los contenedores de Streamlit para que se vea el fondo */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stToolbar"] {
        background-color: transparent !important;
    }
    
    .block-container {
        background-color: rgba(10, 15, 30, 0.75) !important;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    }

    h1, h2, h3, p, label, div, span {
        color: #F8F9FA !important;
    }
    </style>

    <!-- Reproductor de música de fondo en loop al 75% de volumen -->
    <audio id="musicaAmbiente" autoplay loop>
        <source src="musica_fondo.mp3" type="audio/mp3">
    </audio>
    <script>
        var audio = document.getElementById("musicaAmbiente");
        audio.volume = 0.75;
    </script>
    """, unsafe_allow_html=True)

st.title("🎓 Aula Virtual Interactiva: Grupo 2")
st.header("⚡ Sala: Un Mundial con Energía")
st.info("🎯 *Objetivo de la clase:* Descubrir ¿De dónde proviene la energía del Mundial y qué impacto genera producirla?")
st.write("---")

# Menú de navegación interactivo
st.sidebar.title("🗺️ Mapa del Aula Virtual")
estacion = st.sidebar.selectbox("Elige a qué estudiante quieres escuchar:", [
    "🏠 Entrada al Aula", 
    "🌊 Vaqui (El Océano)", 
    "🦏 Javi (La Sabana)", 
    "🦎 Axo (Los Ríos)", 
    "🦍 Gori (La Selva)", 
    "🐻‍❄️ Oso Polar (El Ártico)",
    "📝 Examen Final"
])

if estacion == "🏠 Entrada al Aula":
    st.subheader("¡Bienvenido al Aula Virtual, investigador! 🕵️‍♂️")
    st.write("Para que los estadios brillen, las pantallas transmitan y los aires acondicionados funcionen durante el Mundial, se necesita una cantidad monstruosa de *energía*.")
    st.write("Tus compañeros animales tienen algo muy importante que decirte sobre de dónde sale esa energía y cómo está destruyendo sus hogares. ¡Ve al menú de la izquierda y visita a cada uno!")

elif estacion == "🌊 Vaqui (El Océano)":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🌊 Charla con Vaqui, la Vaquita Marina")
        tab1, tab2 = st.tabs(["🗣️ Escuchar a Vaqui", "🔍 Ver Impacto"])
        
        with tab1:
            st.write("(Vaqui se acerca nadando hacia ti)")
            st.success("🗣️ *Vaqui dice:* '¡Hola! ¿Te has preguntado de dónde sale la electricidad para encender esos enormes estadios? Te lo diré: gran parte proviene de *combustibles fósiles como el petróleo y el gas natural*, los cuales los humanos extraen del fondo de mi hogar, el océano.'")
        
        with tab2:
            st.write("Haz clic en el botón para investigar el impacto de esta energía:")
            if st.button("💥 Descubrir Impacto"):
                st.balloons()
                st.toast('¡Splash! Burbujas en el agua 💦')
                st.error("📉 *El Impacto:* 'Al construir y operar plataformas petroleras marinas para generar esa energía, ocurren derrames de crudo que envenenan el agua. Además, el ruido de las máquinas de extracción arruina mi ecolocalización, ¡haciendo que me pierda en mi propio océano!'")
                
    with col2:
        st.image("vaqui.png", use_container_width=True)

elif estacion == "🦏 Javi (La Sabana)":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🦏 Charla con Javi el Rinoceronte")
        st.write("(Javi pisa fuerte la tierra seca y te mira)")
        st.warning("🗣️ *Javi dice:* '¡Saludos! Para llevar toda esa electricidad a las ciudades sede del Mundial, no solo queman gas, también construyen *megaplantas energéticas e hidroeléctricas gigantescas*.'")
        
        st.write("Mueve el deslizador y luego presiona el botón para ver el impacto:")
        hectareas = st.slider("Hectáreas destruidas", 0, 10000, 100)
        
        if st.button("Ver el impacto en la sabana"):
            if hectareas > 5000:
                st.balloons()
                st.toast('¡Pisotón fuerte! 🦏')
                st.error(f"📉 *El Impacto:* '¡Exacto! Se destruyen más de {hectareas} hectáreas. Para generar esa energía, talan árboles e inundan valles completos. Eso fragmenta mi territorio, me deja sin alimento y bloquea mis rutas de migración.'")
            else:
                st.info("Sube un poco más el deslizador, el daño es mucho mayor... ¡Vuelve a intentarlo!")

    with col2:
        st.image("javi.png", use_container_width=True)

elif estacion == "🦎 Axo (Los Ríos)":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🦎 Charla con Axo el Ajolote")
        st.write("(Axo asoma la cabeza desde el lago)")
        st.info("🗣️ *Axo dice:* 'La energía del Mundial también viene del mundo digital. Transmitir los partidos por internet y usar el VAR requiere *granjas de servidores* que consumen enormes cantidades de electricidad.'")
        
        st.write("Presiona el botón para ver qué pasa con el agua:")
        if st.button("🔍 Ver impacto en el agua"):
            st.balloons()
            st.toast('¡Bloop bloop! 🫧')
            st.error("📉 *El Impacto:* 'Esas plantas de energía y servidores se calientan mucho y usan *millones de litros de agua dulce* para enfriarse. Luego devuelven esa agua caliente a mis lagos, alterando la temperatura y dejándome sin oxígeno. ¡Me estoy cocinando!'")
            
    with col2:
        st.image("axo.png", use_container_width=True)

elif estacion == "🦍 Gori (La Selva)":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🦍 Charla con Gori el Gorila")
        st.write("(Gori se golpea el pecho para llamar tu atención)")
        st.success("🗣️ *Gori dice:* '¡Escucha humano! Toda esa energía que usan necesita viajar por cables, y requiere paneles o baterías inmensas. Todo eso se fabrica con minerales como el *cobre, litio y cobalto* que sacan de la tierra.'")
        
        if st.button("⛏️ Excavar para ver el impacto ambiental"):
            st.balloons()
            st.toast('¡Uhu uhu! 🦍')
            st.error("📉 *El Impacto:* 'Para obtener esos minerales energéticos, hacen minería a cielo abierto en mi selva. Talan los árboles donde duermo y los químicos de las minas envenenan la tierra donde crecen mis frutas.'")
            
    with col2:
        st.image("gori.png", use_container_width=True)

elif estacion == "🐻‍❄️ Oso Polar (El Ártico)":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🐻‍❄️ Charla con el Oso Polar")
        st.write("(El Oso te mira parado sobre un bloque de hielo muy pequeño)")
        st.info("🗣️ *Oso Polar dice:* 'Toda la *quema de carbón, petróleo y gas* para alimentar los estadios y las ciudades mundialistas sube hasta el cielo en forma de gases.'")
        
        if st.button("🌡️ Subir la temperatura global"):
            st.snow() # Único con efecto de nieve
            st.toast('¡Brrr! Se derrite el hielo ❄️')
            st.error("📉 *El Impacto:* '¡Ese es el problema! Esa energía genera toneladas de CO₂ (dióxido de carbono). Esto causa el *efecto invernadero*. Por culpa de esa energía, mi Ártico se está derritiendo a un ritmo acelerado y ya no tengo dónde cazar.'")

    with col2:
        st.image("oso.png", use_container_width=True)

elif estacion == "📝 Examen Final":
    st.subheader("📝 Evaluación del Aula Virtual")
    st.write("Demuestra lo que aprendiste interactuando con tus compañeros.")
    
    with st.form("quiz_energia"):
        q1 = st.selectbox("1. ¿De dónde dice Vaqui que proviene la energía que envenena su océano?", 
                          ["Selecciona una opción...", "De paneles solares", "De la extracción de petróleo y gas (fósiles)", "De la fuerza del viento"])
        
        q2 = st.radio("2. Según Axo, ¿qué impacto generan las plantas de energía y servidores en los lagos?", 
                      ["Los congelan", "Usan agua dulce para enfriarse y devuelven agua caliente y sin oxígeno", "Limpian la contaminación"])
        
        q3 = st.radio("3. ¿Por qué producir energía afecta al Oso Polar?", 
                      ["Porque los estadios le quitan el hielo", "Porque la quema de combustibles libera CO2 y derrite el hielo", "Porque hacen mucho ruido"])
        
        submit = st.form_submit_button("Entregar Examen 🎓")
        
        if submit:
            if q1 == "De la extracción de petróleo y gas (fósiles)" and q2 == "Usan agua dulce para enfriarse y devuelven agua caliente y sin oxígeno" and q3 == "Porque la quema de combustibles libera CO2 y derrite el hielo":
                st.balloons()
                st.success("¡APROBADO! 🎉 Has entendido perfectamente de dónde viene la energía del Mundial y su grave impacto ambiental.")
            else:
                st.warning("Vuelve a las salas e interactúa con los animales para encontrar las respuestas correctas. ¡Tú puedes!")
