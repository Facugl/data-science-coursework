package utilidades;

import java.util.Scanner;

public class Consola {
    private static final String SEPARADOR ="=".repeat(70);
    private static final String COLOR_OK = "\u001B[32m"; // Verde
    private static final String COLOR_ERROR = "\u001B[31m"; // Rojo
    private static final String COLOR_INFO = "\u001B[36m"; // Cian
    private static final String COLOR_RESET = "\u001B[0m";

    private Consola() {
    }

    public static void separador() {
        System.out.println(SEPARADOR);
    }

    public static void titulo(String texto) {
        System.out.println();
        separador();
        System.out.printf("%s%n", texto.toUpperCase());
        separador();
    }

    public static void subtitulo(String texto) {
        System.out.println();
        System.out.println("\\textgreater\\textgreater{} " + texto);
        System.out.println("-".repeat(50));
    }

    public static void exito(String mensaje) {
        System.out.println(COLOR_OK + "[OK]" + mensaje + COLOR_RESET);
    }

    public static void error(String mensaje) {
        System.out.println(COLOR_ERROR + "[ERROR]" + mensaje + COLOR_RESET);
    }

    public static void info(String mensaje) {
        System.out.println(COLOR_INFO + "[INFO]" + mensaje + COLOR_RESET);
    }

    // Lee un número entero y valida el formato
    public static int leerEntero(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt + ": ");
            try {
                int valor = Integer.parseInt(scanner.nextLine().trim());
                return valor;
            } catch (NumberFormatException e) {
                error("Ingrese un número válido.");
            }
        }
    }

    // Lee un número decimal, valida el formato y que sea positivo
    public static double leerDouble(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt + ": $");
            try {
                double valor = Double.parseDouble(scanner.nextLine().trim().replace(",", "."));
                if (valor < 0) {
                    error("El valor debe ser positivo.");
                } else {
                    return valor;
                }
            } catch (NumberFormatException e) {
                error("Ingrese un monto válido (ej: 1500.50).");
            }
        }
    }
}
