"""
Script para reconhecer CAPTCHAs em imagens
Permite reconhecer um CAPTCHA a partir de uma imagem
"""

import sys
import os
from main import CaptchaRecognizer
import cv2


def recognize_captcha_from_path(image_path, model_path=None):
    """Reconhece um CAPTCHA de uma imagem"""
    
    # Verifica se a imagem existe
    if not os.path.exists(image_path):
        print(f"Erro: Arquivo não encontrado: {image_path}")
        return None
    
    # Carrega o reconhecedor
    recognizer = CaptchaRecognizer(model_path)
    
    # Reconhece o CAPTCHA
    result = recognizer.recognize(image_path)
    
    if result:
        print(f"CAPTCHA reconhecido: {result}")
        return result
    else:
        print("Erro ao reconhecer CAPTCHA")
        return None


def batch_recognize(directory, model_path=None):
    """Reconhece múltiplos CAPTCHAs de um diretório"""
    
    recognizer = CaptchaRecognizer(model_path)
    results = {}
    
    # Lista todas as imagens PNG no diretório
    for filename in os.listdir(directory):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = os.path.join(directory, filename)
            result = recognizer.recognize(image_path)
            results[filename] = result
            print(f"{filename}: {result}")
    
    return results


def visualize_and_recognize(image_path, model_path=None):
    """Reconhece um CAPTCHA e exibe a imagem"""
    
    if not os.path.exists(image_path):
        print(f"Erro: Arquivo não encontrado: {image_path}")
        return None
    
    # Carrega e exibe a imagem
    image = cv2.imread(image_path)
    
    if image is None:
        print("Erro ao carregar a imagem")
        return None
    
    # Reconhece o CAPTCHA
    recognizer = CaptchaRecognizer(model_path)
    result = recognizer.recognize(image_path)
    
    # Adiciona o resultado à imagem
    if result:
        text = f"CAPTCHA: {result}"
        cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                   0.7, (0, 255, 0), 2)
    
    # Exibe a imagem
    cv2.imshow("CAPTCHA Recognition", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python recognize_image.py <caminho_imagem> [modelo_path]")
        print("\nExemplo:")
        print("  python recognize_image.py ./data/sample_captcha.png")
        print("  python recognize_image.py ./data/sample_captcha.png ./models/captcha_model.h5")
    else:
        image_path = sys.argv[1]
        model_path = sys.argv[2] if len(sys.argv) > 2 else None
        
        # Reconhece e visualiza
        result = visualize_and_recognize(image_path, model_path)
