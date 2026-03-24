# 🔒 CAPTCHA Recognition - Guia de Uso

## 📚 Índice
1. [Como Rodar](#como-rodar)
2. [Obter Imagens](#onde-obter-imagens-de-teste)
3. [Interfaces Disponíveis](#interfaces-disponíveis)
4. [Exemplos de Uso](#exemplos-de-uso)

---

## 🚀 Como Rodar

### **Opção 1: Interface de Linha de Comando (Recomendado para iniciantes)**

```powershell
cd c:\Users\u26131\Desktop\repositorios\projetos_pessoais\captcha_recognition
c:/Users/u26131/Desktop/repositorios/projetos_pessoais/.venv/Scripts/python.exe cli.py
```

**O que você verá:**
```
======================================================================
  🔒 CAPTCHA RECOGNITION AI - Interface CLI
======================================================================

📋 MENU PRINCIPAL:
  1. Reconhecer uma imagem específica
  2. Testar múltiplas imagens (dataset)
  3. Listar imagens disponíveis
  4. Ver informações do modelo
  5. Sair

Escolha uma opção: _
```

---

### **Opção 2: Interface Gráfica (GUI)**

```powershell
cd c:\Users\u26131\Desktop\repositorios\projetos_pessoais\captcha_recognition
c:/Users/u26131/Desktop/repositorios/projetos_pessoais/.venv/Scripts/python.exe app_gui.py
```

**O que você verá:**

```
┌──────────────────────────────────────────┐
│   🔒 CAPTCHA Recognition AI               │
├──────────────────────────────────────────┤
│                                           │
│  [📂 Abrir Imagem] [🔍 Reconhecer]      │
│  [📊 Testar Dataset]                     │
│                                           │
│  Status: Aguardando ação...              │
│                                           │
│  ┌─────────────────────────────────────┐ │
│  │                                     │ │
│  │    [Imagem CAPTCHA exibida aqui]   │ │
│  │                                     │ │
│  └─────────────────────────────────────┘ │
│                                           │
│  CAPTCHA Reconhecido: ___________        │
│                                           │
└──────────────────────────────────────────┘
```

---

### **Opção 3: Python Direto (Para programadores)**

```python
from main_v2 import CaptchaRecognizer

# Carregar modelo
recognizer = CaptchaRecognizer('./models/captcha_model.h5')

# Reconhecer CAPTCHA
resultado = recognizer.recognize('./data/sample_captcha.png')
print(f"CAPTCHA: {resultado}")  # Output: CAPTCHA: 1CsbF
```

---

## 🖼️ Onde Obter Imagens de Teste

### **1. Imagens Geradas (Já Disponíveis)** ✅

Você já tem 500 imagens prontas:

```
c:\Users\u26131\Desktop\repositorios\projetos_pessoais\captcha_recognition\
  └─ data/
      └─ training_data/
          └─ images/          # ← 500 imagens CAPTCHA
              ├─ captcha_00000.png
              ├─ captcha_00001.png
              └─ ... (até captcha_00499.png)
```

**Para testar:**
1. Execute `cli.py`
2. Escolha opção **3** para listar imagens
3. Escolha opção **2** para testar dataset

---

### **2. Exemplo de Amostra**

```
./data/sample_captcha.png    # Uma imagem de exemplo pronta
```

Reconhecer direto:
```powershell
# CLI
python cli.py
# Digite: ./data/sample_captcha.png

# Ou Python direto
python -c "from main_v2 import CaptchaRecognizer; r = CaptchaRecognizer('./models/captcha_model.h5'); print(r.recognize('./data/sample_captcha.png'))"
```

---

### **3. CAPTCHAs Reais (Para Downloads)**

**Kaggle Datasets:**
- https://www.kaggle.com/search?q=captcha
- Busque por: "CAPTCHA dataset"
- Baixe e coloque em `./data/`

**GitHub:**
```powershell
git clone https://github.com/lepture/captcha.git
```

**Websites com CAPTCHA (para screenshot):**
1. Tire screenshot de CAPTCHAs do Google, hCaptcha, etc.
2. Salve como PNG em `./data/`
3. Teste com CLI opção 1

---

### **4. Gerar Mais Imagens**

Se quiser gerar mais CAPTCHAs:

```powershell
python generate_captcha.py
```

Isso cria 500 novas imagens e atualiza os labels.

---

## 🎮 Interfaces Disponíveis

### **Interface 1: CLI (Linha de Comando)** 

**Arquivo:** `cli.py`

**Menu:**
```
1. Reconhecer uma imagem específica
   - Digite o caminho: ./data/sample_captcha.png
   - Resultado: CAPTCHA RECONHECIDO: 1CsbF

2. Testar múltiplas imagens (dataset)
   - Testa até 10 imagens por vez
   - Mostra taxa de sucesso

3. Listar imagens disponíveis
   - Mostra onde estão as imagens
   - Conta total de imagens

4. Ver informações do modelo
   - Caracteres suportados
   - Tamanho de entrada
   - Arquitetura

5. Sair
```

**Vantagens:**
- ✅ Simples e direto
- ✅ Funciona em qualquer terminal
- ✅ Não precisa de dependências extras
- ✅ Melhor para teste rápido

---

### **Interface 2: GUI (Gráfica)**

**Arquivo:** `app_gui.py`

**Recursos:**
```
🔘 Botões:
   - 📂 Abrir Imagem     → Seleciona arquivo
   - 🔍 Reconhecer      → Processa imagem
   - 📊 Testar Dataset  → Testa 10 imagens

📊 Exibição:
   - Imagem selecionada no centro
   - Resultado em destaque
   - Status em tempo real

📌 Informações:
   - Status atual
   - Caminho do arquivo
   - Taxa de sucesso
```

**Vantagens:**
- ✅ Visual e intuitivo
- ✅ Preview da imagem
- ✅ Teste em lote automático
- ✅ Melhor para apresentações

---

### **Interface 3: Python (Programação)**

**Arquivo:** `main_v2.py`

**Uso:**
```python
from main_v2 import CaptchaRecognizer

# Inicializar
recognizer = CaptchaRecognizer('./models/captcha_model.h5')

# Reconhecer
resultado = recognizer.recognize('./caminho/imagem.png')

# Treinar novo modelo (opcional)
recognizer.train('./data/training_data/images', 
                 './data/training_data/labels.txt', 
                 epochs=20)
recognizer.save_model('./models/novo_modelo.h5')
```

**Métodos:**
- `recognize(image_path)` → Reconhece um CAPTCHA
- `train(images_dir, labels_file, epochs)` → Treina modelo
- `save_model(path)` → Salva modelo
- `load_model(path)` → Carrega modelo
- `preprocess_image(path)` → Processa imagem
- `extract_features(image)` → Extrai características

**Vantagens:**
- ✅ Total controle
- ✅ Integração em aplicações
- ✅ Automação em lote
- ✅ Para desenvolvedores

---

## 📋 Exemplos de Uso

### **Exemplo 1: Reconhecer Uma Imagem (CLI)**

```powershell
# Iniciar CLI
python cli.py

# Menu aparece:
# Escolha uma opção: 1
# Digite o caminho da imagem: ./data/sample_captcha.png
# ✅ CAPTCHA RECONHECIDO: 1CsbF
```

---

### **Exemplo 2: Testar Dataset Completo (CLI)**

```powershell
python cli.py

# Escolha uma opção: 2
# Quantas imagens testar? (máx 500): 20

# Resultados:
# Imagem              | Resultado       | Status
# captcha_00000.png   | A3xK2          | ✅
# captcha_00001.png   | 7FgHq          | ✅
# ...
# ✅ Taxa de sucesso: 18/20 (90.0%)
```

---

### **Exemplo 3: Usar em Aplicação Python**

```python
from main_v2 import CaptchaRecognizer
import os

# Carregar modelo
recognizer = CaptchaRecognizer('./models/captcha_model.h5')

# Testar todas as imagens do dataset
dataset_dir = './data/training_data/images'
images = os.listdir(dataset_dir)

for img_name in images[:5]:  # Primeiras 5
    img_path = os.path.join(dataset_dir, img_name)
    resultado = recognizer.recognize(img_path)
    print(f"{img_name}: {resultado}")
```

---

### **Exemplo 4: Integrar com Selenium (Web Scraping)**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from main_v2 import CaptchaRecognizer
import tempfile

# Inicializar
driver = webdriver.Chrome()
recognizer = CaptchaRecognizer('./models/captcha_model.h5')

# Abrir site com CAPTCHA
driver.get("https://site-com-captcha.com")

# Encontrar elemento CAPTCHA
captcha_element = driver.find_element(By.ID, "captcha_image")

# Salvar screenshot
with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
    captcha_element.screenshot(tmp.name)
    
    # Reconhecer
    resultado = recognizer.recognize(tmp.name)
    print(f"CAPTCHA resolvido: {resultado}")
    
    # Preencher campo
    input_field = driver.find_element(By.ID, "captcha_input")
    input_field.send_keys(resultado)
    input_field.submit()
```

---

### **Exemplo 5: Usar via API REST (Flask)**

```python
from flask import Flask, request, jsonify
from main_v2 import CaptchaRecognizer
import os
import tempfile

app = Flask(__name__)
recognizer = CaptchaRecognizer('./models/captcha_model.h5')

@app.route('/recognize', methods=['POST'])
def recognize():
    # Recebe imagem
    file = request.files['image']
    
    # Salva temporariamente
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        file.save(tmp.name)
        
        # Reconhece
        resultado = recognizer.recognize(tmp.name)
        
        # Remove arquivo temp
        os.remove(tmp.name)
    
    return jsonify({'captcha': resultado})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**Usar:**
```bash
curl -X POST -F "image=@captcha.png" http://localhost:5000/recognize
# {"captcha": "1CsbF"}
```

---

## 💡 Dicas Importantes

1. **Melhor Performance:** Use imagens no mesmo formato que o treino (200x50, PNG)
2. **Falsos Negativos:** Se o CAPTCHA tem muito ruído ou distorção, a precisão cai
3. **Retreinar:** Se quiser melhorar, gere mais imagens e execute `train_model.py` novamente
4. **Backup:** Salve o modelo em `./models/` antes de retreinar

---

## 🆘 Troubleshooting

**Erro: "Modelo não encontrado"**
```powershell
python train_model.py  # Treina e cria o modelo
```

**Erro: "ModuleNotFoundError"**
```powershell
pip install numpy opencv-python Pillow scikit-learn
```

**Imagem não reconhece corretamente**
- Gere mais dados: `python generate_captcha.py`
- Retreine: `python train_model.py`

---

## 📞 Resumo Rápido

| Tarefa | Comando | Arquivo |
|--------|---------|---------|
| **CLI Interativo** | `python cli.py` | cli.py |
| **GUI Gráfica** | `python app_gui.py` | app_gui.py |
| **Reconhecer** | `python -c "..."` | main_v2.py |
| **Gerar Imagens** | `python generate_captcha.py` | generate_captcha.py |
| **Treinar Modelo** | `python train_model.py` | train_model.py |

---

**Versão:** 1.0  
**Data:** 24/03/2026  
**Status:** ✅ Funcionando
