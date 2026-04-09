# 📑 Índice de Agentes Consolidados

## Bem-vindo ao Repositório Consolidado de Agentes

Este diretório contém os ficheiros consolidados de agentes com nomenclatura NetBR.

---

## 📋 Ficheiros Consolidados

| Ficheiro | Agente Consolidado | Finalidade |
|----------|--------------------|------------|
| **CLAUDE.md** | Workflow-NetBR | Orquestração e delegação de fluxo |
| **BACKEND.md** | JavaSênior-NetBR | Desenvolvimento backend Java |
| **FRONTEND.md** | Frontend-NetBR | Desenvolvimento frontend |
| **ISC.md** | ISC-Senior-NetBR | Integrações SailPoint ISC |
| **REPORTER.md** | Reporter-NetBR | Atualização documental |
| **IIQ.md** | IIQ-Senior-NetBR | Desenvolvimento SailPoint IIQ |

---

## 🎯 Guia de Leitura

### Novo no projeto? Comece por:
1. **INDEX.md** ← você está aqui
2. **CLAUDE.md** ← entenda a orquestração
3. **BACKEND.md** / **FRONTEND.md** / **ISC.md** / **IIQ.md** ← especialidades

### Procura por agente específico?

**Para Orquestração:**
- 🎯 [CLAUDE.md](./CLAUDE.md) — Workflow-NetBR

**Para Backend:**
- 🤖 [BACKEND.md](./BACKEND.md) — JavaSênior-NetBR

**Para Frontend:**
- 🖥️ [FRONTEND.md](./FRONTEND.md) — Frontend-NetBR

**Para ISC Cloud:**
- ☁️ [ISC.md](./ISC.md) — ISC-Senior-NetBR

**Para Documentação:**
- 📊 [REPORTER.md](./REPORTER.md) — Reporter-NetBR

**Para Plugin IIQ:**
- 🪶 [IIQ.md](./IIQ.md) — IIQ-Senior-NetBR

---

## ▶️ Como Iniciar o Orquestrador

Use sempre o `CLAUDE.md` deste projeto como orquestrador principal no chat da IA.

### IntelliJ (JetBrains AI Assistant / Copilot Chat)
1. Abra o chat da IA no projeto `agentes`.
2. Cole a instrução abaixo no console.
3. Em seguida, escreva sua solicitação funcional (feature, bug, investigação, etc.).

```text
Use o arquivo CLAUDE.md deste projeto como orquestrador principal (Workflow-NetBR).
Siga Spec-Driven Development: triagem -> spec -> confirmar spec -> analisar -> planejar -> apresentar plano -> aguardar minha confirmação explícita.
Nao inicie implementacao antes do meu "CONFIRMAR".
Considere apenas os agentes deste projeto: BACKEND.md, FRONTEND.md, ISC.md, IIQ.md e REPORTER.md.
```

### VS Code (Copilot Chat)
1. Abra o chat da IA dentro da pasta deste projeto.
2. Cole a instrução abaixo no console.
3. Depois, envie o pedido que deseja executar.

```text
Atue com o Workflow-NetBR descrito em CLAUDE.md deste projeto.
Antes de qualquer acao: classifique a solicitacao, defina a spec no console, repita a spec entendida, monte o plano completo e espere meu "CONFIRMAR".
So depois de confirmado, delegue para os agentes locais (BACKEND.md, FRONTEND.md, ISC.md, IIQ.md, REPORTER.md).
```

### Prompt curto para uso diário

```text
Siga o CLAUDE.md deste projeto. Nao execute nada antes de apresentar plano e receber "CONFIRMAR".
```

---

## 📌 Regra Obrigatória em Todos os Agentes

**⛔ Nenhum código é escrito antes de `CONFIRMAR`**

Todos os agentes seguem **Spec-Driven Development (SDD)**:

```
CONTRACT -> PLAN -> APPROVAL -> CODE
   ↓         ↓         ↓        ↓
 Spec     Review   CONFIRMAR   Build
```

---

## 💡 Dicas de Uso

1. **Começar novo fluxo?**
   - Leia `CLAUDE.md` para entender a orquestração
   - Consulte `BACKEND.md`, `FRONTEND.md`, `ISC.md` e `IIQ.md` conforme a necessidade

2. **Debugar um agente?**
   - Use os ficheiros consolidados
   - Verifique a seção de protocolo e regras de comportamento

3. **Entender validação de premissas?**
   - Consulte `CLAUDE.md`, `BACKEND.md`, `FRONTEND.md`, `ISC.md` e `REPORTER.md`
   - Cada agente descreve quando deve devolver divergências antes de alterar algo

4. **Entender SDD?**
   - Todos os agentes usam o mesmo princípio
   - Comece por `CLAUDE.md` para a visão geral

---

## 📞 Suporte

Para dúvidas sobre um agente específico:
- **Orquestração?** -> `CLAUDE.md`
- **Backend/Java?** -> `BACKEND.md`
- **Frontend/Next.js?** -> `FRONTEND.md`
- **ISC Cloud?** -> `ISC.md`
- **Documentação?** -> `REPORTER.md`
- **Plugin IIQ?** -> `IIQ.md`

---

## ✅ Checklist de Leitura

- [ ] Conheço os ficheiros consolidados
- [ ] Compreendo a regra SDD obrigatória
- [ ] Sei quais agentes consultar por especialidade
- [ ] Entendo onde validar premissas antes de executar alterações
- [ ] Sei qual prompt usar no IntelliJ e no VS Code para iniciar o Workflow-NetBR
