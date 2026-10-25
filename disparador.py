import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURAÇÕES DO GMAIL ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "dicsondantas@gmail.com"
SENHA_APLICATIVO = "voge rmjz fjwk ilam"

# --- TÍTULO E CORPO DA MENSAGEM ---
ASSUNTO = "🚀 Seu site no topo do Google: Mais autoridade e vendas"

CORPO_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; background-color: #f4f6f9; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #1f2937; line-height: 1.6;">
    <div style="max-width: 600px; margin: 40px auto; background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);">
        
        <!-- HEADER / IMAGEM HOSPEDADA NO GITHUB -->
        <div style="background-color: #111827; text-align: center;">
            <a href="https://api.whatsapp.com/send?phone=5584998394928&text=Olá!+Gostaria+de+informações+sobre+a+estratégia+de+backlinks+para+melhorar+a+visibilidade+do+meu+site+no+Google." target="_blank">
                <img src="COLE_O_LINK_RAW_DO_GITHUB_AQUI" alt="Backlinks - Conecte seu site a novas oportunidades" style="width: 100%; height: auto; display: block; border-bottom: 3px solid #f59e0b;">
            </a>
        </div>

        <!-- CONTEÚDO PRINCIPAL -->
        <div style="padding: 40px 30px;">
            <h1 style="font-size: 22px; color: #111827; margin-top: 0; line-height: 1.3; font-weight: 700;">
                Quando alguém pesquisa no Google pelo seu produto ou serviço, sua empresa aparece?
            </h1>

            <p style="font-size: 15px; color: #4b5563; margin-bottom: 20px;">
                Ter um site profissional é apenas o primeiro passo. O verdadeiro segredo para dominar os resultados de busca e atrair clientes qualificados é a <strong>autoridade digital</strong>.
            </p>

            <!-- CAIXA DE DESTAQUE DE BENEFÍCIOS -->
            <div style="background-color: #f8fafc; border-left: 4px solid #2563eb; padding: 20px; border-radius: 0 8px 8px 0; margin: 25px 0;">
                <p style="margin: 0 0 10px 0; font-weight: bold; color: #1e3a8a; font-size: 15px;">O que o trabalho estratégico de Backlinks faz por você:</p>
                <ul style="margin: 0; padding-left: 20px; color: #374151; font-size: 14px;">
                    <li style="margin-bottom: 8px;"><strong>Mais Autoridade:</strong> Seu domínio ganha relevância perante os algoritmos do Google.</li>
                    <li style="margin-bottom: 8px;"><strong>Visibilidade Real:</strong> Posicione sua marca nas primeiras posições de busca.</li>
                    <li style="margin-bottom: 8px;"><strong>Tráfego Qualificado:</strong> Pessoas realmente interessadas chegando até o seu site.</li>
                    <li><strong>Crescimento de Longo Prazo:</strong> Uma base sólida e duradoura para o seu negócio.</li>
                </ul>
            </div>

            <p style="font-size: 15px; color: #4b5563;">
                Cada negócio possui características únicas. Vamos desenhar juntos a estratégia ideal para colocar a sua empresa em destaque.
            </p>

            <!-- BOTÃO DE CHAMADA PARA AÇÃO (CTA) -->
            <div style="text-align: center; margin: 35px 0 20px 0;">
                <a href="https://api.whatsapp.com/send?phone=5584998394928&text=Olá!+Gostaria+de+informações+sobre+a+estratégia+de+backlinks+para+melhorar+a+visibilidade+do+meu+site+no+Google." style="background: linear-gradient(135deg, #25d366, #1ebe5d); color: #ffffff; padding: 14px 32px; text-decoration: none; border-radius: 50px; font-weight: bold; font-size: 16px; display: inline-block; box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);">
                    💬 Falar no WhatsApp
                </a>
            </div>
        </div>

        <!-- RODAPÉ COM REDES SOCIAIS -->
        <div style="background-color: #f1f5f9; padding: 25px 20px; text-align: center; border-top: 1px solid #e2e8f0;">
            <p style="font-size: 13px; font-weight: bold; color: #64748b; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px;">
                Conecte-se com a nossa rede
            </p>
            <div style="margin-bottom: 15px;">
                <a href="https://www.instagram.com/dicson.backlinks/" target="_blank" style="margin: 0 8px; text-decoration: none; color: #E1306C; font-weight: bold; font-size: 13px;">Instagram</a> • 
                <a href="https://www.facebook.com/profile.php?id=100081290636710" target="_blank" style="margin: 0 8px; text-decoration: none; color: #1877F2; font-weight: bold; font-size: 13px;">Facebook</a> • 
                <a href="https://www.linkedin.com/in/dicson-dantas-26229823b/" target="_blank" style="margin: 0 8px; text-decoration: none; color: #0A66C2; font-weight: bold; font-size: 13px;">LinkedIn</a> • 
                <a href="https://api.whatsapp.com/send?phone=5584998394928&text=Olá!+Gostaria+de+informações+sobre+a+estratégia+de+backlinks." target="_blank" style="margin: 0 8px; text-decoration: none; color: #25d366; font-weight: bold; font-size: 13px;">WhatsApp</a>
            </div>
            <p style="font-size: 11px; color: #94a3b8; margin: 0;">
                © 2026 Dicson Backlinks. Todos os direitos reservados.
            </p>
        </div>

    </div>
</body>
</html>
"""

TAMANHO_LOTE = 180

def carregar_emails():
    try:
        with open("emails.txt", "r", encoding="utf-8-sig") as f:
            emails = []
            for linha in f:
                email_limpo = linha.replace("\xa0", "").strip()
                if email_limpo and "@" in email_limpo:
                    emails.append(email_limpo)
        return list(set(emails))
    except FileNotFoundError:
        print("Arquivo emails.txt não encontrado na pasta.")
        return []

def enviar_lote():
    emails = carregar_emails()
    if not emails:
        print("Nenhum e-mail para enviar.")
        return

    indice_atual = 0
    try:
        with open("progresso.txt", "r") as f:
            indice_atual = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        indice_atual = 0

    if indice_atual >= len(emails):
        print("A lista inteira de e-mails foi percorrida. Reiniciando o ciclo.")
        indice_atual = 0

    lote = emails[indice_atual : indice_atual + TAMANHO_LOTE]
    proximo_indice = indice_atual + len(lote)

    print(f"[{time.strftime('%d/%m/%Y %H:%M:%S')}] Iniciando lote: enviando {len(lote)} e-mails...", flush=True)

    try:
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_APLICATIVO)

        for i, destinatario in enumerate(lote, 1):
            try:
                # Agora usamos multipart normal, já que a imagem vai por link web (HTML)
                msg = MIMEMultipart()
                msg['From'] = EMAIL_REMETENTE
                msg['To'] = destinatario
                msg['Subject'] = ASSUNTO
                
                msg.attach(MIMEText(CORPO_HTML, 'html', 'utf-8'))

                servidor.sendmail(EMAIL_REMETENTE, destinatario, msg.as_string())
                print(f"[{i}/{len(lote)}] E-mail enviado para: {destinatario}")
            except Exception as e:
                print(f"Erro ao enviar para {destinatario}: {e}")

        servidor.quit()

        with open("progresso.txt", "w") as f:
            f.write(str(proximo_indice))
        print(f"Lote finalizado. Próximo índice salvo: {proximo_indice}")

    except Exception as e:
        print(f"Erro de conexão SMTP: {e}")

if __name__ == "__main__":
    enviar_lote()
