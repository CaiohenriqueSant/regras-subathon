import streamlit as st
import streamlit.components.v1 as components
import random
import streamlit_analytics
from PIL import Image
import base64

# Função para converter imagem local para HTML
def get_image_base64(path: str) -> str:
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

# Configuração da Página
st.set_page_config(page_title="Subathon do Seraffa", page_icon="🎮", layout="wide")

# CSS para Centralização Total e Estilo
st.markdown("""
    <style>
    .stMainBlockContainer, [data-testid="stVerticalBlock"], [data-testid="column"] {
        text-align: center !important;
        display: flex;
        flex-direction: column;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Cards coloridos para Grupos (cores trocadas conforme pedido) */
    .group-1-card {
        background: linear-gradient(135deg, #1c83e1 0%, #0a5cb0 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 10px 0;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        border-left: 6px solid #0a4d8c;
        color: white;
    }

    .group-2-card {
        background: linear-gradient(135deg, #ff8c42 0%, #e67329 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 10px 0;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        border-left: 6px solid #d65c1a;
        color: white;
    }

    .group-3-card {
        background: linear-gradient(135deg, #ff3b3b 0%, #a60000 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 10px 0;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 10px 24px rgba(0,0,0,0.25);
        border-left: 6px solid #800000;
        color: white;
    }

    .bits-card-new {
        background: linear-gradient(135deg, #9c27b0 0%, #7b1fa2 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 10px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        border-left: 6px solid #6a1b9a;
        color: white;
    }

    .pix-card-new {
        background: linear-gradient(135deg, #4caf50 0%, #388e3c 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 10px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        border-left: 6px solid #2e7d32;
        color: white;
    }

    .group-header {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin-bottom: 15px;
    }

    .group-title {
        margin: 0;
        font-size: 1.6rem;
        font-weight: bold;
    }

    .group-1-card .group-title { color: white; }
    .group-2-card .group-title { color: white; }
    .group-3-card .group-title { color: white; }

    .group-time {
        font-size: 1.9rem;
        font-weight: bold;
        margin: 10px 0;
    }

    .group-1-card .group-time { color: #ffde59; }
    .group-2-card .group-time { color: #ffde59; }
    .group-3-card .group-time { color: #ffde59; }

    .group-description {
        font-size: 1.1rem;
        margin: 0;
    }

    .group-1-card .group-description { color: rgba(255,255,255,0.9); }
    .group-2-card .group-description { color: rgba(255,255,255,0.9); }
    .group-3-card .group-description { color: rgba(255,255,255,0.9); }

    .card-title {
        font-size: 1.8rem;
        margin: 0;
        color: white;
        font-weight: bold;
    }

    .card-time {
        font-size: 1.9rem;
        font-weight: bold;
        margin: 15px 0;
        color: #ffde59;
    }

    .card-description {
        font-size: 1.1rem;
        color: rgba(255,255,255,0.9);
    }

    /* Seção da Roleta (CSS externo não controla o iframe do components.html) */
    .roulette-main-container {
        background: linear-gradient(135deg, #fff4b0 0%, #ffe066 100%);
        padding: 35px;
        border-radius: 20px;
        margin: 30px 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }

    .roulette-title {
        color: white;
        text-align: center;
        margin-bottom: 10px;
        font-size: 2.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
    }

    .roulette-subtitle {
        color: rgba(255,255,255,0.9);
        text-align: center;
        margin-bottom: 40px;
        font-size: 1.3rem;
    }

    .roulette-section-blue {
        background: rgba(255,255,255,0.2);
        padding: 25px;
        border-radius: 12px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        border-left: 6px solid #1c83e1;
    }

    .roulette-section-green {
        background: rgba(255,255,255,0.2);
        padding: 25px;
        border-radius: 12px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        border-left: 6px solid #4caf50;
    }

    .roulette-section h3 {
        margin-bottom: 20px;
        font-size: 1.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .roulette-section-blue h3 { color: #a3d5ff; }
    .roulette-section-green h3 { color: #a5d6a7; }

    .roulette-section ul {
        text-align: left;
        color: white;
        font-size: 1.2rem;
        line-height: 1.8;
        padding-left: 20px;
    }

    .roulette-section ul li { margin-bottom: 10px; }

    /* Seção de Dobrar Pontos */
    .bonus-container {
        background: linear-gradient(135deg, #ff6b6b 0%, #ffde59 100%);
        padding: 35px;
        border-radius: 20px;
        margin: 30px 0;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }

    .bonus-title {
        color: #333;
        font-size: 2rem;
        margin-bottom: 15px;
        font-weight: bold;
    }

    .bonus-text {
        color: #333;
        font-size: 1.4rem;
        font-weight: bold;
    }

    /* Outras seções */
    .metas-container {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }

    .jogos-container {
        background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
        padding: 25px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    .descanso-container {
        background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
        padding: 25px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    /* Agradecimento final */
    .thanks-container {
        background: linear-gradient(135deg, #1c83e1 0%, #0a5cb0 100%);
        padding: 30px;
        border-radius: 15px;
        margin: 30px 0;
        text-align: center;
        color: white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }

    .thanks-text {
        font-size: 1.4rem;
        font-weight: bold;
    }

    div[data-testid="stNotificationContent"] {
        text-align: center !important;
        width: 100%;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Ajustes de espaçamento */
    .spacer { margin: 15px 0; }

    /* Overlay estilo dashboard (aplica automaticamente nos textos principais) */
    .group-time, .group-description, .card-time, .card-description {
        background: rgba(0,0,0,0.22);
        padding: 10px 14px;
        border-radius: 12px;
        backdrop-filter: blur(8px);
        display: inline-block;
        box-shadow: 0 8px 18px rgba(0,0,0,0.16);
    }

    .metas-container h3,
    .metas-container p,
    .jogos-container h3,
    .jogos-container div,
    .descanso-container h3,
    .descanso-container div,
    .bonus-container h3,
    .bonus-container p,
    .thanks-container p {
        background: rgba(0,0,0,0.18);
        padding: 10px 14px;
        border-radius: 12px;
        display: inline-block;
        backdrop-filter: blur(8px);
        box-shadow: 0 8px 18px rgba(0,0,0,0.14);
    }
    </style>
    """, unsafe_allow_html=True)

with streamlit_analytics.track():
    st.markdown("<h1 style='text-align: center;'>🎮 Nosso Primeiro Subathon!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>\"Salve família, bem-vindos às regras do nosso primeiro Subathon!\"</h3>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h2 style='text-align: center;'>⏳ Quanto tempo vamos adicionar?</h2>", unsafe_allow_html=True)

    col_g1, col_g2, col_g3 = st.columns(3)

    # Carregando as imagens (SUBs) + ícone de BITS
    try:
        img1 = get_image_base64("SUB_g_1.png")
        img2 = get_image_base64("SUB_g_2.png")
        img3 = get_image_base64("SUB_g_3.png")
        bits_img = get_image_base64("BITS.png")
    except Exception:
        st.error("Erro ao carregar imagens: Certifique-se que os arquivos .png estão na mesma pasta que o Regras.py")
        img1 = img2 = img3 = bits_img = ""

    with col_g1:
        st.markdown(f"""
        <div class="group-1-card">
            <div class="group-header">
                <img src='data:image/png;base64,{img1}' width='35' height='35'>
                <h3 class="group-title">GRUPO 1</h3>
            </div>
            <div class="group-time">+30 MINUTOS</div>
            <p class="group-description">SUB ou gift SUB!</p>
        </div>
        """, unsafe_allow_html=True)

    with col_g2:
        st.markdown(f"""
        <div class="group-2-card">
            <div class="group-header">
                <img src='data:image/png;base64,{img2}' width='35' height='35'>
                <h3 class="group-title">GRUPO 2</h3>
            </div>
            <div class="group-time">+45 MINUTOS</div>
            <p class="group-description">Sub T2 (R$ 16,00)</p>
        </div>
        """, unsafe_allow_html=True)

    with col_g3:
        st.markdown(f"""
        <div class="group-3-card">
            <div class="group-header">
                <img src='data:image/png;base64,{img3}' width='35' height='35'>
                <h3 class="group-title">GRUPO 3</h3>
            </div>
            <div class="group-time">+120 MINUTOS</div>
            <p class="group-description">Sub T3 (R$ 40,00)</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    col_bits, col_pix = st.columns(2)

    with col_bits:
        st.markdown(f"""
        <div class="bits-card-new">
            <div class="group-header">
                <img src='data:image/png;base64,{bits_img}' width='35' height='35'>
                <h3 class="card-title">BITS</h3>
            </div>
            <div class="card-time">+45 MINUTOS</div>
            <p class="card-description">A cada 100 bits!</p>
        </div>
        """, unsafe_allow_html=True)

    with col_pix:
        st.markdown("""
        <div class="pix-card-new">
            <div class="card-title">💸 LIVEPIX</div>
            <div class="card-time">+30 MINUTOS</div>
            <p class="card-description">A cada 10 R$ no livepix!</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    # Seção de Metas
    st.markdown("""
    <div class="metas-container">
        <h3 style='text-align: center; font-size: 1.8rem; margin-bottom: 15px;'>🚀 Bônus de Metas Adicionais</h3>
        <p style='text-align: center; font-size: 1.2rem; margin-bottom: 25px;'>A cada meta batida abaixo, adicionamos <b>+1 HORA</b> ao timer!<br>As metas são progressivas durante a live.</p>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px;">
            <div style="text-align: center;">
                <div style="font-size: 1.5rem; margin-bottom: 5px;">✅</div>
                <div style="font-size: 1.2rem; font-weight: bold;">5 SUBS</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5rem; margin-bottom: 5px;">✅</div>
                <div style="font-size: 1.2rem; font-weight: bold;">300 BITS</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5rem; margin-bottom: 5px;">✅</div>
                <div style="font-size: 1.2rem; font-weight: bold;">R$ 30,00 Pix</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    # Seção Jogos e Descanso
    col_jogos, col_descanso = st.columns(2)

    with col_jogos:
        st.markdown("""
        <div class="jogos-container">
            <h3 style='text-align: center; font-size: 1.6rem; margin-bottom: 20px;'>🕹️ QUER ESCOLHER O JOGO?</h3>
            <div style='text-align: center; font-size: 1.2rem; margin-bottom: 15px;'>Você poderá escolher o próximo jogo por:</div>
            <div style='text-align: center; font-size: 1.3rem; font-weight: bold; margin-bottom: 15px;'>
                <div>300 Bits ou R$ 30,00</div>
                <div>1 SUB GRUPO 3</div>
            </div>
            <div style='text-align: center; font-style: italic;'>Jogaremos enquanto estiver maneiro!</div>
        </div>
        """, unsafe_allow_html=True)

    with col_descanso:
        st.markdown("""
        <div class="descanso-container">
            <h3 style='text-align: center; font-size: 1.6rem; margin-bottom: 20px;'>💤 SOBRE O DESCANSO</h3>
            <div style='text-align: center; font-size: 1.2rem;'>
                As primeiras 24 horas, tentarei ficar acordado firme e forte.<br>
                Se eu dormir, o timer pausa e a live continua ON.<br>
                Voltamos com o timer quando eu acordar!
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# ================== ROLETA (CORRIGIDA + ZOOM + LEGÍVEL) ==================

roleta_img_base64 = get_image_base64("Roleta.png")

if roleta_img_base64:
    img_tag = f"""
    <img id="roletaImg"
         src="data:image/png;base64,{roleta_img_base64}"
         style="width:100%;max-width:400px;border-radius:12px;cursor:zoom-in;
                box-shadow:0 12px 30px rgba(0,0,0,0.25);">
    """
else:
    img_tag = "<div style='color:white;'>Imagem não encontrada</div>"

components.html(
f"""
<style>
  :root {{
    --bg1: #ffcf4d;
    --bg2: #ffb300;

    /* painéis internos com contraste (menos “lavado”) */
    --panel: rgba(0,0,0,0.32);
    --panelBorder: rgba(255,255,255,0.75);

    --white: #ffffff;
  }}

  body {{
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }}

  .roulette-main-container {{
    background: linear-gradient(135deg, var(--bg1) 0%, var(--bg2) 100%);
    padding: 35px;
    border-radius: 20px;
    margin: 30px 0;
    box-shadow: 0 15px 35px rgba(0,0,0,0.30);
  }}

  .roulette-title {{
    color: var(--white);
    text-align: center;
    margin: 0 0 10px 0;
    font-size: 2.5rem;
    text-shadow: 0 4px 10px rgba(0,0,0,0.45);
    letter-spacing: 0.5px;
  }}

  .roulette-subtitle {{
    color: rgba(255,255,255,0.95);
    text-align: center;
    margin: 0 0 28px 0;
    font-size: 1.25rem;
    text-shadow: 0 2px 6px rgba(0,0,0,0.35);
  }}

  .roulette-section-blue,
  .roulette-section-green {{
    background: var(--panel);
    padding: 22px;
    border-radius: 14px;
    margin: 14px 0;
    border: 1px solid rgba(255,255,255,0.14);
    border-left: 6px solid var(--panelBorder);
    box-shadow: 0 10px 24px rgba(0,0,0,0.18);
    backdrop-filter: blur(8px);
  }}

  .roulette-section-blue h3,
  .roulette-section-green h3 {{
    color: var(--white);
    margin: 0 0 12px 0;
    font-size: 1.45rem;
    text-shadow: 0 2px 6px rgba(0,0,0,0.35);
  }}

  .roulette-section-blue ul,
  .roulette-section-green ul {{
    margin: 0;
    text-align: left;
    color: var(--white);
    font-size: 1.15rem;
    line-height: 1.75;
    padding-left: 22px;
    text-shadow: 0 2px 6px rgba(0,0,0,0.28);

    /* “dashboard” nos textos da roleta */
    background: rgba(0,0,0,0.22);
    padding: 14px 16px;
    border-radius: 12px;
  }}

  .roulette-section-blue li,
  .roulette-section-green li {{ margin-bottom: 10px; }}

  /* -------- MODAL DE ZOOM -------- */
  #roletaModal {{
    position: fixed;
    inset: 0;
    display: none;
    align-items: center;
    justify-content: center;
    background: rgba(0,0,0,0.78);
    z-index: 9999;
  }}

  #roletaModalContent {{
    position: relative;
    width: min(92vw, 1100px);
    height: min(92vh, 820px);
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  #roletaModal img {{
    max-width: 100%;
    max-height: 100%;
    border-radius: 14px;
    box-shadow: 0 18px 50px rgba(0,0,0,0.5);
    transform: scale(1);
    transform-origin: center;
  }}

  .zoomControls {{
    position: absolute;
    top: 14px;
    right: 14px;
    display: flex;
    gap: 10px;
  }}

  .zoomBtn {{
    border: 0;
    border-radius: 10px;
    padding: 10px 12px;
    font-weight: 800;
    cursor: pointer;
    color: #111;
    background: rgba(255,255,255,0.92);
    box-shadow: 0 10px 24px rgba(0,0,0,0.25);
  }}

  .closeHint {{
    position: absolute;
    bottom: 16px;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(255,255,255,0.9);
    font-size: 14px;
  }}
</style>

<div class="roulette-main-container">
  <h2 class="roulette-title">🎡 A Roleta das Prendas</h2>
  <p class="roulette-subtitle">Preparem-se para me ver usando acessórios embaraçosos!</p>

  <div style="display:flex;gap:30px;flex-wrap:wrap;align-items:flex-start;justify-content:center;">
    <div style="flex:1;min-width:300px;max-width:400px;">
      <div class="roulette-section-blue">
        <h3>⚫ 1 GIRO POR:</h3>
        <ul>
          <li><b>1 SUB</b> (Qualquer Nível)</li>
          <li><b>100 Bits</b></li>
          <li><b>R$ 10,00</b> no LivePix</li>
        </ul>
      </div>

      <div class="roulette-section-green">
        <h3>⚫ BÔNUS POR GRUPO:</h3>
        <ul>
          <li><b>GRUPO 2:</b> Ganha <b>2 ROLETADAS</b> ⚫ ⚫</li>
          <li><b>GRUPO 3:</b> Ganha <b>4 ROLETADAS</b> ⚫ ⚫ ⚫ ⚫</li>
        </ul>
      </div>
    </div>

    <div style="flex:1;min-width:300px;max-width:400px;display:flex;align-items:center;justify-content:center;">
      {img_tag}
    </div>
  </div>
</div>

<!-- Modal de zoom -->
<div id="roletaModal">
  <div id="roletaModalContent">
    <div class="zoomControls">
      <button class="zoomBtn" id="zoomOut">−</button>
      <button class="zoomBtn" id="zoomIn">+</button>
      <button class="zoomBtn" id="zoomReset">Reset</button>
    </div>
    <img id="roletaModalImg" src="" alt="Roleta ampliada">
    <div class="closeHint">Clique fora da imagem para fechar</div>
  </div>
</div>

<script>
  const img = document.getElementById('roletaImg');
  const modal = document.getElementById('roletaModal');
  const modalImg = document.getElementById('roletaModalImg');

  let scale = 1;

  function applyScale() {{
    modalImg.style.transform = `scale(${{scale}})`;
  }}

  if (img) {{
    img.addEventListener('click', () => {{
      modalImg.src = img.src;
      scale = 1;
      applyScale();
      modal.style.display = 'flex';
    }});
  }}

  modal.addEventListener('click', (e) => {{
    if (e.target === modal) {{
      modal.style.display = 'none';
    }}
  }});

  document.getElementById('zoomIn').addEventListener('click', (e) => {{
    e.stopPropagation();
    scale = Math.min(scale + 0.2, 3);
    applyScale();
  }});

  document.getElementById('zoomOut').addEventListener('click', (e) => {{
    e.stopPropagation();
    scale = Math.max(scale - 0.2, 0.6);
    applyScale();
  }});

  document.getElementById('zoomReset').addEventListener('click', (e) => {{
    e.stopPropagation();
    scale = 1;
    applyScale();
  }});
</script>
""", height=720, scrolling=False)

# Seção de Dobrar Pontos da Loja
st.markdown("""
    <div class="bonus-container">
        <h3 class="bonus-title">🎯 CHANCE DE DOBRAR SEUS PONTOS DA LOJA!</h3>
        <p class="bonus-text">Cada roleta pode te dar uma chance de dobrar seus pontos na nossa loja de recompensas!</p>
    </div>
    """, unsafe_allow_html=True)

# Agradecimento final
st.markdown("""
    <div class="thanks-container">
        <p class="thanks-text">Agradeço a companhia e a parceria de todos vocês ❤️</p>
    </div>
    """, unsafe_allow_html=True)
