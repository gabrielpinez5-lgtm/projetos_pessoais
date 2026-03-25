"""
CAPTCHA Recognition AI
Sistema de reconhecimento de CAPTCHA usando Deep Learning
"""

import numpy as np
import cv2
from tensorflow import keras
from tensorflow.keras import layers
import os
import string
from PIL import Image

# Configurações
IMG_WIDTH = 200
IMG_HEIGHT = 50
MAX_LENGTH = 5
CHARACTERS = string.ascii_letters + string.digits

class CaptchaRecognizer:
    def __init__(self, model_path=None):
        """Inicializa o reconhecedor de CAPTCHA"""
        self.img_width = IMG_WIDTH
        self.img_height = IMG_HEIGHT
        self.max_length = MAX_LENGTH
        self.characters = CHARACTERS
        self.char_to_num = {char: idx for idx, char in enumerate(self.characters)}
        self.num_to_char = {idx: char for idx, char in enumerate(self.characters)}
        
        if model_path and os.path.exists(model_path):
            self.model = keras.models.load_model(model_path)
        else:
            self.model = self.build_model()
    
    def build_model(self):
        """Constrói o modelo de rede neural"""
        input_img = keras.Input(shape=(self.img_height, self.img_width, 1), name='image')
        
        x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
        x = layers.MaxPooling2D((2, 2))(x)
        
        x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
        x = layers.MaxPooling2D((2, 2))(x)
        
        x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
        x = layers.MaxPooling2D((2, 2))(x)
        
        x = layers.Flatten()(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.Dropout(0.5)(x)
        
        # Saída: múltiplas posições, cada uma prediz um caractere
        output = layers.Dense(self.max_length * len(self.characters), activation='softmax')(x)
        output = layers.Reshape((self.max_length, len(self.characters)), name='output')(output)
        
        model = keras.Model(inputs=input_img, outputs=output)
        return model
    
    def preprocess_image(self, image_path):
        """Pré-processa a imagem para o modelo"""
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            print(f"Erro ao carregar a imagem: {image_path}")
            return None
        
        # Redimensiona para o tamanho esperado
        img = cv2.resize(img, (self.img_width, self.img_height))
        
        # Normaliza os pixels para 0-1
        img = img.astype('float32') / 255.0
        
        # Adiciona dimensão de canal
        img = np.expand_dims(img, axis=-1)
        
        return img
    
    def recognize(self, image_path):
        """Reconhece o CAPTCHA na imagem"""
        img = self.preprocess_image(image_path)
        
        if img is None:
            return None
        
        # Adiciona dimensão de batch
        img = np.expand_dims(img, axis=0)
        
        # Faz a predição
        prediction = self.model.predict(img, verbose=0)
        
        # Extrai o caractere de maior probabilidade em cada posição
        result = []
        for i in range(self.max_length):
            char_idx = np.argmax(prediction[0, i, :])
            result.append(self.num_to_char[char_idx])
        
        # Remove caracteres extras (padding)
        result_str = ''.join(result).replace(self.characters[0], '').strip()
        
        return result_str
    
    def train(self, train_images_dir, train_labels_file, epochs=10, batch_size=32):
        """Treina o modelo com imagens de CAPTCHA"""
        X_train = []
        y_train = []
        
        # Lê as labels
        with open(train_labels_file, 'r') as f:
            labels = f.readlines()
        
        for label_line in labels:
            img_name, captcha_text = label_line.strip().split(',')
            img_path = os.path.join(train_images_dir, img_name)
            
            img = self.preprocess_image(img_path)
            if img is not None:
                X_train.append(img)
                
                # Converte o texto para índices numéricos
                y_label = []
                for char in captcha_text:
                    if char in self.char_to_num:
                        y_label.append(self.char_to_num[char])
                    else:
                        y_label.append(0)  # Padding
                
                # Completa com padding se necessário
                while len(y_label) < self.max_length:
                    y_label.append(0)
                
                y_train.append(y_label[:self.max_length])
        
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        
        # Converte para one-hot encoding
        y_train_encoded = np.zeros((y_train.shape[0], self.max_length, len(self.characters)))
        for i in range(y_train.shape[0]):
            for j in range(self.max_length):
                y_train_encoded[i, j, y_train[i, j]] = 1
        
        # Compila o modelo
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        # Treina o modelo
        self.model.fit(
            X_train, y_train_encoded,
            epochs=epochs,
            batch_size=batch_size,
            verbose=1
        )
    
    def save_model(self, model_path):
        """Salva o modelo treinado"""
        self.model.save(model_path)
        print(f"Modelo salvo em: {model_path}")


if __name__ == "__main__":
    # Exemplo de uso
    recognizer = CaptchaRecognizer()
    
    # Para treinar, descomente e forneça os dados:
    # recognizer.train('data/train_images', 'data/train_labels.txt', epochs=20)
    # recognizer.save_model('models/captcha_model.h5')
    
    # Para reconhecer uma imagem
    # resultado = recognizer.recognize('path/to/captcha.png')
    # print(f"CAPTCHA reconhecido: {resultado}")
    
    print("CaptchaRecognizer carregado. Use os métodos train() ou recognize()")
