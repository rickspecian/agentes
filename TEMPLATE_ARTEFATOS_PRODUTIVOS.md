# 📦 TEMPLATE — ARTEFATOS_PRODUTIVOS.md

**⚠️ ESTE É UM TEMPLATE PARA O AGENTE IIQ**

Sempre que um novo projeto for configurado, o agente IIQ-Senior-NetBR deverá:
1. Analisar a estrutura do projeto final
2. Identificar o caminho correto do projeto
3. Criar um arquivo `ARTEFATOS_PRODUTIVOS.md` na raiz do projeto
4. Usar este template como base

---

# 📦 ARTEFATOS PRODUTIVOS DO PROJETO

**Projeto:** [NOME_PROJETO]  
**Caminho Projeto:** [CAMINHO_PROJETO_FINAL]  
**Data de Atualização:** [DATA_CRIACAO]  
**Status:** ✅ Operacional

---

## 🎯 Propósito

Este arquivo mantém registro de todos os artefatos e arquivos **produtivos** dentro deste projeto que podem ser usados como referência, template ou base para novas implementações.

**Produtivo** = Funcional em ambiente real, testado e validado.

---

## 📂 ESTRUTURA DO PROJETO

```
[CAMINHO_PROJETO_FINAL]
├── applications/          ← Aplicações SailPoint
├── rules/                 ← Rules BeanShell
├── Agentes/               ← Sistema de orquestração (CLAUDE + Especialistas)
└── [Outros arquivos de configuração]
```

---

## ✅ ARTEFATOS PRODUTIVOS IDENTIFICADOS

### 📋 **Aplicações (Applications)**

| Arquivo | Status | Versão | Notas |
|---------|--------|--------|-------|
| `[App Name].xml` | [Status] | 1.0 | [Descrição] |

**Estado:**
- [ ] Identificada
- [ ] Totalmente funcional
- [ ] Necessita correção
- [ ] Pronta para produção

**Próxima Ação:** [Descrever ação necessária]

---

### 🔧 **Rules (BeanShell XML)**

| Arquivo | Status | Funcionalidade | Notas |
|---------|--------|----------------|-------|
| `[Rule Name].xml` | [Status] | [Funcionalidade] | [Notas] |

**Estado Geral:** [Status geral]

---

## 🔗 REFERÊNCIAS EXTERNAS DISPONÍVEIS

### 📚 **Samples de SailPoint IIQ**

**Localização:** `C:\Projetos\Agentes\Samples`

**Conteúdo Esperado:**
- Exemplos de estruturas XML válidas
- Templates de Rules BeanShell
- Estruturas de Aplicações
- Workflows de exemplo
- Conectores funcionais

**⚠️ IMPORTANTE:**
- **Nem tudo nessa pasta é 100% correto**
- Os exemplos servem como **referência**, não como verdade absoluta
- O agente **IIQ-Senior-NetBR** pode e deve fazer sugestões de melhoria
- Usar como base, mas sempre validar contra `sailpoint.dtd`

---

## 🎯 COMO USAR ESTE ARQUIVO

### Para o Agente IIQ-Senior-NetBR:
1. **Ao implementar novo artefato:** Consulte a lista de produtivos acima
2. **Para dúvidas de estrutura:** Verifique samples em `C:\Projetos\Agentes\Samples`
3. **Ao encontrar erro:** Considere sugestão de melhoria (não é gospel)
4. **Ao completar tarefa:** Atualize este arquivo com novo artefato

### Para o Workflow-NetBR (CLAUDE):
1. **Ao planejar implementação:** Veja quais artefatos já existem produtivos
2. **Ao delegar:** Mencione artefatos produtivos como referência
3. **Ao monitorar:** Valide se as regras do projeto foram usadas

---

## 📊 MATRIZ DE ARTEFATOS × CASOS DE USO

```
[Descrever os artefatos principais e seus relacionamentos]
```

---

## 🔄 FLUXO DE ATUALIZAÇÃO DESTE ARQUIVO

Sempre que uma **nova implementação for concluída e entregue**, este arquivo deve ser atualizado:

1. **REPORTER-NetBR** identifica conclusão
2. **REPORTER-NetBR** atualiza matriz de produtivos
3. **Usuário** valida se artefato está realmente pronto
4. **Este arquivo** é versionado e datado

---

## 📝 VERSIONAMENTO

| Versão | Data | Alteração |
|--------|------|-----------|
| 1.0 | [DATA] | Criação inicial |
| [Próximas] | [Data] | [Alterações futuras] |

---

## ✅ CHECKLIST DE QUALIDADE

Antes de marcar como **PRODUTIVO**, o artefato deve atender:

- [ ] Importa sem erros no Debug do IIQ
- [ ] Passa validação DTD (sailpoint.dtd)
- [ ] Testes funcionais concluídos
- [ ] Documentado e comentado
- [ ] Segue padrões do projeto
- [ ] Não contém credenciais hardcoded
- [ ] Tratamento de erros implementado

---

## 🔗 CONEXÕES COM OUTROS ARQUIVOS

- **AGENTES_CONFIGURACAO_OBRIGATORIA.md** → Define quando usar este arquivo
- **IIQ.md** → Agente que consulta este arquivo
- **INDICE_RAPIDO_AGENTES.md** → Referencia localização
- **REGISTRO_DE_ATIVACAO.md** → Documenta ativação do sistema

---

## 🚀 PRÓXIMAS TAREFAS

- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

---

**Documento gerenciado por:** REPORTER-NetBR  
**Última atualização:** [DATA]  
**Próxima revisão:** Após próxima entrega

