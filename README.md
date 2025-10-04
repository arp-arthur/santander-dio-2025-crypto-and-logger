# Relatório - Exemplo de Ransomware & Keylogger


**Autor**: Arthur da Rosa Pinheiro


## Resumo

Este relatório tem como objetivo descrever e explorar de forma controlada o funcionamento de dois tipos de *malwares* comumente estudados: ransomware e *keylogger*. 

Recomenda-se utilizar os scripts contidos aqui em ambientes isolados e exclusivamente para fins acadêmicos.

A simulação do *ransomware* priorizou o entendimento de como *Threat Actors* realizam tais ataques e a gestão de chaves, fluxos de criptografia e restauração.

No estudo do *keylogger*, foram explorados conceitos de captura de eventos do teclado.


## Introdução

*Ransomwares* são tipos de *malware* predominantemente de motivação financeira, em que arquivos ou sistemas são criptografados e a vítima é extorquida para obter a *key* de recuperação. Com isso, eles comprometem a disponibilidade dos sistemas e recursos.

Por outro lado, *Keyloggers* são *malware* mais comuns. Na maioria das vezes possuem o intuito financeiro, mas nem sempre. 



## Detecção e IoCs

* **Ransomwares**: Pode-se procurar por arquivos .enc (por exemplo, pode incluir outras extensões como .cry); possíveis tentativas de apagar *snapshots/shadow copies*; possível comunicação com servidores C2 (*Command & Control*)

* **Keyloggers**: processos suspeitos, exigindo permissões elevadas incomuns; criação periódica de arquivos de log; mecanismos de persistência na inicialização, registros de autorun e pastas de inicialização; tarefas agendadas.

## Documentação Técnica

### 1. Ransomware

#### 1.1 encrypt.py

No início da main, gera-se a chave simétrica e guarda-se em um arquivo .key dentro do diretório .key.

Depois, é chamada a função para recuperar diretórios, subdiretórios na pasta corrente e, para cada arquivo encontrado, o script abre para leitura e escrita.

O arquivo é aberto e obtém-se o conteúdo lido criptografado em *get_encrypted_content*. Em seguida, é preciso mover o cursor para o início do arquivo para não escrever no final dele.

### 1.2 decrypt.py

Na main, pega-se a *key* guardada no arquivo .key (em get_key()).

Em seguida, o script lê o conteúdo criptografado do arquivo e decrypta em get_decrypted_content().

O cursor é enviado para o início do arquivo e o conteúdo em *plaintext* é gravado no arquivo novamente, em seguida, é necessário dar um truncate a fim de eliminar bytes remanescentes da leitura.

### 2. Keylogger

#### 2.1 logger.py

Em main() é executado listener.join() a fim de capturar eventos de teclado. Para cada evento, o script verifica se a tecla é "relevante". Caso positivo, escreve em um arquivo *captured.txt*


### 3. Mitigações

* **Backups contínuos**: Backups e shadow copies contínuos. É imprescindível que esses artefatos estejam em um servidor distinto. 1 cópia offline/imutável e teste de restauração

* **EDR/Antimalware** com detecção comportamental (criptografia em massa, deleção de snapshots, etc).

* **Boas práticas**: bloqueios de macro, patching e segmentação de rede.

* **Isolamento rápido do host**, coleta de evidências e restauração de backups.

* **Adoção de boas práticas de segurança da informação** como *least privilege principle*, por exemplo, implementar MFA

* **Eventos de awareness em cibersegurança** para funcionários (no caso de ambientes corporativos).