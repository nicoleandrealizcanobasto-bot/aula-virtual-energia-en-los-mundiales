import streamlit as st

# Configuración del Aula Virtual
st.set_page_config(page_title="Aula Virtual: Energía en el Mundial", page_icon="🎓", layout="wide")

# CSS personalizado para fondo de estrellas y botones interactivos estilo juego
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #050814, #121A2F) !important;
    }
    
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

    /* Estilo botón de juegos interactivos */
    .btn-juego {
        display: inline-block;
        background-color: #FF4B4B;
        color: white !important;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        text-decoration: none;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(255, 75, 75, 0.4);
        margin-top: 10px;
        margin-bottom: 15px;
        transition: transform 0.2s, background-color 0.2s;
    }
    .btn-juego:hover {
        background-color: #E03E3E;
        transform: scale(1.03);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Aula Virtual Interactiva: Grupo 2")
st.header("⚡ Sala: Un Mundial con Energía")
st.info("🎯 Objetivo de la clase: Descubrir con datos exactos de dónde proviene la energía del Mundial y su verdadero costo ecológico.")
st.write("---")

# Menú lateral
st.sidebar.title("📚️ Mapa del Aula Virtual")
estacion = st.sidebar.selectbox("Selecciona un ecosistema para investigar:", [
    "🏠 Mapa de la Expedición", 
    "🌊 Vaqui, la vaquita marina", 
    "🦏 Javi, el rinoceronte de Java", 
    "🦎 Axo, el ajolote de Xochimilco", 
    "🦍 Gori, el gorila de montaña", 
    "🐻‍❄️ Polo, el oso polar del Ártico",
    "📝 Evaluación Oficial"
])

# ----------------------------------------------------
# 🏠 MAPA DE LA EXPEDICIÓN
# ----------------------------------------------------
if estacion == "🏠 Mapa de la Expedición": 
    st.subheader("Bienvenido a la Central de Investigación Ambiental 🔍")
    st.write("Para que los estadios brillen, las pantallas transmitan a nivel global y los sistemas de enfriamiento masivo funcionen durante el Mundial, se requiere una infraestructura energética monumental. A través de este mapa, investigarás los datos científicos y geográficos exactos que explican cómo la extracción y generación de esta energía altera drásticamente los biomas del planeta.")

# ----------------------------------------------------
# 🏠 MAPA DE LA EXPEDICIÓN
# ----------------------------------------------------
if estacion == "🏠 Mapa de la Expedición":
    
    # Esta es la línea que separa la bienvenida
    st.write("---") 
    
    # Aquí creamos las dos columnas
    col1, col2 = st.columns(2)
    
    # Lado izquierdo: La imagen de tamaño 450
    with col1:
        st.image("mapa.png",
                 caption="Mapa de las 5 estaciones ambientales. Utiliza el menú lateral para iniciar la investigación.", 
         width=450 )
        
    # Lado derecho: El texto
    with col2:
        st.subheader("🗺️ Mapa de la Expedición")
        st.write("En este mapa podrás ver los largos caminos que tendrás que recorrer para llegar a tu meta: la grandiosa evaluación oficial, ¡para convertirte en uno de nosotros! Explora cada estación, recolecta los datos necesarios y prepárate para el desafío final.")

# ----------------------------------------------------
# 🌊 VAQUI, LA VAQUITA MARINA
# ----------------------------------------------------
elif estacion == "🌊 Vaqui, la vaquita marina":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🌊 Impacto en Ecosistemas Marinos")
        
        tab1, tab2 = st.tabs(["📄 Informe Técnico", "💥 Simulador de Impacto"])
        
        with tab1:
            st.success("La energía requerida para iluminar los estadios y mantener las sedes operativas proviene mayoritariamente de la extracción de combustibles fósiles, como el petróleo y el gas natural. La instalación de plataformas marinas en zonas de alta biodiversidad implica el uso de cañones de aire sísmico para la exploración, un proceso que emite ondas de sonido tan intensas que destruyen la capacidad de ecolocalización de diversas especies marinas. Además, los constantes derrames de crudo contaminan el agua de forma prolongada y destruyen las cadenas alimenticias locales, haciendo que el entorno sea biológicamente inhabitable.")
            
        with tab2:
            st.write("Presiona el botón para simular una alteración acústica y química en el ecosistema marino:")
            if st.button("🚨 Simular Operación Petrolera"):
                st.balloons()
                st.toast('Alerta de contaminación acústica y química 🛢️')
                st.error("📉 Análisis de Impacto: La actividad industrial ha provocado un derrame del 15% del crudo extraído, mientras que las ondas sísmicas han desorientado a las poblaciones de cetáceos locales. El índice de supervivencia del ecosistema se reduce drásticamente.")
        
        st.write("---")
        st.subheader("🎮 Recursos Interactivos")
        st.markdown('<a href="https://wordwall.net/es/resource/118296199?wwmethod=link&wwshareintent=other" target="_blank" class="btn-juego">Da clic aquí para poder jugar y aprender con Vaqui</a>', unsafe_allow_html=True)

    with col2:
        st.image("vaqui.png", use_container_width=True)

# ----------------------------------------------------
# 🦏 JAVI, EL RINOCERONTE DE JAVA
# ----------------------------------------------------
elif estacion == "🦏 Javi, el rinoceronte de Java":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🦏 Impacto en Sabanas y Bosques Tropicales")
        
        st.warning("Para lograr transportar enormes cantidades de electricidad hacia las ciudades anfitrionas del Mundial, los gobiernos e industrias construyen megaplantas termoeléctricas e hidroeléctricas. La instalación de estas represas requiere la inundación de valles completos y la tala masiva de bosques, lo que resulta en la pérdida directa de miles de hectáreas de vegetación endémica. Esta alteración geográfica fragmenta el territorio de especies en peligro crítico, bloqueando sus rutas migratorias naturales y reduciendo sus fuentes de alimento y reproducción.")
        
        st.write("---")
        st.subheader("🎛️ Calculadora de Deforestación")
        hectareas = st.slider("Selecciona la escala del proyecto hidroeléctrico (Hectáreas removidas):", 0, 10000, 500)
        
        if st.button("💥 Ejecutar Cálculo de Fragmentación"):
            if hectareas > 4000:
                st.balloons()
                st.toast('Hábitat severamente fragmentado 🦏')
                st.error(f"📉 Análisis de Impacto: La remoción de {hectareas} hectáreas ha interrumpido el 80% de los corredores biológicos de los grandes mamíferos terrestres. El ecosistema ha perdido su capacidad de retención de agua y biodiversidad.")
            else:
                st.info("Aumenta la escala del proyecto en el deslizador para observar el verdadero impacto de las instalaciones del Mundial.")

        st.write("---")
        st.subheader("🎮 Recursos Interactivos")
        st.markdown('<a href="https://view.genially.com/6a975958bc2560881fc0dc70" target="_blank" class="btn-juego">Da clic aquí para poder jugar y aprender con Javi</a>', unsafe_allow_html=True)

    with col2:
        st.image("javi.png", use_container_width=True)

# ----------------------------------------------------
# 🦎 AXO, EL AJOLOTE DE XOCHIMILCO
# ----------------------------------------------------
elif estacion == "🦎 Axo, el ajolote de Xochimilco":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🦎 Impacto de la Energía Digital en Cuerpos de Agua")
        
        st.info("El soporte tecnológico del Mundial, como la transmisión global por internet, el análisis de datos masivos y el uso del VAR, depende de inmensas granjas de servidores que operan sin descanso. Estos centros de datos consumen una cantidad monumental de energía eléctrica y se calientan a niveles extremos, por lo que utilizan millones de litros de agua dulce extraída de ríos y lagos cercanos para sus sistemas de refrigeración. Al devolver esa agua al ecosistema, la temperatura del entorno acuático aumenta drásticamente, lo que provoca la pérdida de oxígeno disuelto y genera una contaminación térmica que acaba con los anfibios y la vida acuática sensible.")
        
        st.write("---")
        st.subheader("🌡️ Termómetro de Contaminación Térmica")
        
        temp = st.select_slider("Temperatura de descarga del agua residual:", options=["Normal (18°C)", "Cálida (25°C)", "Peligrosa (38°C)"])
        
        if st.button("🔍 Medir Oxígeno Disuelto"):
            if temp == "Peligrosa (38°C)":
                st.balloons()
                st.toast('Niveles de oxígeno críticos 🫧')
                st.error("📉 Análisis de Impacto: El aumento térmico provocado por el sistema de refrigeración de los servidores ha reducido el oxígeno en el agua por debajo del límite de supervivencia. Se registra hipoxia severa en el sistema lacustre.")
            else:
                st.info("Mueve el indicador hacia 'Peligrosa (38°C)' para observar el impacto real del funcionamiento continuo de los servidores mundiales.")

        st.write("---")
        st.subheader("🎮 Recursos Interactivos")
        st.markdown('<a href="https://wordwall.net/es/resource/118361869?wwmethod=link&wwshareintent=student" target="_blank" class="btn-juego">Da clic aquí para poder jugar y aprender con Axo</a>', unsafe_allow_html=True)

    with col2:
        st.image("axo.png", use_container_width=True)

# ----------------------------------------------------
# 🦍 GORI, EL GORILA DE MONTAÑA
# ----------------------------------------------------
elif estacion == "🦍 Gori, el gorila de montaña":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🦍 Impacto de la Minería para Transición Energética")
        
        st.success("La transición hacia tecnologías de iluminación eficiente y almacenamiento de energía en los estadios requiere la fabricación masiva de baterías, kilómetros de cableado subterráneo y sistemas de paneles solares. Estos componentes dependen enteramente de la extracción de minerales críticos como el cobre, el litio y el cobalto mediante procesos de minería a cielo abierto. Esta práctica industrial exige la deforestación total de zonas selváticas montañosas y el uso intensivo de químicos reactivos para separar los metales de la roca. Los residuos altamente tóxicos de esta minería se filtran en los suelos, envenenando progresivamente los mantos acuíferos que sostienen la red trófica de la selva.")
        
        st.write("---")
        st.subheader("⛏️ Simulador de Extracción de Minerales")
        
        minado = st.checkbox("Iniciar excavación para obtener Litio y Cobalto")
        if minado:
            st.balloons()
            st.toast('Suelo contaminado detectado 🦍')
            st.error("📉 Análisis de Impacto: La excavación ha deforestado por completo la cima de la montaña. Además, la lluvia ha arrastrado los ácidos de la mina hacia las aguas subterráneas, alterando el pH del suelo y eliminando los recursos alimenticios primarios.")

        st.write("---")
        st.subheader("🎮 Recursos Interactivos")
        st.markdown('<a href="https://view.genially.com/6a9762a9f0171bd0175211f6" target="_blank" class="btn-juego">Da clic aquí para poder jugar y aprender con Gori</a>', unsafe_allow_html=True)

    with col2:
        st.image("gori.png", use_container_width=True)

# ----------------------------------------------------
# 🐻‍❄️ POLO, EL OSO POLAR DEL ÁRTICO
# ----------------------------------------------------
elif estacion == "🐻‍❄️ Polo, el oso polar del Ártico":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🐻‍❄️ Impacto de las Emisiones Globales")
        
        st.info("Toda la infraestructura descrita anteriormente, sumada a la quema directa de carbón, petróleo y gas para satisfacer los picos de demanda energética durante los partidos oficiales, emite millones de toneladas de dióxido de carbono y otros gases de efecto invernadero a la atmósfera. Esta concentración inusual de gases crea una barrera que atrapa el calor solar, provocando una alteración acelerada en la temperatura promedio del planeta. En consecuencia directa de este calentamiento global inducido, las capas de hielo del Ártico sufren un derretimiento prematuro, lo que elimina permanentemente las plataformas de hielo sólido que resultan vitales para la caza, el descanso y la reproducción de las especies polares.")
        
        st.write("---")
        st.subheader("❄️ Modelo de Derretimiento Ártico")
        if st.button("🌡️ Proyectar Acumulación de Gases de Efecto Invernadero"):
            st.snow()
            st.toast('Pérdida de masa de hielo registrada ❄️')
            st.error("📉 Análisis de Impacto: La concentración de CO2 ha elevado la temperatura promedio 1.5 grados. Las imágenes satelitales confirman la reducción del 40% del hielo marino en la temporada de caza, llevando a las poblaciones de mamíferos polares a la inanición.")

        st.write("---")
        st.subheader("🎮 Recursos Interactivos")
        st.markdown('<a href="https://wordwall.net/es/resource/118362513?wwmethod=link&wwshareintent=student" target="_blank" class="btn-juego">Da clic aquí para poder jugar y aprender con Polo</a>', unsafe_allow_html=True)

    with col2:
        st.image("oso.png", use_container_width=True)

# ----------------------------------------------------
# 📝 EVALUACIÓN OFICIAL
# ----------------------------------------------------
elif estacion == "📝 Evaluación Oficial":
    st.subheader("🏆 Evaluación Científica del Aula Virtual")
    st.write("Demuestra tu comprensión técnica sobre los impactos ambientales provocados por la infraestructura energética respondiendo este cuestionario.")
    
    with st.form("quiz_interactivo"):
        q1 = st.selectbox("1. ¿Qué consecuencia directa genera el uso de cañones de aire sísmico para buscar petróleo en el océano?", 
                          ["Selecciona una respuesta...", "Aumenta la cantidad de peces disponibles.", "Destruye la capacidad de ecolocalización de las especies marinas.", "Congela el agua de los océanos a gran velocidad."])
        
        q2 = st.radio("2. Al construir megaplantas hidroeléctricas, ¿cuál es el daño directo al hábitat del Rinoceronte de Java?", 
                      ["La inundación de valles fragmenta el territorio y bloquea sus rutas migratorias.", "Se mejora la fertilidad del suelo para pastar.", "Disminuye la temperatura local considerablemente."])
        
        q3 = st.radio("3. ¿Por qué las granjas de servidores necesarias para el VAR provocan contaminación térmica en los lagos?", 
                      ["Porque utilizan energía nuclear radiactiva.", "Porque emiten gases tóxicos por chimeneas gigantes.", "Porque extraen agua dulce para refrigeración y la devuelven caliente, eliminando el oxígeno."])
        
        q4 = st.selectbox("4. ¿Para qué se requiere la minería a cielo abierto de litio y cobalto durante los eventos mundiales?", 
                          ["Selecciona una respuesta...", "Para fabricar baterías de almacenamiento y sistemas de transmisión eléctrica.", "Para construir asientos de plástico en los estadios.", "Para filtrar el agua potable de las ciudades."])
        
        q5 = st.radio("5. ¿Qué proceso físico provoca el derretimiento de las plataformas de hielo vitales para el Oso Polar?", 
                      ["La vibración constante de las máquinas perforadoras.", "La concentración de dióxido de carbono que atrapa el calor solar en la atmósfera.", "El uso de redes de arrastre en las zonas de pesca."])
        
        q6 = st.radio("6. ¿Qué ocurre con los químicos utilizados para separar metales en la minería de las montañas?", 
                      ["Se evaporan sin causar daños en la zona.", "Se convierten en abono para la selva.", "Se filtran en los suelos y envenenan progresivamente los mantos acuíferos."])
        
        submit = st.form_submit_button("🎓 Evaluar y Calificar Resultados")
        
        if submit:
            aciertos = 0
            if q1 == "Destruye la capacidad de ecolocalización de las especies marinas.": aciertos += 1
            if q2 == "La inundación de valles fragmenta el territorio y bloquea sus rutas migratorias.": aciertos += 1
            if q3 == "Porque extraen agua dulce para refrigeración y la devuelven caliente, eliminando el oxígeno.": aciertos += 1
            if q4 == "Para fabricar baterías de almacenamiento y sistemas de transmisión eléctrica.": aciertos += 1
            if q5 == "La concentración de dióxido de carbono que atrapa el calor solar en la atmósfera.": aciertos += 1
            if q6 == "Se filtran en los suelos y envenenan progresivamente los mantos acuíferos.": aciertos += 1
            
            if aciertos == 6:
                st.balloons()
                st.success(f"🎉 ¡CALIFICACIÓN PERFECTA! Lograste {aciertos}/6 aciertos. Has asimilado con éxito todos los datos técnicos del impacto ambiental.")
            elif aciertos >= 4:
                st.info(f"👍 Buen desempeño. Obtuviste {aciertos}/6 aciertos. Puedes repasar los informes técnicos para alcanzar la calificación máxima.")
            else:
                st.warning(f"Obtuviste {aciertos}/6 aciertos. Te sugerimos volver a las estaciones para leer con cuidado la información científica antes de volver a intentarlo.")
