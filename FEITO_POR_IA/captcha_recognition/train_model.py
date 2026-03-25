"""
Script para treinar o modelo de reconhecimento de CAPTCHA
"""

import os
import sys
from main_v2 import CaptchaRecognizer
from generate_captcha import CaptchaGenerator


def train_from_dataset(dataset_dir, output_model_path, epochs=20, batch_size=32):
    """Treina o modelo usando um dataset existente"""
    
    images_dir = os.path.join(dataset_dir, 'images')
    labels_file = os.path.join(dataset_dir, 'labels.txt')
    
    if not os.path.exists(images_dir):
        print(f"Erro: Diretório de imagens não encontrado: {images_dir}")
        return None
    
    if not os.path.exists(labels_file):
        print(f"Erro: Arquivo de labels não encontrado: {labels_file}")
        return None
    
    print(f"Treinando modelo...")
    print(f"Dataset: {dataset_dir}")
    print(f"Imagens: {images_dir}")
    print(f"Labels: {labels_file}")
    
    # Cria o reconhecedor
    recognizer = CaptchaRecognizer()
    
    # Treina o modelo
    recognizer.train(images_dir, labels_file, epochs=epochs)
    
    # Salva o modelo
    os.makedirs(os.path.dirname(output_model_path), exist_ok=True)
    recognizer.save_model(output_model_path)
    
    print(f"\nTreinamento concluído!")
    print(f"Modelo salvo em: {output_model_path}")
    
    return recognizer


def generate_and_train(num_training_images=500, epochs=20, output_model_path='./models/captcha_model.h5'):
    """Gera um dataset e treina o modelo"""
    
    print(f"Gerando {num_training_images} imagens de CAPTCHA...")
    
    # Gera o dataset
    generator = CaptchaGenerator()
    dataset_dir = './data/training_data'
    generator.generate_dataset(dataset_dir, num_images=num_training_images)
    
    # Treina o modelo
    print(f"\nTreinando modelo...")
    recognizer = train_from_dataset(dataset_dir, output_model_path, epochs=epochs)
    
    return recognizer


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dataset_dir = sys.argv[1]
        output_model_path = sys.argv[2] if len(sys.argv) > 2 else './models/captcha_model.h5'
        epochs = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        
        train_from_dataset(dataset_dir, output_model_path, epochs=epochs)
    else:
        # Gera e treina automaticamente
        print("Iniciando geração e treinamento...")
        generate_and_train(num_training_images=500, epochs=20)
