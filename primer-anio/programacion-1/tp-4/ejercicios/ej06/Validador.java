package com.facundoluna;

import java.util.Scanner;

public class Validador {

    public static String leerTexto(Scanner scanner, String mensaje, String regex) {
        while (true) {
            System.out.print(mensaje);
            String input = scanner.nextLine().trim();
            if (!input.isEmpty() && input.matches(regex)) return input;
            System.out.println("Error: entrada inválida.");
        }
    }

    public static int leerEntero(Scanner scanner, String mensaje, int min, int max) {
        while (true) {
            System.out.print(mensaje);
            try {
                int valor = Integer.parseInt(scanner.nextLine().trim());
                if (valor >= min && valor <= max) return valor;
                System.out.println("Error: ingrese un valor entre " + min + " y " + max + ".");
            } catch (NumberFormatException e) {
                System.out.println("Error: ingrese un número entero válido.");
            }
        }
    }

    public static double leerDecimal(Scanner scanner, String mensaje, double min, double max) {
        while (true) {
            System.out.print(mensaje);
            try {
                double valor = Double.parseDouble(scanner.nextLine().trim());
                if (valor >= min && valor <= max) return valor;
                System.out.println("Error: ingrese un valor entre " + min + " y " + max + ".");
            } catch (NumberFormatException e) {
                System.out.println("Error: ingrese un número decimal válido.");
            }
        }
    }
}