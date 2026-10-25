import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURAÇÕES DO GMAIL ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "dicsondantas@gmail.com"      # O teu e-mail
SENHA_APLICATIVO = "voge rmjz fjwk ilam"  # Senha de App configurada

# --- TÍTULO E CORPO DA MENSAGEM (HTML) ---
ASSUNTO = "TESTE DE DISPARO - BACKLINKS GLOBAL"

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

        <h2 style="color: #1a73e8;">Este é um e-mail de teste do seu robô de automação!</h2>

        <p>Se estás a ler esta mensagem, significa que a conexão com o servidor SMTP do Gmail e o envio de HTML através do GitHub Actions estão a funcionar perfeitamente.</p>
        
        <p><strong>Tudo pronto para disparar para a tua base de clientes!</strong></p>

        <hr style="border: none; border-top: 1px solid #eeeeee; margin: 20px 0;">
        <p style="font-size: 12px; color: #888888; text-align: center;">© 2026 Todos os direitos reservados.</p>
    </div>
</body>
</html>
"""

def enviar_teste():
    print(f"[{time.strftime('%d/%m/%Y %H:%M:%S')}] A iniciar teste de envio...", flush=True)

    try:
        print("A conectar ao servidor SMTP do Gmail...", flush=True)
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
        servidor.starttls()
        
        print("A fazer login com a senha de aplicativo...", flush=True)
        servidor.login(EMAIL_REMETENTE, SENHA_APLICATIVO)

        print(f"A preparar e-mail para: {EMAIL_REMETENTE}", flush=True)
        msg = MIMEMultipart()
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = EMAIL_REMETENTE
        msg['Subject'] = ASSUNTO
        
        msg.attach(MIMEText(CORPO_HTML, 'html', 'utf-8'))

        print("A enviar o e-mail...", flush=True)
        servidor.sendmail(EMAIL_REMETENTE, EMAIL_REMETENTE, msg.as_string())
        
        servidor.quit()
        print(f"E-MAIL DE TESTE ENVIADO COM SUCESSO para {EMAIL_REMETENTE}!", flush=True)

    except Exception as e:
        print(f"ERRO NO TESTE: {e}", flush=True)

if __name__ == "__main__":
    enviar_teste()
