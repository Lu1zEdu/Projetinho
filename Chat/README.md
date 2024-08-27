# Terminal Chat Application

## Descrição

A **Terminal Chat Application** é um projeto desenvolvido em Java que simula um chat com uma interface temática de terminal. A aplicação permite aos usuários enviar e receber mensagens em um ambiente que imita um terminal de texto, além de suportar vários comandos e personalizações.

## Funcionalidades

- **Interface de Terminal:** Ambiente de chat com visual de terminal.
- **Alteração de Nome de Usuário:** Permite ao usuário alterar seu nome exibido nas mensagens.
- **Comandos de Chat:** Suporte para comandos para ajuda, limpar mensagens e reportar.
- **Persistência de Relatórios:** Armazena relatórios em um arquivo com detalhes sobre quem reportou e o que foi reportado.
- **Conexão em Rede:** Vários usuários podem se conectar e interagir na mesma rede local.

## Requisitos

- **Java 8** ou superior.
- **IDE** como IntelliJ IDEA, Eclipse, ou qualquer outra para desenvolvimento Java.
- **Bibliotecas** padrão do Java.

## Instalação e Configuração

### Clonar o Repositório

Clone o repositório do projeto:

```bash
git clone https://github.com/seu-usuario/terminal-chat.git
cd terminal-chat
```

### Compilar o Projeto

Compile o código-fonte:

```bash
javac -d bin src/*.java
```

### Executar o Servidor

Inicie o servidor para aceitar conexões dos clientes:

```bash
java -cp bin ChatServer
```

### Executar o Cliente

Em outra instância de terminal, inicie o cliente. Certifique-se de que o `SERVER_IP` no código do cliente está configurado para o IP do servidor:

```bash
java -cp bin ChatClient
```

## Comandos

Aqui estão os comandos suportados pela aplicação:

- **`--help` ou `--h`**: Mostra uma lista de comandos disponíveis.

  ```
  --help
  ```

- **`--clear` ou `--c`**: Limpa todas as mensagens do chat.

  ```
  --clear
  ```

- **`--user <novo-nome>` ou `--u <novo-nome>`**: Altera o nome de usuário. Exemplo:

  ```
  --user NovoNome
  ```

- **`--report <mensagem>` ou `--r <mensagem>`**: Reporta um usuário e armazena o relatório em um arquivo. Exemplo:

  ```
  --report Usuário x enviou mensagem ofensiva
  ```

- **`--exit` ou `--e`**: Sai da aplicação.

  ```
  --exit
  ```

## Exemplo de Uso

Após iniciar o servidor e um ou mais clientes, você pode interagir da seguinte forma:

1. **Alterar Nome:**

   Digite o comando para alterar seu nome de usuário:

   ```
   --user NovoNome
   ```

   Isso alterará o nome de usuário exibido nas mensagens para `NovoNome`.

2. **Enviar Mensagens:**

   Digite uma mensagem e pressione Enter. As mensagens serão exibidas com o prefixo do nome de usuário atual.

   ```
   Olá, este é um exemplo de mensagem.
   ```

3. **Limpar Mensagens:**

   Para limpar todas as mensagens do chat:

   ```
   --clear
   ```

4. **Reportar um Usuário:**

   Para reportar um usuário com uma mensagem:

   ```
   --report Usuário x enviou mensagem ofensiva
   ```

   Isso armazenará o relatório em um arquivo, incluindo a data, quem reportou e o que foi reportado.

## Contribuição

Contribuições são bem-vindas! Para contribuir com o projeto, siga estes passos:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça as alterações necessárias e commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
5. Crie um Pull Request no GitHub.


## Contato

Para dúvidas ou suporte adicional, entre em contato com [E-mail](mailto:ledu64816@gmail.com).


### Explicação das Seções

- **Descrição e Funcionalidades:** Apresenta o objetivo do projeto e as principais funcionalidades.
- **Requisitos:** Lista o que é necessário para executar o projeto.
- **Instalação e Configuração:** Passos para clonar, compilar e executar o servidor e cliente.
- **Comandos:** Descrição dos comandos suportados e exemplos de uso.
- **Exemplo de Uso:** Exemplos práticos de como interagir com a aplicação.
- **Contribuição:** Orientações para quem deseja contribuir com o projeto.
- **Licença e Contato:** Informações sobre a licença e como entrar em contato para suporte.

Você pode personalizar os links e informações de contato conforme necessário. Se precisar de mais detalhes ou ajustes, estou aqui para ajudar!

## ⚠️ Importante

Antes de começar, certifique-se de revisar os seguintes pontos:

- Verifique se todas as dependências estão instaladas.
- Configure o `SERVER_IP` corretamente no código do cliente.
- Siga os passos de instalação e configuração com atenção.
