# Memória de Longo Prazo e Porta Única

> Proposta conceitual · Anthony William Staiger, com apoio do Claude (Anthropic) · 19/10/2026
> **Status:** ideia em desenvolvimento, ainda não implementada.

## A ideia

As conversas antigas guardadas no menu lateral já são, na prática, uma memória de longo prazo. Em vez de tratá-las só como histórico, elas passam a ser **a memória de longo prazo de verdade**, organizada pelo tempo, e a memória de curto prazo vira a **porta de entrada única**.

## Como funciona

1. **Camada recente:** as últimas 24 horas (por exemplo) ficam em detalhe e são lidas como hoje, usando o timestamp por mensagem.
2. **Camada antiga:** o que é mais velho vira resumo etiquetado (Pessoa / Projeto / Ferramenta / Ruído) e é buscado só quando o assunto pede.
3. **Porta única:** ao voltar ao app, o chat aparece limpo, como uma aba nova. Para ver as mensagens anteriores, o usuário as recarrega com digital, rosto ou PIN. Se for só uma conversa simples, nada é recarregado.

## Ganhos esperados

- **Velocidade e custo:** a aba nova começa leve. Em testes informais do autor (anotações perdidas), a aba saturada chegou a demorar mais de 5 minutos para responder, e a nova respondeu rápido.
- **Contexto melhor:** a memória guarda a história desde o primeiro dia, sem precisar reler tudo a cada mensagem.
- **Privacidade:** quem pega o celular desbloqueado não vê as conversas anteriores sem passar pela porta.

## Limitações conhecidas

- **Caminhos laterais:** menu lateral, busca, prévia em notificações e "esqueci a senha" precisam passar pela mesma porta, senão ela não vale.
- **Resumo perde nuance:** o texto original precisa continuar guardado, fora do caminho.
- **Padrão de escrita** (ritmo, vírgulas, manias) pode servir como **sinal auxiliar**, nunca como única barreira: corretor ortográfico e sotaques regionais o alteram.
- Esta ideia é uma camada de **privacidade e conveniência**, não uma garantia de segurança completa.
