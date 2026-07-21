1. Platform
   1.1 Identify valid search queries and their results - duas questões fáceis de query, 1 com erro de sintaxe e outra utilizando um @entitlements.name que não existe, só marcar que não são válidas
   1.2 Create and schedule search reports - 1 questão para montar o passo a passo de uma schedule, outra de V ou F pra saber se pode editar uma subscription (V)
   1.3 Know how to authenticate to the Rest API - vai passar um curl da api de auth da sp e precisa validar se o payload/endpoint estão corretos
   1.4 Identify different ways you can monitor provisioning activity - esse tema caiu pouco e ele é repetido várias vezes no material de estudo, 2 a 3 questões simples de V ou F
   1.5 Know different security administrations - não caiu, se caiu não associei a isso
   1.6 Understand the use cases surrounding Event Triggers - 1 questão, passou um caso de uso de desligamento e a pergunta era se a trigger participava do fluxo de de-provision (?) essa não sei se acertei, marquei V
   1.7 Know how to configure the different authentication options to the tenant  - caiu umas 3 sobre idp e identity sign in options (de boa, a de sign in que caiu perguntava se as opções de sign in eram: pwd+user, direct connection e sso. Resposta é F, apenas pwd+user e direct connection
   1.8 Recognize the different components of a Workflow - não caiu
   1.9 Know how to backup and restore configurations - 1 questão, qual era o procedimento correto para realizar um backup? (fazer um draft do ambiente produtivo e comparar com o backup) a outra opção não lembro direito mas é bem nada a ver

2. Virtual Appliances
   2.1 Understand virtual appliances and know what they are - aqui tem casca de banana - vai ter questões simples sobre o que é uma VA, mas tem uma em específica que pergunta se a proporção de VA 2:1 em relação a uma VM é a pratica indicada, e não! VA x VM é 1:1, VA pra cluster que é 2:1
   2.2 Monitor the health of virtual appliances - alguns exemplos de trace e perguntava qual o possível diagnóstico ou ação (cenários simples)
   2.3 Perform basic troubleshooting of virtual appliances - vai ter uma questão de um payload do endpoint de setar debug level, precisa saber se o body tá ok, essa não sei se acertei...

3. Identity and Lifecycle Management
   3.1 Understand the use of identity profiles - 2 questões de boa bem genéricas
   3.2 Understand the authentication options in an identity profile - questão do 1.7
   3.3 Know identity attribute mappings and how they function within an identity profile - 2 questões, 1 era sobre qual o procedimento correto de um atributo novo do RH pra inputar na identidade: (Deletar todas as contas e reagregar os usuarios)(F) (Agregar a fonte autoritativa de forma não otimizada)(V)
   3.4 Recognize which options are available for configuring mappings in an identity profile - não caiu
   3.5 Know lifecycle states and their use cases - boas questões sobre, mas todas bem básicas e tranquilas, 1 delas é se o admin pode criar clstates customizados
   3.6 Understand the different provisioning options within a lifecycle state - boas questões também, 1 questão era se o clstate pode executar provisionamento
   3.7 Describe the purpose of the cloud lifecycle state attribute - não caiu

4. Provisioning
   4.1 Understand how provisioning is triggered - não caiu
   4.2 Know the different components of source provisioning - não caiu
   4.3 Understand what the possible provisioning channels are and their high-level use case - 1 questão, selecionar qual opção corresponde ao cenário, chamado no servicenow - service desk integration, leitura e provisionamento em source - direct connection - aprovação de itens manual pro source owner - file based, o outro n lembro o texto mas era web service kkk
   4.4 Understand how to enable logging and different logging levels for specific connectors - Caiu questão de log e análise p carai, a maioria eram cenários específicos e qual eram as melhores decisões pra erros
   4.5 Know which objects to search on to troubleshoot provisioning errors - caiu mas não lmebro os textos...

5. Access Management
   5.1 Recognize how user levels grant specific capabilities - caiu 1, permissões do perfil de helpdesk
   5.2 Understand the basics of entitlements - caiu umas 3, todas simples, 1 por exemplo perguntava se o entitlement era a definição de zero ou mais acessos numa aplicação (F)
   5.3 Understand different types of access that SailPoint supports - caiu quais são as opções de aprovador que um access profile pode ter
   5.4 Know how automated role assignments work - caiu uma de montagem de uma role baseada em critério, são 3 requisitos, ele vai passar um passo a passo de montagem de um critério e pedir pra validar se está certo
   5.5 Troubleshoot access management errors - caiu análise de situação teórica

6. Supporting Governance
   6.1 Recognize the basic steps of access requests - não caiu
   6.2 Understand work reassignment - caiu sobre reset de workreassign ex: se o gestor tinha aprovações pendentes e foi realizado um reassign, o usuário novo vai pegar aquelas pendentes? (F)
   6.3 Understand the approval flow - nao caiu
   6.4 Know the lifecycle of a certification  - caiu montagem de certificação
   6.5 Understand the different types of certifications that are supported in Identity Security Cloud - 1. vai passar um cenário e 2 opções de montagem de certificação, as 2 são válidas, 2. vai passar um cenário com uma certa e uma errada
   6.6 Understand the different types of policies that are supported in Identity Security Cloud - caiu bastante também, SoD, Privileged Access e FII, basicamente selecionar qual se encaixava no contexto proposto

7. Sources
   7.1 Recognize the difference between aggregation types - vai ter uma sobre a diferença de otimizada e não otimizada
   7.2 Know the process for obtaining account and entitlement information - não caiu
   7.3 Understand uncorrelated accounts - caiu umas 2, questões simples sobre qual era a definição de uma conta não correlacionada (é uma identidade de máquina?)F é uma conta que não atendeu ao critério de correlação?V
   7.4 Understand the account deletion process and how the account deletion affects the aggregation process - vai cair uma de delta aggregation, se o delta automaticamente bypassa o account deletion (F)
   7.5 Know the main (generic) different types of connectors (cai sobre conector Generic e conector LDAP) definições e cenários
   7.6 Know how to search for source errors - 1 cenário de entitlement que devia aparecer e não apareceu, qual melhor prática verificar schedule de agregação?V ou realizar um sync identity pra aparecer na identidade (F)
   7.7 Understand the purpose of a source - caiu tbm, se a source era um backup (F) e se um dos propósitos dela era servir de repositório de acessos e usuários (V) 2 questões distintas

8. General knowledge for Identity Security Administrators
   8.1 Define and understand IGA - 3 questões na mesma linha, qual o propósito de IGA, se políticas de SoD faziam parte de IGA (V)
   8.2 Understand compliance - nao caiu
   8.3 Compare and contrast authentication and authorization - caiu 5, cenarios onde perguntava se era autenticação ou autorização, cuidado pq tem casca de banana nas questões
   8.4 Understand the concept of federation - caiu legal - sobre IDP e sailpoint como service provider
   8.5 Know methods of authentication - caiu sobre SAML, OAUTH e OIDC