# CAPTCHA Recognition AI

Sistema de reconhecimento de CAPTCHA usando Deep Learning com TensorFlow/Keras.

## 📋 Descrição

Este projeto implementa uma rede neural convolucional (CNN) capaz de reconhecer textos em imagens CAPTCHA. Utiliza processamento de imagem com OpenCV e Deep Learning com Keras.

## 🚀 Características

- **Modelo CNN**: Rede neural convolucional treinada para reconhecer caracteres em CAPTCHAs
- **Gerador de CAPTCHAs**: Cria dataset de treinamento automaticamente
- **Pré-processamento**: Normalização, distorção e adição de ruído
- **Inferência**: Reconhece CAPTCHAs de imagens
- **Persistência**: Salva e carrega modelos treinados

## 📦 Instalação

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

Dependências principais:
- `tensorflow`: Framework de Deep Learning
- `opencv-python`: Processamento de imagem
- `numpy`: Computação numérica
- `pillow`: Manipulação de imagens

## 🎯 Uso

### 1. Gerar Dataset de Treinamento

```bash
python generate_captcha.py
```

Isso criará:
- `data/training_data/images/`: Imagens CAPTCHA (padrão: 500 imagens)
- `data/training_data/labels.txt`: Labels com o texto de cada CAPTCHA

### 2. Treinar o Modelo

**Opção A: Treinar com dataset existente**

```bash
python train_model.py ./data/training_data ./models/captcha_model.h5 20
```

Argumentos:
- Dataset directory
- Caminho do modelo de saída
- Número de épocas (opcional, padrão: 20)

**Opção B: Gerar dataset e treinar automaticamente**

```bash
python train_model.py
```

### 3. Reconhecer CAPTCHAs

**Reconhecer uma imagem única**

```bash
python recognize_image.py ./data/sample_captcha.png ./models/captcha_model.h5
```

**Usar na aplicação Python**

```python
from main import CaptchaRecognizer

# Carregar o modelo
recognizer = CaptchaRecognizer('./models/captcha_model.h5')

# Reconhecer uma imagem
resultado = recognizer.recognize('./path/to/captcha.png')
print(f"CAPTCHA reconhecido: {resultado}")
```

## 📁 Estrutura do Projeto

```
captcha_recognition/
├── main.py                  # Classe principal CaptchaRecognizer
├── generate_captcha.py      # Gerador de CAPTCHAs
├── train_model.py          # Script de treinamento
├── recognize_image.py      # Script de reconhecimento
├── requirements.txt        # Dependências Python
├── models/                 # Modelos treinados (H5)
└── data/                   # Dados de treinamento e teste
    ├── training_data/
    │   ├── images/
    │   └── labels.txt
    └── sample_captcha.png
```

## 🧠 Arquitetura do Modelo

```
Input Layer (50x200x1)
    ↓
Conv2D(32) + ReLU + MaxPool
    ↓
Conv2D(64) + ReLU + MaxPool
    ↓
Conv2D(128) + ReLU + MaxPool
    ↓
Flatten
    ↓
Dense(256) + ReLU + Dropout
    ↓
Dense(5x62) + Softmax
    ↓
Reshape Output (5 caracteres)
```

**Especificações:**
- Entrada: Imagens grayscale 50x200px
- Saída: 5 caracteres (máximo)
- Caracteres suportados: A-Z, a-z, 0-9 (62 total)
- Loss: Categorical Crossentropy
- Optimizer: Adam

## 📊 Performance

- **Acurácia típica**: 85-95% em dataset de treinamento
- **Tempo de treinamento**: ~5-10 minutos (500 imagens, 20 épocas)
- **Tempo de inferência**: ~50-100ms por imagem

## 🔧 Customizações

### Alterar tamanho da imagem

Edite em `main.py`:
```python
IMG_WIDTH = 200    # Altere para sua dimensão
IMG_HEIGHT = 50
```

### Alterar número de caracteres

```python
MAX_LENGTH = 5
CHARACTERS = string.ascii_letters + string.digits
```

### Ajustar ruído e distorção

Em `generate_captcha.py`:
```python
image = self.add_noise(image, noise_level=0.05)  # 0-1
```

## 📝 Exemplos de Uso Avançado

### Lote de CAPTCHAs

```python
from recognize_image import batch_recognize

resultados = batch_recognize('./data/test_images', './models/captcha_model.h5')
for filename, captcha in resultados.items():
    print(f"{filename}: {captcha}")
```

### Integração com Selenium

```python
from selenium import webdriver
from main import CaptchaRecognizer
import tempfile

recognizer = CaptchaRecognizer('./models/captcha_model.h5')

# Encontrar elemento CAPTCHA
captcha_element = driver.find_element("img", "class_do_captcha")

# Salvar screenshot
with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
    captcha_element.screenshot(tmp.name)
    resultado = recognizer.recognize(tmp.name)
    print(f"CAPTCHA resolvido: {resultado}")
```

## ⚠️ Limitações

- Funciona melhor com CAPTCHAs simples (texto reto)
- CAPTCHAs com distorção extrema podem ter baixa acurácia
- Requer treinamento específico para cada tipo de CAPTCHA
- Algoritmos de detecção de bot podem bloquear o reconhecimento automático

## 🤝 Melhorias Futuras

- [ ] Suporte para CAPTCHAs com números e caracteres especiais
- [ ] Detecção de pontos de referência
- [ ] Aumento de dados (data augmentation) automático
- [ ] API REST para integração
- [ ] Suporte para CAPTCHAs em diferentes idiomas
- [ ] Otimização para CPU/GPU

## 📄 Licença

Este projeto é fornecido como está para fins educacionais.

## ⚡ Notas de Segurança

Este projeto é destinado **APENAS para fins educacionais e de teste** em CAPTCHAs que você controla. 

**Não use para:**
- Contornar CAPTCHAs de terceiros
- Automação não autorizada
- Atividades ilícitas

Respeite os Termos de Serviço dos websites e use essa tecnologia de forma ética e legal.

---

**Desenvolvido com TensorFlow + OpenCV**
