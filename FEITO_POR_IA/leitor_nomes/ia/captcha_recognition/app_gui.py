"""
Interface gráfica para reconhecimento de CAPTCHA
Permite testar o modelo com imagens
"""

import os
import sys
import cv2
import numpy as np
from main_v2 import CaptchaRecognizer
from tkinter import Tk, Label, Button, filedialog, messagebox, Frame
from PIL import Image, ImageTk
import threading


class CaptchaRecognitionApp:
    def __init__(self, root, model_path='./models/captcha_model.h5'):
        self.root = root
        self.root.title("🔒 CAPTCHA Recognition AI")
        self.root.geometry("900x700")
        self.root.configure(bg='#2b2b2b')
        
        # Carrega o modelo
        self.recognizer = CaptchaRecognizer(model_path)
        self.current_image_path = None
        self.current_image = None
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Cria os widgets da interface"""
        
        # Título
        title = Label(self.root, text="🔒 CAPTCHA Recognition AI", 
                     font=("Arial", 20, "bold"), bg='#2b2b2b', fg='#00ff00')
        title.pack(pady=10)
        
        # Frame para controles
        control_frame = Frame(self.root, bg='#2b2b2b')
        control_frame.pack(pady=10)
        
        # Botão para abrir imagem
        open_btn = Button(control_frame, text="📂 Abrir Imagem", 
                         command=self._open_image, 
                         bg='#0066cc', fg='white', font=("Arial", 11, "bold"),
                         padx=15, pady=8)
        open_btn.pack(side="left", padx=5)
        
        # Botão para reconhecer
        recognize_btn = Button(control_frame, text="🔍 Reconhecer", 
                              command=self._recognize, 
                              bg='#00cc00', fg='white', font=("Arial", 11, "bold"),
                              padx=15, pady=8)
        recognize_btn.pack(side="left", padx=5)
        
        # Botão para testar dataset
        test_btn = Button(control_frame, text="📊 Testar Dataset", 
                         command=self._test_dataset, 
                         bg='#ff6600', fg='white', font=("Arial", 11, "bold"),
                         padx=15, pady=8)
        test_btn.pack(side="left", padx=5)
        
        # Label para status
        self.status_label = Label(self.root, text="Aguardando ação...", 
                                 bg='#2b2b2b', fg='#ffff00', font=("Arial", 10))
        self.status_label.pack(pady=5)
        
        # Frame para exibir imagem
        image_frame = Frame(self.root, bg='#1a1a1a', relief="sunken", bd=2)
        image_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.image_label = Label(image_frame, bg='#1a1a1a')
        self.image_label.pack(fill="both", expand=True)
        
        # Frame para resultado
        result_frame = Frame(self.root, bg='#2b2b2b')
        result_frame.pack(pady=10, fill="x", padx=10)
        
        Label(result_frame, text="CAPTCHA Reconhecido:", 
              bg='#2b2b2b', fg='#00ff00', font=("Arial", 11, "bold")).pack(side="left")
        
        self.result_label = Label(result_frame, text="---", 
                                 bg='#2b2b2b', fg='#ffffff', 
                                 font=("Arial", 14, "bold"), width=30)
        self.result_label.pack(side="left", padx=10)
        
        # Frame para informações
        info_frame = Frame(self.root, bg='#1a1a1a', relief="sunken", bd=1)
        info_frame.pack(pady=10, padx=10, fill="x")
        
        self.info_label = Label(info_frame, 
                               text="📌 Instruções: 1) Abra uma imagem  2) Clique em Reconhecer  3) Veja o resultado",
                               bg='#1a1a1a', fg='#cccccc', font=("Arial", 9),
                               justify="left", wraplength=850)
        self.info_label.pack(padx=5, pady=5)
    
    def _open_image(self):
        """Abre um diálogo para selecionar uma imagem"""
        filetypes = (('PNG files', '*.png'), ('JPG files', '*.jpg'), ('All files', '*.*'))
        
        filename = filedialog.askopenfilename(
            title="Selecione uma imagem CAPTCHA",
            filetypes=filetypes,
            initialdir="./data"
        )
        
        if filename:
            self.current_image_path = filename
            self._display_image(filename)
            self.status_label.config(text=f"✅ Imagem carregada: {os.path.basename(filename)}")
            self.result_label.config(text="---")
    
    def _display_image(self, image_path):
        """Exibe a imagem na interface"""
        img = cv2.imread(image_path)
        
        if img is None:
            messagebox.showerror("Erro", "Não foi possível carregar a imagem")
            return
        
        # Redimensiona para caber na interface
        h, w = img.shape[:2]
        max_height = 400
        if h > max_height:
            ratio = max_height / h
            w = int(w * ratio)
            h = max_height
            img = cv2.resize(img, (w, h))
        
        # Converte BGR para RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Converte para PIL
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk
        self.current_image = img
    
    def _recognize(self):
        """Reconhece o CAPTCHA da imagem"""
        if self.current_image_path is None:
            messagebox.showwarning("Aviso", "Abra uma imagem primeiro!")
            return
        
        self.status_label.config(text="⏳ Reconhecendo...")
        self.root.update()
        
        try:
            resultado = self.recognizer.recognize(self.current_image_path)
            
            if resultado:
                self.result_label.config(text=resultado, fg='#00ff00')
                self.status_label.config(text="✅ Reconhecimento concluído com sucesso!")
            else:
                self.result_label.config(text="Erro", fg='#ff0000')
                self.status_label.config(text="❌ Erro ao reconhecer CAPTCHA")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao reconhecer: {str(e)}")
            self.status_label.config(text="❌ Erro durante o reconhecimento")
    
    def _test_dataset(self):
        """Testa o modelo com múltiplas imagens do dataset"""
        dataset_dir = './data/training_data/images'
        
        if not os.path.exists(dataset_dir):
            messagebox.showerror("Erro", f"Dataset não encontrado em {dataset_dir}")
            return
        
        # Lista imagens
        images = [f for f in os.listdir(dataset_dir) if f.endswith('.png')][:10]
        
        if not images:
            messagebox.showerror("Erro", "Nenhuma imagem encontrada no dataset")
            return
        
        self.status_label.config(text=f"⏳ Testando {len(images)} imagens...")
        self.root.update()
        
        # Testa em thread separada
        threading.Thread(target=self._test_batch, args=(dataset_dir, images)).start()
    
    def _test_batch(self, dataset_dir, images):
        """Testa um lote de imagens"""
        results = []
        
        for img_name in images:
            img_path = os.path.join(dataset_dir, img_name)
            try:
                resultado = self.recognizer.recognize(img_path)
                results.append(f"{img_name}: {resultado}")
            except Exception as e:
                results.append(f"{img_name}: Erro - {str(e)}")
        
        # Atualiza UI
        result_text = "\n".join(results)
        messagebox.showinfo("Resultados do Teste", 
                          f"Testes concluídos:\n\n{result_text}")
        
        self.status_label.config(text="✅ Testes concluídos!")


def main():
    root = Tk()
    app = CaptchaRecognitionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
