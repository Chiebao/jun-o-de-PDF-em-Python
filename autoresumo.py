from PyPDF2 import PdfMerger
import os 

#Para mesclar o PDF
merger = PdfMerger()

#Listamento de arquivos para mesclar
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if arquivo.lower().endswith(".pdf"): #diz que se acabar em pdf é para puxar
        merger.append(f"arquivos/{arquivo}")
        
merger.write("PDFfinal.pdf")
merger.close()