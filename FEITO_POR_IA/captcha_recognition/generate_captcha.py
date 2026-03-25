"""
Gerador de CAPTCHA para treinamento
Cria imagens de CAPTCHA com labels para treinar o modelo
"""

import random
import string
import cv2
import numpy as np
import os

class CaptchaGenerator:
    def __init__(self, width=200, height=50):
        self.width = width
        self.height = height
        self.characters = string.ascii_letters + string.digits
    
    def generate_captcha_text(self, length=5):
        """Gera um texto CAPTCHA aleatório"""
        return ''.join(random.choices(self.characters, k=length))
    
    def add_noise(self, image, noise_level=0.1):
        """Adiciona ruído à imagem"""
        noise = np.random.normal(0, noise_level * 255, image.shape)
        image = np.clip(image + noise, 0, 255).astype(np.uint8)
        return image
    
    def add_distortion(self, image):
        """Adiciona distorção à imagem"""
        # Aplica blur aleatório
        kernel_size = random.choice([1, 3, 5])
        if kernel_size > 1:
            image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        
        return image
    
    def generate(self, text=None):
        """Gera uma imagem CAPTCHA"""
        if text is None:
            text = self.generate_captcha_text()
        
        # Cria uma imagem branca
        image = np.ones((self.height, self.width, 3), dtype=np.uint8) * 255
        
        # Adiciona texto
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1.0
        font_color = (0, 0, 0)  # Preto
        font_thickness = 2
        
        # Posiciona o texto no centro
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        text_x = (self.width - text_size[0]) // 2
        text_y = (self.height + text_size[1]) // 2
        
        cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness)
        
        # Converte para grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Adiciona ruído
        image = self.add_noise(image, noise_level=0.05)
        
        # Adiciona distorção
        image = self.add_distortion(image)
        
        # Adiciona linhas aleatórias (efeito CAPTCHA típico)
        for _ in range(random.randint(2, 5)):
            pt1 = (random.randint(0, self.width), random.randint(0, self.height))
            pt2 = (random.randint(0, self.width), random.randint(0, self.height))
            color = random.randint(0, 150)
            cv2.line(image, pt1, pt2, color, random.randint(1, 2))
        
        return image, text
    
    def generate_dataset(self, output_dir, num_images=1000):
        """Gera um dataset de CAPTCHAs para treinamento"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        images_dir = os.path.join(output_dir, 'images')
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
        
        labels_file = os.path.join(output_dir, 'labels.txt')
        
        with open(labels_file, 'w') as f:
            for i in range(num_images):
                image, text = self.generate()
                
                # Salva a imagem
                img_name = f'captcha_{i:05d}.png'
                img_path = os.path.join(images_dir, img_name)
                cv2.imwrite(img_path, image)
                
                # Salva o label
                f.write(f'{img_name},{text}\n')
                
                if (i + 1) % 100 == 0:
                    print(f"Geradas {i + 1}/{num_images} imagens")
        
        print(f"\nDataset gerado em: {output_dir}")
        print(f"Total de imagens: {num_images}")


if __name__ == "__main__":
    generator = CaptchaGenerator()
    
    # Gera dataset de treinamento
    output_dir = './data/training_data'
    generator.generate_dataset(output_dir, num_images=500)
    
    # Exemplo: gera e salva uma única imagem
    image, text = generator.generate()
    cv2.imwrite('./data/sample_captcha.png', image)
    print(f"\nExemplo CAPTCHA gerado: {text}")
    print("Salvo em: ./data/sample_captcha.png")
