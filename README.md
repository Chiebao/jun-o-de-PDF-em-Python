🗂️ Automação para Mesclar PDFs
Este projeto é uma ferramenta de automação desenvolvida em Python para mesclar múltiplos arquivos PDF em um único documento, de forma rápida, prática e segura.

A solução foi projetada para eliminar tarefas repetitivas e agilizar o fluxo de trabalho, garantindo eficiência e preservação da qualidade dos arquivos originais.

💡 Ideal para:

Unificar relatórios empresariais mensais ou anuais.

Agrupar contratos, propostas ou documentos jurídicos.

Organizar e consolidar apostilas, ebooks e materiais acadêmicos.

Preparar documentos para envio único, evitando múltiplos anexos.

✨ Diferenciais:

Automação total – basta indicar os arquivos e o script faz o resto.

Flexibilidade – funciona com qualquer PDF, independente do tamanho.

Segurança – preserva formatação, imagens, tabelas e fontes originais.

Simplicidade – interface via terminal, fácil de adaptar para interface gráfica.

🚀 Funcionalidades
📑 Mescla dois ou mais arquivos PDF em um único documento.

⚡ Execução rápida e simples, sem necessidade de softwares pesados.

🔒 Mantém a qualidade e a formatação original dos arquivos.

🖥️ Interface de execução via terminal (pode ser adaptada para interface gráfica).

📋 Requisitos
Python 3.8+

Bibliotecas:

PyPDF2 (manipulação de PDFs)

Instale as dependências com:

bash
Copiar
Editar
pip install PyPDF2
📦 Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/mesclar-pdf.git
Acesse a pasta do projeto:

bash
Copiar
Editar
cd mesclar-pdf
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
🛠️ Uso
Coloque os PDFs que deseja mesclar na pasta indicada no código ou no mesmo diretório do script.

Execute o script:

bash
Copiar
Editar
python mesclar_pdf.py
Informe a ordem dos arquivos (se necessário).

O arquivo final será gerado no diretório especificado.

📂 Exemplo de Código
python
Copiar
Editar
import PyPDF2

merger = PyPDF2.PdfMerger()

arquivos = ["arquivo1.pdf", "arquivo2.pdf", "arquivo3.pdf"]

for pdf in arquivos:
    merger.append(pdf)

merger.write("resultado_final.pdf")
merger.close()
📄 Licença
Este projeto está licenciado sob a MIT License – sinta-se livre para usar e modificar.
