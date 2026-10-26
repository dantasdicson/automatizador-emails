import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURAÇÕES DO GMAIL ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "dicsondantas@gmail.com"      # O seu e-mail
SENHA_APLICATIVO = "voge rmjz fjwk ilam"  # Senha de App configurada

# --- TÍTULO E CORPO DA MENSAGEM (COM A SUA IMAGEM CORRETA E REDES SOCIAIS) ---
ASSUNTO = "NOVIDADE !!! SEU SITE MERECE SER ENCONTRADO POR MAIS PESSOAS"

CORPO_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body style="font-family: 'Segoe UI', Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 0; color: #2d3748; line-height: 1.6;">
    <div style="max-width: 600px; margin: 30px auto; background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        
        <!-- Cabeçalho / Sua Imagem Personalizada (imagem.jpg) com Link para o WhatsApp -->
        <div style="text-align: center; background: #ffcc00; padding: 20px;">
                <img src="https://imgur.com/a/F9uEWPk" alt="Backlinks SEO" style="max-width: 100%; height: auto; border-radius: 8px; display: block; margin: 0 auto;">
            </a>
        </div>

        <!-- Conteúdo Principal -->
        <div style="padding: 40px 30px;">
            <h2 style="color: #1a365d; font-size: 22px; margin-top: 0; line-height: 1.3;">Quando alguém pesquisa no Google por um produto ou serviço, sua empresa está entre as opções que aparecem nos resultados?</h2>

            <p style="color: #4a5568; font-size: 15px;">Ter um site é um passo importante para a presença digital de qualquer negócio. Mas você sabia que existem estratégias que podem ajudar a fortalecer a relevância desse site nos mecanismos de busca?</p>
            
            <p style="color: #2d3748; font-size: 15px;"><strong>Uma delas é o trabalho estratégico com Backlinks.</strong></p>

            <div style="background: #f8fafc; border-left: 4px solid #3182ce; padding: 15px 20px; margin: 20px 0; border-radius: 0 8px 8px 0;">
                <h3 style="color: #2b6cb0; margin: 0 0 8px 0; font-size: 16px;">O que isso significa na prática?</h3>
                <p style="margin: 0; color: #4a5568; font-size: 14px;">Imagine que outros sites publicam links direcionando os visitantes para o seu domínio. Quando vêm de páginas relevantes, fortalecem a sua autoridade perante o Google.</p>
            </div>

            <h3 style="color: #1a365d; font-size: 18px; margin-top: 30px;">Principais Benefícios:</h3>
            <ul style="padding-left: 20px; color: #4a5568; font-size: 15px;">
                <li style="margin-bottom: 8px;"><strong>Fortalecimento digital:</strong> Mais espaço nos resultados de pesquisa.</li>
                <li style="margin-bottom: 8px;"><strong>Mais credibilidade:</strong> Reputação sólida para o seu domínio.</li>
                <li style="margin-bottom: 8px;"><strong>Novas oportunidades:</strong> Tráfego qualificado de outros portais.</li>
                <li style="margin-bottom: 8px;"><strong>Estratégia de longo prazo:</strong> SEO robusto e sustentável.</li>
            </ul>

            <p style="color: #4a5568; font-size: 15px; margin-top: 30px;">Cada site tem características e necessidades próprias. Vamos analisar o seu negócio para identificar as melhores oportunidades.</p>
            
            <!-- Botão de Ação Principal (WhatsApp) -->
            <div style="text-align: center; margin: 35px 0 20px 0;">
                <a href="https://api.whatsapp.com/send?phone=5584998394928&text=Olá!+Gostaria+de+informações+sobre+a+estratégia+de+backlinks+para+melhorar+a+visibilidade+do+meu+site+no+Google." style="background-color: #25d366; color: white; padding: 14px 28px; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 16px; display: inline-block; box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3);">Fale Conosco no WhatsApp</a>
            </div>
        </div>

        <!-- Rodapé Moderno com Ponteiros para as Redes Sociais -->
        <div style="background: #edf2f7; padding: 25px 20px; text-align: center; border-top: 1px solid #e2e8f0;">
            <p style="margin: 0 0 15px 0; font-size: 13px; color: #718096; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Acompanhe nossas redes oficiais</p>
            
            <div style="margin-bottom: 15px;">
                <a href="https://api.whatsapp.com/send?phone=5584998394928&text=Olá!+Gostaria+de+informações+sobre+a+estratégia+de+backlinks." target="_blank" style="display: inline-block; margin: 0 8px; color: #25d366; text-decoration: none; font-weight: bold; font-size: 14px;">WhatsApp</a> | 
                <a href="https://instagram.com/dicson.dts" target="_blank" style="display: inline-block; margin: 0 8px; color: #e1306c; text-decoration: none; font-weight: bold; font-size: 14px;">Instagram</a> | 
                <a href="https://linkedin.com" target="_blank" style="display: inline-block; margin: 0 8px; color: #0077b5; text-decoration: none; font-weight: bold; font-size: 14px;">LinkedIn</a> | 
                <a href="https://facebook.com" target="_blank" style="display: inline-block; margin: 0 8px; color: #1877f2; text-decoration: none; font-weight: bold; font-size: 14px;">Facebook</a>
            </div>

            <p style="font-size: 12px; color: #a0aec0; margin: 0;">© 2026 Backlinks Global. Todos os direitos reservados.</p>
        </div>
    </div>
</body>
</html>
"""

def enviar_teste():
    print(f"[{time.strftime('%d/%m/%Y %H:%M:%S')}] A iniciar teste com a imagem correta...", flush=True)

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
        print(f"E-MAIL ENVIADO COM SUCESSO para {EMAIL_REMETENTE}!", flush=True)

    except Exception as e:
        print(f"ERRO NO TESTE: {e}", flush=True)

if __name__ == "__main__":
    enviar_teste()
