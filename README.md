# PDFtoMP3

## Descrição

O **PDFtoMP3** é uma aplicação simples que converte documentos PDF em arquivos de áudio no formato MP3, utilizando a tecnologia de síntese de fala (Text-to-Speech). Esse projeto facilita a transformação de qualquer documento em uma narração em áudio, permitindo que você ouça o conteúdo de um PDF em vez de lê-lo.

## Funcionalidades

- Converte arquivos PDF em arquivos de áudio MP3
- Escolha de idioma e voz para a síntese de fala
- Fácil de usar, com uma interface simples

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada
- **PyPDF2**: Biblioteca para manipulação de arquivos PDF
- **gTTS (Google Text-to-Speech)**: Para a conversão de texto em áudio

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/JrGirotto/PDFtoMP3.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd PDFtoMP3
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```bash
    python main.py caminho_para_o_seu_arquivo.pdf
    ```

   Exemplo:
    ```bash
    python main.py exemplo.pdf
    ```

5. O arquivo MP3 será gerado no mesmo diretório.

## Requisitos

- Python 3.x
- Dependências listadas no arquivo `requirements.txt`

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir _issues_ ou enviar _pull requests_.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
