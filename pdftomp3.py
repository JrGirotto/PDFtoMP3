import PyPDF2
from gtts import gTTS
import time

# Função para extrair o texto do PDF
def extract_text_from_pdf(pdf_file):
    print("Iniciando a extração de texto do PDF...")
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    print("Extração de texto concluída.")
    return text

# Função para simular o andamento da conversão
def simulate_conversion_progress(duration):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        progress = min(elapsed_time / duration, 1)  # Garantir que não passe de 100%
        percent = int(progress * 100)
        print(f"\rConversão em andamento... {percent}% concluído", end="")
        time.sleep(1)  # Atualiza a cada segundo
        if progress >= 1:
            break
    print("\nConversão concluída.")

# Função para converter o texto em áudio MP3 com simulação de progresso
def text_to_speech(text, output_file):
    print("Iniciando a conversão para MP3...")
    
    # Estima uma duração para a conversão com base no número de caracteres
    estimated_duration = len(text) / 100  # Aproximadamente 50 caracteres por segundo

    # Simular a conversão com barra de progresso
    simulate_conversion_progress(estimated_duration)

    # Converte o texto em áudio de fato
    tts = gTTS(text=text, lang='pt')
    tts.save(output_file)
    print(f"Áudio salvo como {output_file}")

# Caminho do arquivo PDF de entrada e do MP3 de saída
pdf_file = 'exemplo.pdf'
mp3_file = pdf_file.replace('.pdf', '.mp3')  # Gera o nome do arquivo MP3 automaticamente

# Extração do texto e conversão para MP3
text = extract_text_from_pdf(pdf_file)
text_to_speech(text, mp3_file)
