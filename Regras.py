import streamlit as st
import streamlit.components.v1 as components
import streamlit_analytics
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

    /* CARDS BASE - MESMO FORMATO PARA TODOS */
    .card-base {
        padding: 15px; /* REDUZIDO DE 20px PARA 15px */
        border-radius: 15px;
        text-align: center;
        margin: 10px 0;
        min-height: 130px; /* REDUZIDO DE 160px PARA 130px */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        border-left: 5px solid;
        color: white;
    }

    /* Cards coloridos para Grupos */
    .group-1-card { background: linear-gradient(135deg, #1c83e1 0%, #0a5cb0 100%); border-left-color: #0a4d8c; }
    .group-2-card { background: linear-gradient(135deg, #ff8c42 0%, #e67329 100%); border-left-color: #d65c1a; }
    .group-3-card { background: linear-gradient(135deg, #ff3b3b 0%, #a60000 100%); border-left-color: #800000; box-shadow: 0 8px 20px rgba(0,0,0,0.2); }
    .bits-card-new { background: linear-gradient(135deg, #9c27b0 0%, #7b1fa2 100%); border-left-color: #6a1b9a; }
    .pix-card-new { background: linear-gradient(135deg, #4caf50 0%, #388e3c 100%); border-left-color: #2e7d32; }
    .metas-container { background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); border-left-color: #4a1c9e; min-height: auto !important; padding: 20px !important; }
    .jogos-container { background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%); border-left-color: #1b5e20; min-height: auto !important; padding: 20px !important; }
    .descanso-container { background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%); border-left-color: #e65100; min-height: auto !important; padding: 20px !important; }
    .bonus-container { background: linear-gradient(135deg, #ff6b6b 0%, #ffde59 100%); border-left-color: #ff5722; min-height: auto !important; padding: 20px !important; }
    .thanks-container { background: linear-gradient(135deg, #1c83e1 0%, #0a5cb0 100%); border-left-color: #0a4d8c; min-height: auto !important; padding: 20px !important; }

    .group-header {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin-bottom: 8px; /* REDUZIDO DE 12px PARA 8px */
    }

    .group-title {
        margin: 0;
        font-size: 1.3rem; /* REDUZIDO DE 1.4rem PARA 1.3rem */
        font-weight: bold;
    }

    .group-time {
        font-size: 1.5rem; /* REDUZIDO DE 1.6rem PARA 1.5rem */
        font-weight: bold;
        margin: 5px 0; /* REDUZIDO DE 8px PARA 5px */
        color: #ffde59;
    }

    .group-description {
        font-size: 1rem; /* REDUZIDO DE 1.1rem PARA 1rem */
        margin: 0;
        color: rgba(255,255,255,0.9);
        line-height: 1.3;
    }

    .card-title {
        font-size: 1.4rem; /* REDUZIDO DE 1.5rem PARA 1.4rem */
        margin: 0;
        color: white;
        font-weight: bold;
    }

    .card-time {
        font-size: 1.5rem; /* REDUZIDO DE 1.6rem PARA 1.5rem */
        font-weight: bold;
        margin: 8px 0; /* REDUZIDO DE 12px PARA 8px */
        color: #ffde59;
    }

    .card-description {
        font-size: 1rem; /* REDUZIDO DE 1.1rem PARA 1rem */
        color: rgba(255,255,255,0.9);
        line-height: 1.3;
        margin: 0;
    }

    /* Seção da Roleta - CINZA ELEGANTE */
    .roulette-main-container {
        background: linear-gradient(135deg, #424242 0%, #2c2c2c 100%);
        padding: 25px;
        border-radius: 18px;
        margin: 25px 0;
        box-shadow: 0 12px 30px rgba(0,0,0,0.2);
    }

    .roulette-title {
        color: white;
        text-align: center;
        margin-bottom: 8px;
        font-size: 2rem;
        font-weight: bold;
    }

    .roulette-subtitle {
        color: rgba(255,255,255,0.85);
        text-align: center;
        margin-bottom: 30px;
        font-size: 1.1rem;
    }

    .roulette-tab-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .roulette-tab {
        background: rgba(255, 255, 255, 0.1);
        padding: 15px; /* REDUZIDO DE 18px PARA 15px */
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        border-left: 5px solid;
        text-align: left;
        backdrop-filter: blur(10px);
        width: 100%;
        box-sizing: border-box;
    }

    .tab-blue { border-left-color: #1c83e1; }
    .tab-green { border-left-color: #4caf50; }

    .roulette-tab h3 {
        margin: 0 0 10px 0; /* REDUZIDO DE 12px PARA 10px */
        font-size: 1.2rem; /* REDUZIDO DE 1.3rem PARA 1.2rem */
        color: white;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .roulette-tab ul {
        margin: 0;
        color: rgba(255,255,255,0.9);
        font-size: 1rem; /* REDUZIDO DE 1.1rem PARA 1rem */
        line-height: 1.5;
        padding-left: 18px;
        width: 100%;
        box-sizing: border-box;
    }

    .roulette-tab ul li { 
        margin-bottom: 6px;
        color: rgba(255,255,255,0.85);
        word-wrap: break-word;
        overflow-wrap: break-word;
    }

    .roulette-tab ul li b { color: #ffde59; }

    div[data-testid="stNotificationContent"] { text-align: center !important; width: 100%; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Overlay estilo dashboard */
    .group-time, .group-description, .card-time, .card-description,
    .metas-text-content, .jogos-text-content, .descanso-text-content,
    .bonus-text-content, .thanks-text-content {
        background: rgba(0,0,0,0.22);
        padding: 6px 10px; /* REDUZIDO DE 8px 12px PARA 6px 10px */
        border-radius: 10px;
        backdrop-filter: blur(8px);
        display: inline-block;
        box-shadow: 0 6px 15px rgba(0,0,0,0.16);
        margin: 3px 0; /* REDUZIDO DE 4px PARA 3px */
    }

    /* Centralização de conteúdo */
    .centered-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
    }

    /* Para textos empilhados dentro dos cards */
    .stacked-text {
        display: flex;
        flex-direction: column;
        gap: 4px; /* REDUZIDO DE 6px PARA 4px */
        align-items: center;
        width: 100%;
    }
    
    /* Seção menor para metas */
    .metas-grid {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 15px; /* REDUZIDO DE 20px PARA 15px */
        margin-top: 10px;
    }
    
    .meta-item {
        text-align: center;
        min-width: 90px; /* REDUZIDO DE 100px PARA 90px */
    }
    
    /* Divisão mais fina */
    .stDivider {
        margin: 15px 0 !important; /* REDUZIDO DE 20px PARA 15px */
    }
    
    /* Ajustes específicos para cards menores */
    .bits-card-new .stacked-text,
    .pix-card-new .stacked-text {
        gap: 2px; /* ESPAÇAMENTO AINDA MENOR PARA CARDS PEQUENOS */
    }
    
    .bits-card-new .card-time,
    .pix-card-new .card-time {
        margin: 5px 0; /* MARGEM MENOR PARA CARDS PEQUENOS */
    }
    
    .bits-card-new .card-description,
    .pix-card-new .card-description {
        font-size: 0.95rem; /* FONTE UM POUCO MENOR PARA CARDS PEQUENOS */
        line-height: 1.2;
    }
    </style>
    """, unsafe_allow_html=True)

with streamlit_analytics.track():
    # TÍTULO PRINCIPAL
    st.markdown("<h1 style='text-align: center;'>🎮 NOSSO PRIMEIRÃO SUBATHON! 🤯</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size: 1.3rem;'>Salve família! 👋 Bem-vindos às regras do nosso primeiro Subathon! Vai ser épico, relaxa que eu explico tudinho! 😎</h3>", unsafe_allow_html=True)
    
    st.divider()
    
    # PRIMEIRA SEÇÃO: Quanto tempo vamos adicionar?
    st.markdown("<h2 style='text-align: center;'>⏳ Quanto tempo vamos adicionar?</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.1rem;'>Cada contribuição vai aumentando o timer, então bora encher essa live de tempo! 🚀</p>", unsafe_allow_html=True)

    # Grupos 1, 2, 3
    col_g1, col_g2, col_g3 = st.columns(3)

    # Carregando as imagens
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
        <div class="card-base group-1-card">
            <div class="group-header">
                <img src='data:image/png;base64,{img1}' width='25' height='25'> <!-- REDUZIDO DE 30 PARA 25 -->
                <h3 class="group-title">SUBS - GRUPO 1</h3>
            </div>
            <div class="group-time">+30 MINUTOS</div>
            <p class="group-description">1 SUB ou gift SUB, é só sucesso! 🎉</p>
        </div>
        """, unsafe_allow_html=True)

    with col_g2:
        st.markdown(f"""
        <div class="card-base group-2-card">
            <div class="group-header">
                <img src='data:image/png;base64,{img2}' width='25' height='25'> <!-- REDUZIDO DE 30 PARA 25 -->
                <h3 class="group-title">SUBS - GRUPO 2</h3>
            </div>
            <div class="group-time">+45 MINUTOS</div>
            <p class="group-description">Sub T2 (R$ 16,00) - Vale muito a pena!</p>
        </div>
        """, unsafe_allow_html=True)

    with col_g3:
        st.markdown(f"""
        <div class="card-base group-3-card">
            <div class="group-header">
                <img src='data:image/png;base64,{img3}' width='25' height='25'> <!-- REDUZIDO DE 30 PARA 25 -->
                <h3 class="group-title">SUBS - GRUPO 3</h3>
            </div>
            <div class="group-time">+120 MINUTOS</div>
            <p class="group-description">Sub T3 (R$ 40,00) - Isso aqui é elite pura! 🏆</p>
        </div>
        """, unsafe_allow_html=True)

    # BITS e LIVEPIX lado a lado
    col_bits, col_pix = st.columns(2)

    with col_bits:
        st.markdown(f"""
        <div class="card-base bits-card-new">
            <div class="centered-content stacked-text">
                <div class="group-header">
                    <img src='data:image/png;base64,{bits_img}' width='25' height='25'> <!-- REDUZIDO DE 30 PARA 25 -->
                    <h3 class="card-title">BITS</h3>
                </div>
                <div class="card-time">+45 MINUTOS</div>
                <p class="card-description">A cada 100 bitolas que mandarem! ✨</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_pix:
        st.markdown("""
        <div class="card-base pix-card-new">
            <div class="centered-content stacked-text">
                <div class="card-title">💸 LIVEPIX - PIX NA HORA!</div>
                <div class="card-time">+30 MINUTOS</div>
                <p class="card-description">A cada 10 R$ no livepix! Cai na conta e já soma tempo! 📈</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Seção de Metas
    st.markdown("""
    <div class="card-base metas-container">
        <div class="centered-content">
            <h3 style='font-size: 1.5rem; margin-bottom: 10px;'>🚀 BÔNUS DE METAS ADICIONAIS - AQUI É CUMULATIVO, FAMÍLIA!</h3>
            <p class="metas-text-content" style='font-size: 1.1rem; margin-bottom: 15px;'>A cada meta que a gente bater, vai ser <b>+20 MINUTOS EXTRA</b> no timer!🤩</p>
            <div class="metas-grid">
                <div class="meta-item">
                    <div style="font-size: 1.3rem; margin-bottom: 3px;">✅</div>
                    <div style="font-size: 1.1rem; font-weight: bold;">5 SUBS 💙</div>
                </div>
                <div class="meta-item">
                    <div style="font-size: 1.3rem; margin-bottom: 3px;">✅</div>
                    <div style="font-size: 1.1rem; font-weight: bold;">300 BITS 💎</div>
                </div>
                <div class="meta-item">
                    <div style="font-size: 1.3rem; margin-bottom: 3px;">✅</div>
                    <div style="font-size: 1.1rem; font-weight: bold;">R$ 30,00 Pix 🤑</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # DIVISÃO 1 (entre metas e jogos/descanso)
    st.divider()
    
    # SEGUNDA SEÇÃO: Jogos e Descanso
    st.markdown("<h2 style='text-align: center;'>🎮 INFORMAÇÕES EXTRAS!</h2>", unsafe_allow_html=True)
    
    col_jogos, col_descanso = st.columns(2)

    with col_jogos:
        st.markdown("""
        <div class="card-base jogos-container">
            <div class="centered-content stacked-text">
                <h3 style='font-size: 1.4rem; margin-bottom: 12px;'>🕹️ QUER MANDAR EU JOGAR O QUE VOCÊ QUISER? 🤔</h3>
                <p class="jogos-text-content" style='font-size: 1.1rem; margin-bottom: 10px;'>Pode escolher o próximo jogo por essa bagatela aí:</p>
                <div class="jogos-text-content" style='font-size: 1.2rem; font-weight: bold; margin-bottom: 10px;'>
                    <div>🎮 300 Bits <i>ou</i> R$ 30,00 no Pix</div>
                    <div>🔥 <b>OU 1 SUB DO GRUPO 3!</b> (por R$ 40,00 você já escolhe <i>E</i> adiciona 2 horas!)</div>
                </div>
                <div style='font-style: italic; margin-top: 6px; font-size: 1rem;'>Se eu não tiver o jogo, você tem que me mandar também, tá? Dependendo do valor, claro! 😉<br>E a gente joga enquanto estiver maneiro! Se cansar, partimos pra próxima gameplay ou papo furado! 🎯</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_descanso:
        st.markdown("""
        <div class="card-base descanso-container">
            <div class="centered-content stacked-text">
                <h3 style='font-size: 1.4rem; margin-bottom: 12px;'>💤 Como vou descansar? 🤔 😴</h3>
                <div class="descanso-text-content" style='font-size: 1.1rem;'>
                    Nas primeiras 24 horas, eu vou tentar estar firme e forte, acordado com vocês! ⚡<br><br>
                    <b>MAS</b> se depois disso eu estiver muito cansado, vou dar uma dormidinha rapidinho...<br><br>
                    A live continua ON, mas o timer do Subathon pausa! ⏸️<br><br>
                    Quando eu acordar e voltar pro PC, a gente continua com o timer de onde parou! 🔄
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # DIVISÃO 2 (entre jogos/descanso e roleta)
    st.divider()
    
    # TERCEIRA SEÇÃO: Roleta
    roleta_img_base64 = get_image_base64("Roleta.png")

    if roleta_img_base64:
        img_tag = f"""
        <img id="roletaImg"
             src="data:image/png;base64,{roleta_img_base64}"
             style="width:100%;max-width:350px;border-radius:10px;cursor:zoom-in;
                    box-shadow:0 10px 25px rgba(0,0,0,0.25);">
        """
    else:
        img_tag = "<div style='color:white;'>Imagem não encontrada</div>"

    components.html(
    f"""
    <style>
      body {{
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      }}

      .roulette-main-container {{
        background: linear-gradient(135deg, #424242 0%, #2c2c2c 100%);
        padding: 20px; /* REDUZIDO DE 25px PARA 20px */
        border-radius: 18px;
        margin: 20px 0; /* REDUZIDO DE 25px PARA 20px */
        box-shadow: 0 12px 30px rgba(0,0,0,0.2);
      }}

      .roulette-title {{
        color: white;
        text-align: center;
        margin: 0 0 6px 0; /* REDUZIDO DE 8px PARA 6px */
        font-size: 1.8rem; /* REDUZIDO DE 2rem PARA 1.8rem */
        font-weight: bold;
      }}

      .roulette-subtitle {{
        color: rgba(255,255,255,0.85);
        text-align: center;
        margin: 0 0 20px 0; /* REDUZIDO DE 25px PARA 20px */
        font-size: 1.1rem; /* REDUZIDO DE 1.2rem PARA 1.1rem */
      }}

      .roulette-tab-container {{
        display: flex;
        flex-direction: column;
        gap: 10px; /* REDUZIDO DE 12px PARA 10px */
      }}

      .roulette-tab {{
        background: rgba(255, 255, 255, 0.1);
        padding: 15px; /* REDUZIDO DE 18px PARA 15px */
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        border-left: 5px solid;
        text-align: left;
        backdrop-filter: blur(10px);
        width: 100%;
        box-sizing: border-box;
      }}

      .tab-blue {{ border-left-color: #1c83e1; }}
      .tab-green {{ border-left-color: #4caf50; }}

      .roulette-tab h3 {{
        margin: 0 0 10px 0; /* REDUZIDO DE 12px PARA 10px */
        font-size: 1.2rem; /* REDUZIDO DE 1.3rem PARA 1.2rem */
        color: white;
        display: flex;
        align-items: center;
        gap: 8px;
      }}

      .roulette-tab ul {{
        margin: 0;
        color: rgba(255,255,255,0.9);
        font-size: 1rem; /* REDUZIDO DE 1.1rem PARA 1rem */
        line-height: 1.5;
        padding-left: 18px;
        width: 100%;
        box-sizing: border-box;
      }}

      .roulette-tab ul li {{ 
        margin-bottom: 6px;
        color: rgba(255,255,255,0.85);
        word-wrap: break-word;
        overflow-wrap: break-word;
        padding-right: 10px;
      }}

      .roulette-tab ul li b {{
        color: #ffde59;
      }}

      /* -------- MODAL DE ZOOM -------- */
      #roletaModal {{
        position: fixed;
        inset: 0;
        display: none;
        align-items: center;
        justify-content: center;
        background: rgba(0,0,0,0.85);
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
        border-radius: 12px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
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
        font-size: 14px; /* REDUZIDO DE 15px PARA 14px */
      }}
    </style>

    <div class="roulette-main-container">
      <h2 class="roulette-title">🎡 A ROLETA - AQUI EU ME LASCO! 😂</h2>
      <p class="roulette-subtitle">Preparem-se pra me ver usando acessórios inusitados! Tem de tudo na roleta: desde prendas pra eu me lascar até pontos da nossa lojinha! 🎁✨</p>

      <div style="display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start;justify-content:center;"> <!-- REDUZIDO gap DE 25px PARA 20px -->
        <div style="flex:1;min-width:280px;max-width:400px;">
          <div class="roulette-tab-container">
            <div class="roulette-tab tab-blue">
              <h3>⭕ CADA GIRO VOCÊ GANHA POR:</h3>
              <ul>
                <li><b>1 SUB</b> - (qualquer nível, meu consagrado!) 💙</li>
                <li><b>100 Bits</b> - brilha que eu giro! 💎</li>
                <li><b>R$ 10,00</b> - No LivePix - caiu, girou! 💸</li>
              </ul>
            </div>

            <div class="roulette-tab tab-green">
              <h3>⭕ QUEM GASTOU MAIS TEM BÔNUS POR GRUPO! 🎰</h3>
              <ul>
                <li><b>GRUPO 2:</b> Ganha <b>2 ROLETADAS</b> 🎡 🎡 🚀</li>
                <li><b>GRUPO 3:</b> Ganha <b>4 ROLETADAS</b> 🎡 🎡 🎡 🎡 🚀</li>
              </ul>
            </div>
          </div>
        </div>

        <div style="flex:1;min-width:280px;max-width:350px;display:flex;align-items:center;justify-content:center;">
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
    """, height=580, scrolling=False)  # REDUZIDO DE 620 PARA 580

    # DIVISÃO 3 (entre roleta e seção de dobrar pontos)
    st.divider()
    
    # QUARTA SEÇÃO: Dobrar Pontos
    st.markdown("""
        <div class="card-base bonus-container">
            <div class="centered-content">
                <h3 class="bonus-text-content" style='font-size: 1.6rem; margin-bottom: 10px; font-weight: bold;'>🎯 ATENÇÃO: CHANCE DE DOBRAR SEUS PONTOS DA LOJA! 🤑</h3>
                <p class="bonus-text-content" style='font-size: 1.2rem; font-weight: bold;'>Isso mesmo que você leu! Cada roleta pode te dar uma chance de DOBRAR seus pontos na nossa lojinha de recompensas! É muita vantagem, mano! 🚀✨</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # DIVISÃO 4 (entre dobrar pontos e agradecimento)
    st.divider()
    
    # QUINTA SEÇÃO: Agradecimento final
    st.markdown("""
        <div class="card-base thanks-container">
            <p class="thanks-text-content" style='font-size: 1.4rem; font-weight: bold;'>Manooo, agradeço demais a companhia e a parceria de todos vocês! ❤️<br><br><i>Vamo que vamo, família! É NÓIS! 🤩</i></p>
        </div>
        """, unsafe_allow_html=True)
