"""
CAPTCHA Recognition AI (Versão simplificada com scikit-learn)
Sistema de reconhecimento de CAPTCHA usando Machine Learning
"""

import numpy as np
import cv2
import os
import string
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor

class CaptchaRecognizer:
    def __init__(self, model_path=None):
        """Inicializa o reconhecedor de CAPTCHA"""
        self.img_width = 200
        self.img_height = 50
        self.max_length = 5
        self.characters = string.ascii_letters + string.digits
        self.char_to_num = {char: idx for idx, char in enumerate(self.characters)}
        self.num_to_char = {idx: char for idx, char in enumerate(self.characters)}
        
        self.model = None
        
        if model_path and os.path.exists(model_path):
            self.load_model(model_path)
    
    def build_model(self):
        """Constrói o modelo de rede neural para múltiplos caracteres"""
        # Usa MultiOutputRegressor com RandomForest para prever múltiplos caracteres
        base_model = RandomForestRegressor(
            n_estimators=200,
            max_depth=30,
            random_state=42,
            n_jobs=-1,
            verbose=1
        )
        model = MultiOutputRegressor(base_model)
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
        
        return img
    
    def extract_features(self, image):
        """Extrai características da imagem"""
        # Flatten para vetor
        features = image.flatten()
        
        # Adiciona alguns recursos derivados
        edges = cv2.Canny(
            (image * 255).astype('uint8'), 50, 150
        )
        edges = edges.astype('float32') / 255.0
        
        features = np.concatenate([features, edges.flatten()])
        
        return features
    
    def recognize(self, image_path):
        """Reconhece TODOS os caracteres do CAPTCHA na imagem"""
        if self.model is None:
            print("Erro: Modelo não foi treinado. Treine primeiro com train()")
            return None
        
        img = self.preprocess_image(image_path)
        
        if img is None:
            return None
        
        features = self.extract_features(img)
        features = features.reshape(1, -1)
        
        # Predição - retorna múltiplos caracteres
        prediction = self.model.predict(features)
        
        # Converte índices para caracteres
        result = []
        
        # prediction[0] contém os índices dos caracteres em cada posição
        for pred_value in prediction[0]:
            idx = int(round(pred_value))
            
            # Valida o índice
            if 0 < idx < len(self.num_to_char):
                result.append(self.num_to_char[idx])
            elif idx == 0:
                # Padding, não adiciona
                pass
        
        result_str = ''.join(result).strip()
        return result_str if result_str else "Erro ao reconhecer"
    
    def train(self, train_images_dir, train_labels_file, epochs=10):
        """Treina o modelo com imagens de CAPTCHA (todos os caracteres)"""
        X_train = []
        y_train = []
        
        # Lê as labels
        with open(train_labels_file, 'r', encoding='utf-8') as f:
            labels = f.readlines()
        
        print(f"Carregando {len(labels)} imagens...")
        
        for idx, label_line in enumerate(labels):
            try:
                parts = label_line.strip().split(',')
                img_name = parts[0]
                captcha_text = parts[1] if len(parts) > 1 else ""
                
                img_path = os.path.join(train_images_dir, img_name)
                
                img = self.preprocess_image(img_path)
                if img is not None:
                    features = self.extract_features(img)
                    X_train.append(features)
                    
                    # Cria um label para CADA posição de caractere
                    y_label = []
                    for i in range(self.max_length):
                        if i < len(captcha_text):
                            char = captcha_text[i]
                            char_idx = self.char_to_num.get(char, 0)
                        else:
                            char_idx = 0  # Padding
                        y_label.append(char_idx)
                    
                    y_train.append(y_label)
                
                if (idx + 1) % 50 == 0:
                    print(f"Processadas {idx + 1}/{len(labels)} imagens")
            except Exception as e:
                print(f"Erro ao processar {label_line}: {e}")
        
        if not X_train:
            print("Erro: Nenhuma imagem foi carregada")
            return
        
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        
        print(f"\nTreinando modelo com {len(X_train)} amostras...")
        print(f"Formato de entrada: {X_train.shape}")
        print(f"Formato de saída: {y_train.shape}")
        
        # Cria e treina o modelo
        self.model = self.build_model()
        self.model.fit(X_train, y_train)
        
        print("✅ Treinamento concluído!")
        print(f"Modelo pronto para reconhecer até {self.max_length} caracteres")
    
    def save_model(self, model_path):
        """Salva o modelo treinado"""
        os.makedirs(os.path.dirname(model_path) or '.', exist_ok=True)
        
        with open(model_path, 'wb') as f:
            pickle.dump({
                'model': self.model,
                'char_to_num': self.char_to_num,
                'num_to_char': self.num_to_char,
                'characters': self.characters
            }, f)
        
        print(f"Modelo salvo em: {model_path}")
    
    def load_model(self, model_path):
        """Carrega um modelo treinado"""
        with open(model_path, 'rb') as f:
            data = pickle.load(f)
            self.model = data['model']
            self.char_to_num = data['char_to_num']
            self.num_to_char = data['num_to_char']
            self.characters = data['characters']
        
        print(f"Modelo carregado de: {model_path}")


if __name__ == "__main__":
    print("CaptchaRecognizer carregado. Use os métodos train() ou recognize()")
