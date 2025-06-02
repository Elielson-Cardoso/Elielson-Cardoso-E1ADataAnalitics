import streamlit as st
import datetime
# import io # Não utilizado
# import base64 # Não utilizado

# --- Configurações da Página ---
st.set_page_config(
    page_title="E1A Data Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Cores personalizadas (baseadas na logo e tema de dados) ---
primary_color = "#264653"    # Azul escuro/petróleo
secondary_color = "#2a9d8f"  # Verde/azul mais claro
text_color = "#333333"       # Cinza escuro para o texto principal
background_color = "#F4F6F8"  # Cinza claro para o fundo
accent_color = "#e9c46a"     # Um toque de amarelo/dourado para destaque
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
    .css-1d391kg {{ /* Container principal do Streamlit - Pode precisar de ajuste dependendo da versão do Streamlit */
        padding-left: 1rem;
        padding-right: 1rem;
    }}
    /* Para versões mais recentes do Streamlit, o seletor do container principal pode ser mais estável assim:
       [data-testid="stAppViewContainer"] .main .block-container {{ ... }}
       ou de forma mais geral para o block-container:
       .block-container {{
           padding-left: 1rem !important;
           padding-right: 1rem !important;
       }}
    */
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
    .stImage {{ /* Estilo para o container da imagem do Streamlit */
        border-radius: 12px;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem; /* Espaço abaixo das imagens */
        text-align: center; /* Centraliza a imagem se ela for menor que a coluna */
    }}
    .stImage img {{ /* Estilo para a tag img dentro do container */
        border-radius: 12px; /* Garante que a imagem também tenha bordas arredondadas */
    }}
    .stAlert {{
        background-color: {accent_color};
        color: {text_color}; /* Alterado para text_color para melhor contraste, ou pode ser #000 */
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
        border: 1px solid {accent_color}; /* Borda sutil */
    }}
    .stMarkdown p {{
        font-size: 1.05em;
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
# O número do WhatsApp deve incluir o código do país (55 para Brasil) e DDD.
whatsapp_number_display = "(14) 99873-6036" # Para exibição
whatsapp_number_link = "5514998736036" # Para o link wa.me
whatsapp_url = f"https://wa.me/{whatsapp_number_link}"

# --- Cabeçalho com Logo e Título ---
col1, col2 = st.columns([1, 4], gap="medium") # Adicionado gap
with col1:
    try:
        st.image("logo.jpg", width=120) # Caminho para sua logo
    except FileNotFoundError:
        st.warning("Logo não encontrada! Verifique o caminho 'logo.jpg'.")
        st.image("https://placehold.co/120x120/cccccc/333333?text=E1A", width=120) # Placeholder

with col2:
    st.title("E1A Data Analytics")
    st.markdown("Transformando dados brutos em **insights estratégicos** para o seu negócio.")

st.markdown("---")

# --- Seção "Sobre Nós" ---
# Removida a definição de colunas aqui, pois não havia imagem diretamente associada a esta seção.
# O texto fluirá ocupando a largura disponível.
st.header("Sobre Nós")
st.write(
    """
    A E1A Data Analytics é uma empresa especializada em transformar dados brutos em **insights estratégicos** para o seu negócio.
    Atuamos nas frentes de **Business Intelligence (BI)**, **Análise de Dados** e **Ciência de Dados**,
    oferecendo soluções completas que permitem a você tomar decisões mais inteligentes e embasadas.
    """
)

# --- Nossos Pilares de Atuação ---
st.header("Nossos Pilares de Atuação:")

col_pilares_texto, col_pilares_img = st.columns([3, 1], gap="large") # Renomeado para clareza e adicionado gap

with col_pilares_texto:
    st.markdown("📈 **Business Intelligence (BI):** Visualizamos e entendemos seus dados através de painéis interativos e relatórios claros, proporcionando uma visão 360º do seu desempenho.")
    st.markdown("🔍 **Análise de Dados:** Nossas análises aprofundadas revelam padrões, tendências, oportunidades e desafios ocultos em seus dados, impulsionando a tomada de decisão.")
    st.markdown("🔮 **Ciência de Dados:** Construímos modelos preditivos robustos para antecipar cenários futuros, otimizar suas estratégias e gerar valor a longo prazo.")

with col_pilares_img:
    try:
        st.image("data2.jpg", caption="O poder dos dados", width=180) # Tamanho da imagem ajustado
    except FileNotFoundError:
        st.warning("Imagem 'data2.jpg' não encontrada.")
        st.image("https://placehold.co/180x180/cccccc/333333?text=Imagem+Pilares", width=180)

st.write("Na E1A Data Analytics, seu sucesso é impulsionado pelo **poder dos dados**.")

st.markdown("---")

# --- Contato ---
st.header("Fale Conosco!")
st.subheader("Nosso Especialista em Dados")

col_contact_info, col_contact_img = st.columns([2, 1], gap="large") # Renomeado e adicionado gap

with col_contact_info:
    st.markdown(f"""
    **Elielson Cardoso**<br>
    *Cientista de Dados e Fundador*

    📞 Contato: <a href="{whatsapp_url}" target="_blank">WhatsApp: {whatsapp_number_display}</a>
    """, unsafe_allow_html=True)
    # Observação: A frase abaixo refere-se a um QR Code.
    # Certifique-se de que 'data1.jpg' (exibida ao lado) seja de fato um QR Code para o WhatsApp,
    # ou altere esta frase/imagem para evitar confusão.
    st.write("Escaneie o QR Code ao lado para nos enviar uma mensagem direta no WhatsApp e iniciar sua jornada de dados!")

with col_contact_img:
    try:
        st.image("data1.jpg", caption="Entre em contato", width=180) # Tamanho da imagem ajustado
    except FileNotFoundError:
        st.warning("Imagem 'data1.jpg' não encontrada.")
        st.image("https://placehold.co/180x180/cccccc/333333?text=Contato", width=180)


st.markdown("---")

st.info("🚀 Pronto para transformar seus dados em resultados? Entre em contato e descubra como podemos impulsionar o seu negócio!")

# --- Rodapé ---
st.markdown(
    f"""
    <div class="footer">
        <p>&copy; {datetime.date.today().year} E1A Data Analytics. Todos os direitos reservados.</p>
        <p>Desenvolvido com Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)