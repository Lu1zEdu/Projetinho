import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class JogoDaForca {
    public static void main(String[] args) {
        jogarForca();
    }

    public static String escolherPalavra() {
        String[] palavras = {
                "python", "desenvolvimento", "computador", "programacao", "internet",
                "javascript", "algoritmo", "variavel", "funcao", "objeto",
                "classe", "framework", "biblioteca", "software", "hardware",
                "tecnologia", "inteligencia", "artificial", "navegador", "servidor",
                "cliente", "aplicativo", "rede", "criptografia", "seguranca",
                "dados", "informacao", "sistema", "operacional", "memoria",
                "processador", "arquitetura", "sintaxe", "compilador", "interpretador"
        };
        Random random = new Random();
        return palavras[random.nextInt(palavras.length)];
    }

    public static void displayJogo(String palavra, List<Character> letrasCorretas) {
        StringBuilder display = new StringBuilder();
        for (char letra : palavra.toCharArray()) {
            if (letrasCorretas.contains(letra)) {
                display.append(letra).append(" ");
            } else {
                display.append("_ ");
            }
        }
        System.out.println(display.toString().trim());
    }

    public static void desenharForca(int tentativas) {
        String[] estagios = {
                """
               -----
               |   |
               |   O
               |  /|\\
               |  / \\
               |
            --------
            """,
                """
               -----
               |   |
               |   O
               |  /|\\
               |  / 
               |
            --------
            """,
                """
               -----
               |   |
               |   O
               |  /|\\
               |  
               |
            --------
            """,
                """
               -----
               |   |
               |   O
               |  /|
               |  
               |
            --------
            """,
                """
               -----
               |   |
               |   O
               |   |
               |  
               |
            --------
            """,
                """
               -----
               |   |
               |   O
               |   
               |  
               |
            --------
            """,
                """
               -----
               |   |
               |   
               |   
               |  
               |
            --------
            """
        };
        System.out.println(estagios[6 - tentativas]);
    }

    public static void jogarForca() {
        String palavra = escolherPalavra();
        List<Character> letrasCorretas = new ArrayList<>();
        List<Character> letrasErradas = new ArrayList<>();
        int tentativas = 6;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Bem-vindo ao jogo da Forca!");

        while (tentativas > 0) {
            limparTela();
            desenharForca(tentativas);
            displayJogo(palavra, letrasCorretas);
            System.out.println("Tentativas restantes: " + tentativas);
            System.out.print("Letras erradas: ");
            for (char letra : letrasErradas) {
                System.out.print(letra + " ");
            }
            System.out.println();

            System.out.print("Digite uma letra: ");
            char chute = scanner.next().toLowerCase().charAt(0);

            if (letrasCorretas.contains(chute) || letrasErradas.contains(chute)) {
                System.out.println("Você já escolheu essa letra. Tente outra.");
                continue;
            }

            if (palavra.indexOf(chute) >= 0) {
                letrasCorretas.add(chute);
                System.out.println("Boa! A letra '" + chute + "' está na palavra.");
            } else {
                letrasErradas.add(chute);
                tentativas--;
                System.out.println("A letra '" + chute + "' não está na palavra.");
            }

            if (palavra.chars().allMatch(c -> letrasCorretas.contains((char) c))) {
                System.out.println("Parabéns! Você adivinhou a palavra: " + palavra);
                break;
            }
        }

        if (tentativas == 0) {
            desenharForca(tentativas);
            System.out.println("Você perdeu! A palavra era: " + palavra);
        }
        scanner.close();
    }

    public static void limparTela() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                Runtime.getRuntime().exec("clear");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
