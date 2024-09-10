import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def pdf_metni_cikart(pdf_yolu):
    metin = ''
    pdf_okuyucu = PyPDF2.PdfReader(open(pdf_yolu, 'rb'))

    for i in range(len(pdf_okuyucu.pages)):
        metin += pdf_okuyucu.pages[i].extract_text()
        #i = sayfa numarasi
    return metin

def metin_ses(metin, cikti_dosyasi):
    ses_cevirici = gTTS(text = metin, lang='tr')
    ses_cevirici.save(cikti_dosyasi)

def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(filetypes=[('PDF Sec', '*.pdf')])
    if dosya_yolu:
        pdf_metin = pdf_metni_cikart(dosya_yolu)
        metin_ses(pdf_metin,'Kaydet.mp3')
        os.system('start Kaydet.mp3')
        
    
app = tk.Tk()
app.title('Sesli Kitap Uygulamasi')
app.geometry('250x100')
button = tk.Button(app, text='PDF Sec', command=dosya_sec, padx=20, pady=20)

button.pack(pady=20)

app.mainloop()
