import streamlit as st
import pandas as pd # Mantido caso use em outras partes, não usado no gráfico HTML
import numpy as np  # Mantido caso use em outras partes, não usado no gráfico HTML
import time # Mantido caso use em outras partes, não usado no gráfico HTML
import datetime
import streamlit.components.v1 as components
import urllib.parse

# --- Configurações da Página ---
st.set_page_config(
    page_title="E1A Data Analytics - Ouro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Nova Paleta de Cores (Tema Ouro e Profissional) ---
primary_color = "#B08D57"      # Ouro envelhecido/Bronze - Para títulos e elementos principais
secondary_color = "#4A4A4A"    # Cinza Chumbo - Para botões, elementos secundários
text_color = "#333333"         # Cinza Escuro - Texto principal
background_color = "#FDFBF5"   # Branco Neve/Off-white com leve tom creme - Fundo principal
accent_color = "#D4AF37"       # Ouro Metálico Suave - Para destaques, alertas
widget_background_color = "#FFFFFF" # Branco puro - Para fundos de widgets/cards se necessário
footer_text_color = "#555555"   # Cinza para o texto do rodapé


# --- Injeção de CSS Customizado para o Tema ---
st.markdown(
    f"""
    <style>
    @import url('https://fonts.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* O Streamlit já gerencia a cor do body e .stApp com base no tema.
       Removendo essas definições para que o modo escuro funcione.
       Se você mantiver, ele força o fundo claro/texto escuro sempre.
    */
    body {{
        font-family: 'Inter', sans-serif;
        /* A linha abaixo foi removida, pois 'text_color' não existe mais como variável Python */
        /* color: {text_color}; */
    }}

    /* .stApp {{
        background-color: {background_color}; REMOVIDO
        padding-top: 2.5rem;
        padding-bottom: 2.5rem;
    }} */

    .main .block-container {{
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: {primary_color}; /* Seus títulos manterão a cor ouro */
        font-weight: 700;
        margin-bottom: 0.6em;
    }}
    h1 {{ font-size: 2.6em; letter-spacing: -0.5px; }}
    h2 {{ font-size: 2.0em; }}
    h3 {{ font-size: 1.6em; }}

    p, .stMarkdown p {{
        font-size: 1.0em;
        line-height: 1.7;
        margin-bottom: 1em;
        /* Remover a cor fixa aqui para que o Streamlit defina a cor do texto padrão */
        /* color: {text_color}; REMOVIDO */
    }}
    
    /* ... o restante do seu CSS continua aqui ... */

    </style>
    """,
    unsafe_allow_html=True
)

# --- Geração do Link para WhatsApp ---
whatsapp_number = "5599981042926"
whatsapp_number_display = "(99) 98104-2926"
whatsapp_msg = "Olá! Vim pelo E1A Data Analytics e gostaria de saber mais."
whatsapp_url = f"https://wa.me/{whatsapp_number}?text={urllib.parse.quote(whatsapp_msg)}"
# --- Cabeçalho com Logo, Título e Gráfico ---
col_logo, col_title, col_chart = st.columns([1, 3, 3], gap="medium")

with col_logo:
    try:
        st.image("logo.jpg", width=120)
    except FileNotFoundError:
        st.warning("Logo não encontrada.")
        st.image(f"https://placehold.co/100x100/{primary_color.replace('#','')}/{background_color.replace('#','')}?text=E1A", width=100)

with col_title:
    st.title("E1A Data Analytics")
    st.markdown("##### Transformando dados em **insights estratégicos**.")

# --- Nova Terceira Coluna para o Gráfico Animado HTML/SVG ---
with col_chart:
    st.markdown("###### Performance Ilustrativa")

    # Cores para as linhas do gráfico
    cor_linha_constante = secondary_color  # Cinza Chumbo
    cor_linha_crescente = accent_color     # Ouro Metálico Suave

    html_chart = f"""
        <div style="width: 100%; height: 100px; border: 1px solid #dddddd33; border-radius: 5px; overflow: hidden;">
        <svg width="100%" height="100%" viewBox="0 0 300 100" preserveAspectRatio="xMidYMid meet">
            <line x1="10" y1="30" x2="290" y2="30" stroke="{cor_linha_constante}" stroke-width="2"/>
            <polyline id="dynamic-growing-line" points="10,70" stroke="{cor_linha_crescente}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        </div>
        <script>
        (function() {{
        const growingLineElement = document.getElementById('dynamic-growing-line');
        const svgViewBoxWidth = 300;
        const startX = 10;
        const startY = 70;
        let currentX = startX;
        let currentY = startY;

        let growingPoints = [[startX, startY]];
        let deltaY = -0.15;
        let waveCounter = 0;
        const waveChangeInterval = 50;

        function animateChart() {{
            currentX += 1.0;
            currentY += deltaY;

            waveCounter += 1;
            if (waveCounter >= waveChangeInterval) {{
            deltaY *= -1;
            waveCounter = 0;
            }}

            if (currentX > svgViewBoxWidth - 10 || currentY < 30 || currentY > 80) {{
            currentX = startX;
            currentY = startY;
            growingPoints = [[startX, startY]];
            deltaY = -0.15;
            waveCounter = 0;
            }} else {{
            growingPoints.push([currentX, currentY]);
            }}

            growingLineElement.setAttribute('points', growingPoints.map(p => p.join(',')).join(' '));
            requestAnimationFrame(animateChart);
        }}

        requestAnimationFrame(animateChart);
        }})();
        </script>
        """

    components.html(html_chart, height=120) # Ajuste a altura conforme necessário

st.markdown("---")

# --- Seção "Sobre Nós" e "Nossos Pilares" ---
# (Mantida a estrutura de 3 colunas que você já tinha corrigido)
col_pilares_header, col_pilares_texto, col_pilares_img = st.columns([2, 3, 2], gap="large")

with col_pilares_header:
    st.header("Quem Somos")
    st.markdown(
        """
        <ul>
            <li>🚀 <strong>Na E1A Data Analytics:</strong> empresa focada em desvendar o potencial dos dados.</li>
            <li>🚀 <strong>Nossa Missão:</strong> é capacitar empresas com clareza e inteligência analítica,
            transformando informações complexas em decisões estratégicas que impulsionam crescimento e inovação do seu negócio.</li>
        </ul>
        """, unsafe_allow_html=True
    )

with col_pilares_texto:
    st.header("Nossos Pilares")
    st.markdown(
        """
        <ul>
            <li>📊 <strong>Business Intelligence (BI):</strong> Painéis interativos e relatórios dinâmicos para uma visão 360º do seu desempenho e identificação de tendências.</li>
            <li>🔍 <strong>Análise de Dados Avançada:</strong> Descoberta de padrões, correlações e anomalias para otimização e mitigação de riscos.</li>
            <li>🔮 <strong>Ciência de Dados e Modelagem Preditiva:</strong> Algoritmos de machine learning para prever cenários, personalizar experiências e automatizar processos.</li>
            <li>🤖 <strong>Automatização de Processos:</strong> Criamos soluções inteligentes de automação de processos que otimizam seus fluxos de trabalho.</li>
        </ul>
        """, unsafe_allow_html=True
    )

with col_pilares_img:
    st.header("Fale Conosco!")
    st.markdown(f"""
        <div style="color:{text_color}; font-family: Inter, sans-serif; font-size: 1.05em; line-height: 1.6;">
            <strong>Elielson Cardoso</strong><br>
            <em>Cientista de Dados e Fundador</em><br><br>

            Pronto para dar o próximo passo na jornada com dados?<br>
            Entre em contato para uma consultoria personalizada.<br><br>

            📞 <strong>WhatsApp:</strong> <a href="{whatsapp_url}" target="_blank" style="color:{primary_color}; font-weight:600; font-size:1.1em;">{whatsapp_number_display}</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown(
    f"<p style='text-align:center; font-size: 1.05em; color: {primary_color}; margin-top:1rem; margin-bottom:1rem;'><strong>Seu sucesso impulsionado por dados.</strong></p>",
    unsafe_allow_html=True
)

# --- Rodapé ---
current_year = datetime.date.today().year
st.markdown(
    f"""
    <div class="footer">
        <p>&copy; {current_year} E1A Data Analytics. Todos os direitos reservados.</p>
        <p>Consultoria Especializada em Dados</p>
    </div>
    """,
    unsafe_allow_html=True
)