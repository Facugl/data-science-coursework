package com.example;

import java.util.Scanner;

public class Ejercicio01 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {

            System.out.print("Ingrese el primer número: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double num1 = scanner.nextDouble(); // nextDouble acepta decimales y enteros

            System.out.print("Ingrese el segundo número: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double num2 = scanner.nextDouble(); // nextDouble acepta decimales y enteros

            double suma = num1 + num2;
            System.out.printf("La suma de %.2f y %.2f es: %.2f%n", num1, num2, suma);

        } // libera el recurso del sistema al terminar
    }
}
