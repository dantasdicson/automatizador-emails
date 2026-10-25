import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURAÇÕES DO GMAIL ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "dicsondantas@gmail.com"      # O teu e-mail
SENHA_APLICATIVO = "voge rmjz fjwk ilam"  # Senha de App configurada

# --- TÍTULO E CORPO DA MENSAGEM (HTML ORIGINAL E CORRIGIDO) ---
ASSUNTO = "NOVIDADE !!! SEU SITE MERECE SER ENCONTRADO POR MAIS PESSOAS"

CORPO_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body style="font-family: Arial, sans-serif; color: #333333; line-height: 1.6;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        
        <!-- Imagem com Link para o WhatsApp -->
        <div style="text-align: center; margin-bottom: 20px;">
            <a href="https://api.whatsapp.com/send?phone=5584998394928&text=Olá!+Gostaria+de+informações+sobre+a+estratégia+de+backlinks+para+melhorar+a+visibilidade+do+meu+site+no+Google." target="_blank">
                <img src="https://ci3.googleusercontent.com/meips/ADKq_NbmKB2kiadhKdAykNAgBSrAQTD4gk5iYjZ4oE5d2JyvASG-_JblvHTH1BqCEGN3PwNw1mPHwdcOEDePJ0A53VGBZSCGeUrxd1Mv_6sgkB6l7jZiz8jZeIROVNKsaFCDdyykPjsTzbhnwDm4_y9cgqHqd-72RcJ3gvsn7KmY8w=s0-d-e1-ft#https://55by4ianysmo62fl6qpby79v6rphgl_h7n8onw6evuy.canva-cdn.email/57906d916adb14b149c68b357a184048.png" alt="Backlinks SEO" style="max-width: 100%; height: auto; border-radius: 8px;">
            </a>
        </div>

        <h2 style="color: #1a73e8;">Quando alguém pesquisa no Google por um produto ou serviço, sua empresa está entre as opções que aparecem nos resultados?</h2>

        <p>Ter um site é um passo importante para a presença digital de qualquer negócio. Mas você sabia que existem estratégias que podem ajudar a fortalecer a relevância desse site nos mecanismos de busca?</p>
        
        <p><strong>Uma delas é o trabalho com Backlinks.</strong></p>

        <h3>Mas o que isso significa na prática?</h3>
        <p>Imagine que outros sites publicam links direcionando os visitantes para o site da sua empresa. Esses links são chamados de backlinks e, quando vêm de páginas relevantes e confiáveis, podem contribuir para fortalecer a autoridade do seu site perante o Google.</p>

        <h3>Quais são os benefícios dessa estratégia?</h3>
        <ul>
            <li><strong>Fortalecimento da presença digital:</strong> sua empresa trabalha para conquistar mais espaço nos resultados de pesquisa.</li>
            <li><strong>Mais credibilidade:</strong> links de sites relevantes podem contribuir para a reputação do seu domínio.</li>
            <li><strong>Novas oportunidades de acesso:</strong> pessoas que visitam outros sites podem chegar até sua empresa por meio desses links.</li>
            <li><strong>Estratégia de longo prazo:</strong> os backlinks podem complementar outras ações de SEO para melhorar o desempenho do seu site.</li>
        </ul>

        <p>Buscamos oportunidades estratégicas para ajudar empresas a fortalecer sua presença na internet por meio de backlinks relevantes.</p>
        
        <p>Cada site tem suas próprias características e necessidades. Por isso, entender o seu negócio é o primeiro passo para identificar as oportunidades mais adequadas.</p>

        <p><strong>Quer saber como os backlinks podem contribuir para a presença digital da sua empresa?</strong></p>
        
        <p style="text-align: center; margin: 30px 0;">
            <a href="https://api.whatsapp.com/send?phone=5584998394928&text=Olá!+Gostaria+de+informações+sobre+a+estratégia+de+backlinks+para+melhorar+a+visibilidade+do+meu+site+no+Google." style="background-color: #25d366; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">Fale conosco no WhatsApp</a>
        </p>

        <hr style="border: none; border-top: 1px solid #eeeeee; margin: 20px 0;">
        <p style="font-size: 12px; color: #888888; text-align: center;">© 2026 Todos os direitos reservados.</p>
    </div>
</body>
</html>
"""

def enviar_teste():
    print(f"[{time.strftime('%d/%m/%Y %H:%M:%S')}] A iniciar teste de envio com a mensagem original...", flush=True)

    try:
        print("A conectar ao servidor SMTP do Gmail...", flush=True)
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
        servidor.starttls()
        
        print("A fazer login com a senha de aplicativo...", flush=True)
        servidor.login(EMAIL_REMETENTE, SENHA_APLICATIVO)

        print(f"A preparar e-mail HTML para: {EMAIL_REMETENTE}", flush=True)
        msg = MIMEMultipart()
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = EMAIL_REMETENTE
        msg['Subject'] = ASSUNTO
        
        msg.attach(MIMEText(CORPO_HTML, 'html', 'utf-8'))

        print("A enviar o e-mail de teste...", flush=True)
        servidor.sendmail(EMAIL_REMETENTE, EMAIL_REMETENTE, msg.as_string())
        
        servidor.quit()
        print(f"E-MAIL DE TESTE ENVIADO COM SUCESSO para {EMAIL_REMETENTE}!", flush=True)

    except Exception as e:
        print(f"ERRO NO TESTE: {e}", flush=True)

if __name__ == "__main__":
    enviar_teste()
