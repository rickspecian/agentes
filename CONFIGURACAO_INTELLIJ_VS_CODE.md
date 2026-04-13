# ⚙️ CONFIGURAÇÃO DOS AGENTES NETBR — IntelliJ + VS Code

> Instruções passo-a-passo para configurar o protocolo SDD globalmente em ambos os IDEs.

---

## 🎯 O QUE CONFIGURAR

**Arquivo:** `C:\Projetos\Agentes\CLAUDE.md` (Workflow-NetBR)

Este arquivo contém o orquestrador e todas as regras SDD que devem ser aplicadas globalmente.

---

## 📍 INTELLIJ — CONFIGURAÇÃO GLOBAL

### Opção 1️⃣ — GitHub Copilot Plugin (Recomendado)

#### Pré-requisito:
- GitHub Copilot plugin instalado no IntelliJ

#### Passos:

1. **Abra as configurações:**
   - Atalho: `Ctrl+Alt+S` (Windows/Linux) ou `Cmd+,` (macOS)
   - Ou: Menu `File` → `Settings`

2. **Procure por Copilot:**
   - Na barra de busca superior, digite: `copilot`
   - Clique em `GitHub Copilot` ou `Copilot Chat`

3. **Localize o campo de instruções customizadas:**
   - Procure por: `Custom Instructions`, `System Prompt`, `Global Instructions`, ou `Chat System Prompt`
   - O nome pode variar conforme versão do plugin

4. **Cole o conteúdo do CLAUDE.md:**
   ```
   Abra: C:\Projetos\Agentes\CLAUDE.md
   Selecione tudo: Ctrl+A
   Copie: Ctrl+C
   Cole no campo de instruções personalizadas: Ctrl+V
   ```

5. **Aplique as mudanças:**
   - Clique em `Apply` e depois `OK`
   - Feche o IntelliJ completamente
   - Reabra o IntelliJ

#### Validação:
- Abra o chat do Copilot
- Envie: `Nova feature: criar endpoint de teste`
- Se receber resposta com `🔍 TRIAGEM:` → ✅ **Funcionando!**

---

### Opção 2️⃣ — JetBrains AI Assistant

#### Pré-requisito:
- JetBrains AI Assistant plugin instalado no IntelliJ

#### Passos:

1. **Abra as configurações:**
   - Atalho: `Ctrl+Alt+S` (Windows/Linux) ou `Cmd+,` (macOS)
   - Ou: Menu `File` → `Settings`

2. **Procure por AI Assistant:**
   - Na barra de busca superior, digite: `ai assistant`
   - Clique em `AI Assistant`

3. **Acesse a seção de prompts/rules:**
   - Procure por: `Prompt`, `Rules`, `Profile`, `System Instructions`, ou `Custom Prompt`
   - O nome pode variar conforme versão

4. **Crie um novo perfil (se aplicável):**
   - Clique em `New Profile` ou `+`
   - Nome: `Workflow-NetBR`

5. **Cole o conteúdo do CLAUDE.md:**
   ```
   Abra: C:\Projetos\Agentes\CLAUDE.md
   Selecione tudo: Ctrl+A
   Copie: Ctrl+C
   Cole no campo do novo perfil: Ctrl+V
   ```

6. **Defina como padrão (se houver opção):**
   - Marque: `Set as Default Profile` ou similar
   - Clique em `Apply` e depois `OK`
   - Feche e reabra o IntelliJ

#### Validação:
- Abra o chat do AI Assistant
- Envie: `Nova feature: criar endpoint de teste`
- Se receber resposta com `🔍 TRIAGEM:` → ✅ **Funcionando!**

---

## 🔧 VS CODE — CONFIGURAÇÃO GLOBAL

### Opção 1️⃣ — GitHub Copilot Chat Extension

#### Pré-requisito:
- Extensão `GitHub Copilot Chat` instalada no VS Code

#### Passos:

1. **Abra a paleta de comandos:**
   - Atalho: `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS)

2. **Procure por Copilot settings:**
   - Digite: `preferences: open user settings (json)`
   - Pressione Enter
   - Abre o arquivo `settings.json`

3. **Adicione a instrução global:**
   ```json
   "github.copilot.chat.systemPrompt": "[Cole aqui o conteúdo do CLAUDE.md]"
   ```

   **Exemplo completo:**
   ```json
   {
     "github.copilot.chat.systemPrompt": "# 🎯 Agentes de IA — Orquestradores de Workflow\n\n## Consolidação de Orquestradores\n\nEste ficheiro consolida o orquestrador de workflow com nomenclatura NetBR em uma definição única.\n\n---\n\n## 🎯 Workflow-NetBR\n\n### Responsabilidades:\n- ✅ Receber toda solicitação primeiro pelo console\n- ✅ Classificar a solicitação antes de qualquer execução\n...",
     "other.settings": "..."
   }
   ```

4. **Salve o arquivo:**
   - Atalho: `Ctrl+S`

#### ⚠️ IMPORTANTE — Caracteres Especiais:

Se copiar diretamente, use um conversor ou ferramenta:

**Opção A — Manualmente (simples):**
1. Use a paleta de comandos: `Ctrl+Shift+P`
2. Digite: `Copilot: Set custom instructions`
3. Cole o conteúdo do `CLAUDE.md` diretamente no campo

**Opção B — Via arquivo (recomendado se muitos caracteres especiais):**
1. Abra: `C:\Projetos\Agentes\CLAUDE.md`
2. Copie TODO o conteúdo
3. Abra VS Code
4. Paleta de comandos: `Ctrl+Shift+P`
5. Digite: `Copilot: Set custom instructions` (ou similar)
6. Cole o conteúdo

#### Validação:
- Abra o chat do Copilot (`Ctrl+I` ou menu)
- Envie: `Nova feature: criar endpoint de teste`
- Se receber resposta com `🔍 TRIAGEM:` → ✅ **Funcionando!**

---

### Opção 2️⃣ — Cody (Sourcegraph)

#### Pré-requisito:
- Extensão `Cody` instalada no VS Code

#### Passos:

1. **Abra a extensão Cody:**
   - Clique no ícone Cody na sidebar esquerda
   - Ou: Atalho `Ctrl+Shift+Alt+/`

2. **Acesse configurações:**
   - Clique em `Settings` (ícone de engrenagem)
   - Ou: `File` → `Preferences` → `Settings` → procure por `Cody`

3. **Localize o campo de sistema prompt/custom instructions:**
   - Procure por: `System Prompt`, `Custom Instructions`, ou `Custom Prompt`

4. **Cole o conteúdo do CLAUDE.md:**
   ```
   Abra: C:\Projetos\Agentes\CLAUDE.md
   Selecione tudo: Ctrl+A
   Copie: Ctrl+C
   Cole no campo: Ctrl+V
   ```

5. **Salve:**
   - As mudanças são salvas automaticamente

#### Validação:
- Abra o chat do Cody
- Envie: `Nova feature: criar endpoint de teste`
- Se receber resposta com `🔍 TRIAGEM:` → ✅ **Funcionando!**

---

## ✅ VALIDAÇÃO DE CONFIGURAÇÃO (Ambos IDEs)

### Teste Simples:

1. **Abra o chat de IA** (Copilot ou Cody)
2. **Envie esta mensagem exata:**
   ```
   Nova feature: criar endpoint GET /healthcheck
   ```

3. **Resposta esperada (começa com):**
   ```
   🔍 TRIAGEM: Nova feature

   📋 SPEC necessária para definir:
     - Método HTTP (GET?)
     - Path (/healthcheck?)
     - Response esperado (status + campos?)
   
   Defina o contrato no console, depois responda CONFIRMAR.
   ```

### Se receber esta resposta:
✅ **Configuração bem-sucedida!**

### Se NÃO receber (ou recebe algo diferente):
❌ Verifique:
1. Se colou TODO o arquivo `CLAUDE.md` (não parcial)
2. Se fechou e reabriu o IDE
3. Se o arquivo não tem erros de caracteres especiais
4. Tente de novo com Opção B (fallback manual)

---

## 🔄 FLUXO APÓS CONFIGURAÇÃO

### IntelliJ ou VS Code — Qualquer Projeto:

```
Você: "Nova feature: [descrição]"
         ↓
Sistema (CLAUDE.md automático):
  → TRIAGEM (classifica)
  → SPEC (exige especificação)
  → CONFIRMAR (aguarda aprovação)
  → ANALISAR (estuda contexto)
  → PLANEJAR (monta plano)
  → APRESENTAR (exibe plano)
  → AGUARDAR (espera CONFIRMAR)
    ↓  (você responde "CONFIRMAR")
  → DELEGAR (aciona agente especializado)
  → MONITORAR (acompanha)
  → CONCLUIR (emite relatório)
         ↓
Você: Tem seu código, testes e documentação prontos!
```

---

## 📊 COMPARAÇÃO — INTELLIJ vs VS CODE

| Aspecto | IntelliJ | VS Code |
|---------|----------|---------|
| **Setup** | Settings UI visual | settings.json ou UI |
| **Facilidade** | ⭐⭐⭐⭐⭐ Mais fácil | ⭐⭐⭐⭐ Fácil |
| **Recomendação** | Usar Copilot Plugin | Usar Copilot Chat |
| **Performance** | Excelente | Excelente |
| **Global?** | Sim | Sim |
| **Por Projeto?** | Sim (workspace settings) | Sim (workspace settings) |

---

## 🆘 TROUBLESHOOTING

### IntelliJ — "Não encontro o campo de Custom Instructions"

**Solução 1:**
- Verifique se o plugin está instalado: `File` → `Settings` → `Plugins`
- Procure por `GitHub Copilot` ou `JetBrains AI Assistant`
- Se não estiver, instale

**Solução 2:**
- A interface varia por versão
- Procure por termos similares: `Prompt`, `System`, `Instructions`, `Chat`, `Settings`

**Solução 3:**
- Atualize o IntelliJ para a versão mais recente
- Atualize o plugin para a versão mais recente

### VS Code — "Caracteres especiais aparecem estranhos"

**Solução:**
- Não copie diretamente para JSON
- Use: Paleta de comandos → `Copilot: Set custom instructions`
- Cole o conteúdo em campo de texto puro (não JSON direto)

### Ambos IDEs — "O agente não segue o protocolo SDD"

**Solução:**
- Confirme que colou o arquivo **INTEIRO** (não parcial)
- Verifique a última linha: deve estar completa
- Feche e reabra o IDE
- Tente de novo

### "Em um projeto, funciona; em outro, não"

**Solução:**
- Se configurou globalmente, deve funcionar em TODOS
- Se está por-projeto, precise configurar em cada um
- Verifique se copiou para **Global Settings** (não Workspace)

---

## 📋 CHECKLIST DE CONFIGURAÇÃO

### IntelliJ (GitHub Copilot):
- [ ] GitHub Copilot plugin instalado
- [ ] `Settings` → `Copilot` aberto
- [ ] Campo `Custom Instructions` localizado
- [ ] Arquivo `CLAUDE.md` copiado inteiro
- [ ] Colado no campo de instruções
- [ ] `Apply` e `OK` clicados
- [ ] IntelliJ fechado e reaberto
- [ ] Teste enviado: `Nova feature: criar endpoint de teste`
- [ ] Resposta recebida com `🔍 TRIAGEM:`
- [ ] ✅ Configuração validada

### IntelliJ (JetBrains AI Assistant):
- [ ] JetBrains AI Assistant plugin instalado
- [ ] `Settings` → `AI Assistant` aberto
- [ ] Campo `Prompt` ou `Rules` localizado
- [ ] Novo perfil criado ou campo padrão encontrado
- [ ] Arquivo `CLAUDE.md` copiado inteiro
- [ ] Colado no campo do perfil
- [ ] Perfil definido como padrão (se aplicável)
- [ ] `Apply` e `OK` clicados
- [ ] IntelliJ fechado e reaberto
- [ ] Teste enviado: `Nova feature: criar endpoint de teste`
- [ ] Resposta recebida com `🔍 TRIAGEM:`
- [ ] ✅ Configuração validada

### VS Code (Copilot Chat):
- [ ] GitHub Copilot Chat extensão instalada
- [ ] Paleta de comandos aberta (`Ctrl+Shift+P`)
- [ ] Opção `Copilot: Set custom instructions` encontrada
- [ ] Arquivo `CLAUDE.md` copiado inteiro
- [ ] Colado no campo de instruções
- [ ] Arquivo salvo
- [ ] VS Code fechado e reaberto
- [ ] Teste enviado: `Nova feature: criar endpoint de teste`
- [ ] Resposta recebida com `🔍 TRIAGEM:`
- [ ] ✅ Configuração validada

---

## 📞 PRÓXIMOS PASSOS

Após confirmar que o protocolo SDD está ativo:

1. **Abra um projeto** (qualquer um)
2. **Envie uma solicitação real**
3. **Siga o fluxo:**
   - Defina a SPEC
   - Responda `CONFIRMAR` quando solicitado
   - Aprove o plano respondendo `CONFIRMAR`
   - Receba código implementado

---

**Versão:** 1.0.0  
**Data:** 10/04/2026  
**Status:** ✅ Pronto para configuração

🚀 **Escolha seu IDE acima e configure agora!**

