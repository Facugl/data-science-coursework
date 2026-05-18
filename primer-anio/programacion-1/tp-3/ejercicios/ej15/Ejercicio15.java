/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 15
 * Solicitar 5 números al usuario. Luego mostrar: la suma total de todos los números y el producto de todos los números. 
 * ==================================================
 */

package com.example;

import java.util.Scanner;

public class Ejercicio15 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingrese el primer número: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double num1 = scanner.nextDouble();

            System.out.print("Ingrese el segundo número: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double num2 = scanner.nextDouble();

            System.out.print("Ingrese el tercer número: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double num3 = scanner.nextDouble();

            System.out.print("Ingrese el cuarto número: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double num4 = scanner.nextDouble();

            System.out.print("Ingrese el quinto número: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double num5 = scanner.nextDouble();

            double suma = num1 + num2 + num3 + num4 + num5;
            double producto = num1 * num2 * num3 * num4 * num5;
            System.out.println("La suma de de los 5 números es: " + suma);
            System.out.println("La producto de de los 5 números es: " + producto);
        }
    }
}
