"""
Interface de linha de comando para reconhecimento de CAPTCHA
Permite testar o modelo facilmente no terminal
"""

import os
import cv2
from main_v2 import CaptchaRecognizer
from pathlib import Path


def print_banner():
    """Exibe um banner inicial"""
    print("\n" + "="*70)
    print("  🔒 CAPTCHA RECOGNITION AI - Interface CLI")
    print("="*70 + "\n")


def print_menu():
    """Exibe o menu principal"""
    print("\n📋 MENU PRINCIPAL:")
    print("  1. Reconhecer uma imagem específica")
    print("  2. Testar múltiplas imagens (dataset)")
    print("  3. Listar imagens disponíveis")
    print("  4. Ver informações do modelo")
    print("  5. Sair")
    print()


def recognize_single_image(recognizer):
    """Reconhece uma imagem única"""
    print("\n📂 RECONHECER IMAGEM ÚNICA")
    print("-" * 70)
    
    image_path = input("Digite o caminho da imagem: ").strip()
    
    if not os.path.exists(image_path):
        print("❌ Arquivo não encontrado!")
        return
    
    print(f"⏳ Reconhecendo {os.path.basename(image_path)}...")
    
    try:
        resultado = recognizer.recognize(image_path)
        
        if resultado:
            print(f"\n✅ CAPTCHA RECONHECIDO: {resultado}")
            
            # Exibe a imagem (opcional)
            img = cv2.imread(image_path)
            if img is not None:
                print(f"   Tamanho: {img.shape[1]}x{img.shape[0]} pixels")
        else:
            print("❌ Erro ao reconhecer CAPTCHA")
    
    except Exception as e:
        print(f"❌ Erro: {str(e)}")


def test_dataset(recognizer):
    """Testa múltiplas imagens do dataset"""
    print("\n📊 TESTAR DATASET")
    print("-" * 70)
    
    dataset_dir = './data/training_data/images'
    
    if not os.path.exists(dataset_dir):
        print(f"❌ Dataset não encontrado em {dataset_dir}")
        return
    
    # Lista imagens
    images = sorted([f for f in os.listdir(dataset_dir) if f.endswith('.png')])
    
    if not images:
        print("❌ Nenhuma imagem encontrada")
        return
    
    # Pergunta quantas testar
    try:
        num_test = int(input(f"Quantas imagens testar? (máx {len(images)}): "))
        num_test = min(num_test, len(images))
    except ValueError:
        num_test = 10
    
    print(f"\n⏳ Testando {num_test} imagens...\n")
    print(f"{'Imagem':<20} | {'Resultado':<15} | Status")
    print("-" * 70)
    
    successes = 0
    
    for i, img_name in enumerate(images[:num_test]):
        img_path = os.path.join(dataset_dir, img_name)
        
        try:
            resultado = recognizer.recognize(img_path)
            
            if resultado:
                status = "✅"
                successes += 1
            else:
                resultado = "Erro"
                status = "❌"
            
            print(f"{img_name:<20} | {resultado:<15} | {status}")
        
        except Exception as e:
            print(f"{img_name:<20} | Erro: {str(e)[:13]:<15} | ❌")
    
    # Resumo
    accuracy = (successes / num_test * 100) if num_test > 0 else 0
    print("-" * 70)
    print(f"✅ Taxa de sucesso: {successes}/{num_test} ({accuracy:.1f}%)\n")


def list_images():
    """Lista imagens disponíveis"""
    print("\n🖼️ IMAGENS DISPONÍVEIS")
    print("-" * 70)
    
    dataset_dir = './data/training_data/images'
    sample_img = './data/sample_captcha.png'
    
    # Dataset
    if os.path.exists(dataset_dir):
        images = [f for f in os.listdir(dataset_dir) if f.endswith('.png')]
        print(f"\n📁 Dataset de treinamento: {len(images)} imagens")
        print(f"   Localização: {os.path.abspath(dataset_dir)}")
        print(f"   Primeiras 5: {', '.join(images[:5])}")
    
    # Sample
    if os.path.exists(sample_img):
        print(f"\n📌 Imagem de amostra:")
        print(f"   {os.path.abspath(sample_img)}")
    
    print("\n💡 Dica: Você pode adicionar suas próprias imagens em ./data/")


def show_model_info(recognizer):
    """Mostra informações do modelo"""
    print("\n🤖 INFORMAÇÕES DO MODELO")
    print("-" * 70)
    
    print(f"Caracteres suportados: {len(recognizer.characters)} caracteres")
    print(f"Alfabeto: {recognizer.characters}")
    print(f"Tamanho de entrada: {recognizer.img_width}x{recognizer.img_height} pixels")
    print(f"Comprimento máximo: {recognizer.max_length} caracteres")
    
    if recognizer.model:
        print(f"\n✅ Modelo carregado")
        print(f"   Tipo: MLPClassifier (scikit-learn)")
        print(f"   Camadas: [Input] -> 256 -> 128 -> [Output]")
    else:
        print(f"\n❌ Nenhum modelo carregado")


def main():
    """Loop principal da aplicação"""
    print_banner()
    
    # Carrega o modelo
    model_path = './models/captcha_model.h5'
    
    if not os.path.exists(model_path):
        print(f"❌ Modelo não encontrado em: {model_path}")
        print("   Execute: python train_model.py")
        return
    
    print(f"🔄 Carregando modelo...")
    recognizer = CaptchaRecognizer(model_path)
    print("✅ Modelo carregado com sucesso!\n")
    
    while True:
        print_menu()
        choice = input("Escolha uma opção: ").strip()
        
        if choice == "1":
            recognize_single_image(recognizer)
        
        elif choice == "2":
            test_dataset(recognizer)
        
        elif choice == "3":
            list_images()
        
        elif choice == "4":
            show_model_info(recognizer)
        
        elif choice == "5":
            print("\n👋 Até logo!\n")
            break
        
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()
