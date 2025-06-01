import streamlit as st
import qrcode
import io
import base64

# --- Configurações da Página ---
st.set_page_config(
    page_title="E1A Data Analytics",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Cores personalizadas (baseadas na logo e tema de dados) ---
# Você pode ajustar esses valores hexadecimais para combinar perfeitamente com sua logo
primary_color = "#264653"  # Azul escuro/petróleo
secondary_color = "#2a9d8f" # Verde/azul mais claro
text_color = "#333333"     # Cinza escuro para o texto principal
background_color = "#F4F6F8" # Cinza claro para o fundo
accent_color = "#e9c46a"   # Um toque de amarelo/dourado para destaque
footer_text_color = "#6c757d" # Cor para o texto do rodapé

# --- Injeção de CSS Customizado para o Tema ---
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    .stApp {{
        background-color: {background_color};
        color: {text_color};
        font-family: 'Inter', sans-serif;
        padding-top: 2rem; /* Adiciona um pouco de espaço no topo */
        padding-bottom: 2rem; /* Adiciona um pouco de espaço na parte inferior */
    }}
    .css-1d391kg {{ /* Container principal do Streamlit */
        padding-left: 1rem;
        padding-right: 1rem;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {primary_color};
        font-weight: 700; /* Mais peso para títulos */
        margin-bottom: 0.8em;
    }}
    .stButton>button {{
        background-color: {secondary_color};
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 25px;
        font-size: 16px;
        cursor: pointer;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        font-weight: 600;
    }}
    .stButton>button:hover {{
        background-color: #218c7d; /* Um tom ligeiramente mais escuro ao passar o mouse */
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3);
        transform: translateY(-2px);
    }}
    .stImage {{
        border-radius: 12px;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem; /* Espaço abaixo das imagens */
    }}
    .stAlert {{
        background-color: {accent_color};
        color: {text_color};
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
        border: 1px solid {accent_color}; /* Borda sutil */
    }}
    .stMarkdown p {{
        font-size: 1.05em; /* Ligeiramente menor para corpo de texto */
        line-height: 1.7;
        margin-bottom: 1em;
    }}
    .stMarkdown ul {{
        list-style-type: none; /* Remove marcadores de lista padrão */
        padding-left: 0;
    }}
    .stMarkdown ul li {{
        margin-bottom: 0.5em;
        position: relative;
        padding-left: 1.5em;
    }}
    .stMarkdown ul li::before {{
        content: '•'; /* Adiciona um marcador de lista personalizado */
        color: {secondary_color};
        position: absolute;
        left: 0;
        font-weight: bold;
    }}
    .footer {{
        font-size: 0.9em;
        color: {footer_text_color};
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #e0e0e0;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Geração do QR Code para WhatsApp ---
# O número do WhatsApp deve incluir o código do país (55 para Brasil)
whatsapp_number = "014998736036"
whatsapp_url = f"https://wa.me/{whatsapp_number}"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Alta correção de erro
    box_size=10,
    border=4,
)
qr.add_data(whatsapp_url)
qr.make(fit=True)

img_qr = qr.make_image(fill_color=primary_color, back_color="white") # Cor do QR code com a primary_color

# Converte a imagem do QR code para base64 para exibir no Streamlit
buffered_qr = io.BytesIO()
img_qr.save(buffered_qr, format="PNG")
img_str_qr = base64.b64encode(buffered_qr.getvalue()).decode()

# --- Cabeçalho com Logo e Título ---
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo.jpg", width=120) # Caminho para sua logo
    except FileNotFoundError:
        st.warning("Logo não encontrada! Certifique-se de que 'logo.jpg' está na mesma pasta.")
        st.image("https://placehold.co/120x120/cccccc/333333?text=E1A", width=120) # Placeholder se a logo não for encontrada

with col2:
    st.title("E1A Data Analytics")
    st.write("Transformando dados brutos em **insights estratégicos** para o seu negócio.")

st.markdown("---")

# --- Seção "Sobre Nós" com Imagem ---
col_pilares_1, col_pilares_2 = st.columns([3, 1])

with col_pilares_1:
    st.header("Sobre Nós")
    st.write(
        """
        A E1A Data Analytics é uma empresa especializada em transformar dados brutos em **insights estratégicos** para o seu negócio.
        Atuamos nas frentes de **Business Intelligence (BI)**, **Análise de Dados** e **Ciência de Dados**,
        oferecendo soluções completas que permitem a você tomar decisões mais inteligentes e embasadas.
        """
    )
#with col_pilares_2:
#    try:
#        st.image("data1.jpg", caption="Transformando dados em insights", use_column_width=True) # Imagem para a seção "Sobre Nós"
#    except FileNotFoundError:
#        st.warning("Imagem 'data1.jpg' não encontrada. Certifique-se de que está na mesma pasta.")
#        st.image("https://placehold.co/600x300/cccccc/333333?text=Imagem+Sobre+Nós", use_column_width=True)


# --- Como Ajudamos as Empresas ---
st.header("Nossos Pilares de Atuação:")

col_pilares_1, col_pilares_2 = st.columns([3, 1])

with col_pilares_1:
    st.markdown("📈 **Business Intelligence (BI):** Visualizamos e entendemos seus dados através de painéis interativos e relatórios claros, proporcionando uma visão 360º do seu desempenho.")
    st.markdown("🔍 **Análise de Dados:** Nossas análises aprofundadas revelam padrões, tendências, oportunidades e desafios ocultos em seus dados, impulsionando a tomada de decisão.")
    st.markdown("🔮 **Ciência de Dados:** Construímos modelos preditivos robustos para antecipar cenários futuros, otimizar suas estratégias e gerar valor a longo prazo.")

with col_pilares_2:
    try:
        st.image("data2.jpg", caption="O poder dos dados", width=200) # Imagem para os pilares de atuação
    except FileNotFoundError:
        st.warning("Imagem 'data2.jpg' não encontrada. Certifique-se de que está na mesma pasta.")
        st.image("https://placehold.co/200x200/cccccc/333333?text=Imagem+Pillares", width=200)

st.write("Na E1A Data Analytics, seu sucesso é impulsionado pelo **poder dos dados**.")

st.markdown("---")

# --- Contato ---
st.header("Fale Conosco!")
st.subheader("Nosso Especialista em Dados")

col_contact_1, col_contact_2 = st.columns([2, 1])

with col_contact_1:
    st.markdown(f"""
    **Elielson Cardoso**
    *Cientista de Dados e Fundador*
    📞 Contato: [WhatsApp: {whatsapp_number}](https://wa.me/{whatsapp_number})
    """)
    st.write("Escaneie o QR Code ao lado para nos enviar uma mensagem direta no WhatsApp e iniciar sua jornada de dados!")

with col_contact_2:
    st.image(f"data:image/png;base64,{img_str_qr}", caption="Escaneie para Contato WhatsApp", width=150)

st.markdown("---")

st.info("Pronto para transformar seus dados em resultados? Entre em contato e descubra como podemos impulsionar o seu negócio!")

# --- Rodapé ---
st.markdown(
    f"""
    <div class="footer">
        <p>&copy; 2025 E1A Data Analytics. Todos os direitos reservados.</p>
        <p>Desenvolvido com Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
