
## 📅 Dia 1 — Configuração de Ambiente

### 1. Criar um ambiente virtual com `venv`

#### Windows
```bash
python -m venv venv
```

#### Linux ou macOS
```bash
python3 -m venv venv
```

---

### 2. Ativar o ambiente virtual

#### Windows
```bash
.\venv\Scripts\activate
```

#### Linux ou macOS
```bash
source venv/bin/activate
```

---

### 3. Por que usar um ambiente virtual?

Um ambiente virtual permite:

- Gerenciar os pacotes e dependências de forma isolada para cada projeto;
- Evitar conflitos entre versões de bibliotecas utilizadas em diferentes projetos;
- Ter maior controle e organização do ambiente de desenvolvimento.

---

📌 *Dica:* Para desativar o ambiente virtual, basta digitar:
```bash
deactivate
```
