/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 2
 * Solicitar al usuario el ingreso de dos números, calcular y mostrar el promedio de ambos valores.
 * ==================================================
 */

package com.example;

import java.util.Scanner;

public class Ejercicio02 {
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

            double prom = (num1 + num2)/2;
            System.out.printf("El promedio de %.2f y %.2f es: %.2f%n", num1, num2, prom);

        } // libera el recurso del sistema al terminar
    }
}
