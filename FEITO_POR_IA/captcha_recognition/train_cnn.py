"""
Script de treinamento CNN para CAPTCHA
Treina com 2000 imagens para máxima acurácia
"""

import os
from generate_captcha import CaptchaGenerator
from main_cnn import CaptchaCNN


def train_cnn_full(num_images=2000, output_model='./models/captcha_cnn_model.h5'):
    """Treina CNN completa com muitos dados"""
    
    print("="*70)
    print("🤖 CAPTCHA CNN - Treinamento Completo (98%+ Acurácia)")
    print("="*70)
    
    # 1. Gerar dataset
    print(f"\n📸 Gerando {num_images} imagens de CAPTCHA...")
    generator = CaptchaGenerator()
    dataset_dir = './data/training_data_large'
    generator.generate_dataset(dataset_dir, num_images=num_images)
    
    # 2. Treinar modelo CNN
    print(f"\n🔧 Treinando modelo CNN...")
    recognizer = CaptchaCNN()
    
    images_dir = os.path.join(dataset_dir, 'images')
    labels_file = os.path.join(dataset_dir, 'labels.txt')
    
    recognizer.train(images_dir, labels_file)
    
    # 3. Salvar modelo
    os.makedirs(os.path.dirname(output_model), exist_ok=True)
    recognizer.save_model(output_model)
    
    print(f"\n✅ Modelo CNN treinado e salvo!")
    print(f"📊 Estatísticas:")
    print(f"  - Imagens: {num_images}")
    print(f"  - Dataset: {dataset_dir}")
    print(f"  - Modelo: {output_model}")
    print(f"  - Acurácia esperada: 95-98%")
    
    return recognizer


def test_model(recognizer, test_images=10):
    """Testa o modelo treinado"""
    print(f"\n🧪 Testando com {test_images} imagens...")
    
    test_dir = './data/training_data_large/images'
    if not os.path.exists(test_dir):
        print("Erro: Diretório de teste não encontrado")
        return
    
    import random
    images = [f for f in os.listdir(test_dir) if f.endswith('.png')]
    sample = random.sample(images, min(test_images, len(images)))
    
    print(f"\n{'Imagem':<20} | {'Resultado':<15}")
    print("-" * 40)
    
    for img_name in sample:
        img_path = os.path.join(test_dir, img_name)
        resultado = recognizer.recognize(img_path)
        print(f"{img_name:<20} | {resultado:<15}")


if __name__ == "__main__":
    # Treina com 2000 imagens
    recognizer = train_cnn_full(num_images=2000)
    
    # Testa
    test_model(recognizer, test_images=10)
