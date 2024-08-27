import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ChatWindow extends JFrame {
    private JTextArea textArea;
    private JTextField textField;
    private ChatManager chatManager;
    private String userName; // Nome do usuário
    private String userPrefix; // Prefixo do usuário no chat

    public ChatWindow() {
        // Configurações da janela
        setTitle("Terminal Chat");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Inicializa o nome do usuário
        userName = "Usuário"; // Defina um nome padrão ou adicione uma lógica para definir
        userPrefix = "> " + userName + " >> "; // Define o prefixo inicial

        // Cria o chat manager
        chatManager = new ChatManager();

        // Configura a área de texto para exibir mensagens
        textArea = new JTextArea(20, 50);
        textArea.setEditable(false);
        textArea.setFont(new Font("Monospaced", Font.PLAIN, 12));
        textArea.setBackground(Color.BLACK);
        textArea.setForeground(Color.GREEN);
        add(new JScrollPane(textArea), BorderLayout.CENTER);

        // Configura o campo de texto para entrada de mensagens
        textField = new JTextField(50);
        textField.setBackground(Color.BLACK);
        textField.setForeground(Color.GREEN);
        textField.setCaretColor(Color.GREEN); // Define a cor do cursor para combinar com o texto
        add(textField, BorderLayout.SOUTH);

        // Adiciona um listener para o campo de texto
        textField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String input = textField.getText();
                if (!input.trim().isEmpty()) {
                    processInput(input);
                    textField.setText("");
                }
            }
        });
    }

    // Método para processar a entrada e executar comandos
    private void processInput(String input) {
        if (input.startsWith("--")) {
            String[] parts = input.substring(2).split(" ", 2); // Divide o comando e os argumentos
            String command = parts[0].toLowerCase();
            String arguments = parts.length > 1 ? parts[1] : "";

            switch (command) {
                case "help":
                case "h":
                    displayMessage(
                            "Comandos disponíveis:\n" +
                                    " --help ou --h = Alguma ajuda para os códigos\n" +
                                    " --clear ou --c = Apaga todas as mensagens\n" +
                                    " --user ou --u = Trocar de nome de usuário\n" +
                                    " --report ou --r = Reportar algum usuário para o admin\n" +
                                    " --exit ou --e = Sair"
                    );
                    break;
                case "clear":
                case "c":
                    textArea.setText("");
                    break;
                case "user":
                case "u":
                    String newUserName = arguments.trim();
                    if (!newUserName.isEmpty()) {
                        userName = newUserName;
                        userPrefix = "> " + userName + " >> "; // Atualiza o prefixo do usuário
                        displayMessage("Nome de usuário alterado para: " + userName);
                    } else {
                        displayMessage("Por favor, forneça um novo nome de usuário.");
                    }
                    break;
                case "report":
                case "r":
                    saveReport(arguments);
                    displayMessage("Relatório enviado: " + arguments);
                    break;
                case "exit":
                case "e":
                    displayMessage("Saindo...");
                    System.exit(0); // Fecha a aplicação
                    break;
                default:
                    displayMessage("Comando desconhecido: " + command);
                    break;
            }
        } else {
            // Se não é um comando, apenas adiciona a mensagem ao chat
            chatManager.sendMessage(input, userName);
            textArea.append(userPrefix + input + "\n"); // Usa o prefixo atualizado
        }
    }

    // Método para salvar o relatório em um arquivo
    private void saveReport(String reportContent) {
        String fileName = "reports.txt";
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, true))) {
            String timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
            writer.write("Data: " + timestamp);
            writer.newLine();
            writer.write("Reportado por: " + userName);
            writer.newLine();
            writer.write("Conteúdo: " + reportContent);
            writer.newLine();
            writer.write("--------------------------------------------------");
            writer.newLine();
        } catch (IOException e) {
            displayMessage("Erro ao salvar o relatório: " + e.getMessage());
        }
    }

    public void displayMessage(String message) {
        textArea.append(message + "\n");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            ChatWindow chatWindow = new ChatWindow();
            chatWindow.setVisible(true);
        });
    }
}
