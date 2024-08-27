import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class ClientHandler extends Thread {
    private Socket socket;
    private PrintWriter out;
    private BufferedReader in;
    private static Map<Socket, String> clientNames = new HashMap<>();

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    public void run() {
        try {
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);

            // Define o nome padrão para o cliente
            clientNames.put(socket, "Usuário");

            String message;
            while ((message = in.readLine()) != null) {
                if (message.startsWith("--user")) {
                    // Comando para alterar o nome do usuário
                    String newName = message.substring(7).trim();
                    clientNames.put(socket, newName);
                    broadcast("Nome alterado para: " + newName);
                } else {
                    // Envia a mensagem para todos os clientes
                    String prefix = clientNames.get(socket);
                    broadcast(prefix + " >> " + message);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                socket.close();
                clientNames.remove(socket);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private void broadcast(String message) {
        // Envia a mensagem para todos os clientes conectados
        for (Socket clientSocket : clientNames.keySet()) {
            try {
                PrintWriter clientOut = new PrintWriter(clientSocket.getOutputStream(), true);
                clientOut.println(message);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
