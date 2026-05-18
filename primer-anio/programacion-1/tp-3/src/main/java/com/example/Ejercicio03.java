/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 3
 * Solicitar al usuario el ingreso de la BASE y la ALTURA de un triángulo, calcular y mostrar el área del triángulo. 
 * ==================================================
 */

package com.example;

import java.util.Scanner;

public class Ejercicio03 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {

            System.out.print("Ingrese la base del triángulo: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double base = scanner.nextDouble();
            if (base <= 0) {
                System.out.println("Error: la base debe ser un número positivo.");
                return;
            }

            System.out.print("Ingrese la altura del triángulo: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double altura = scanner.nextDouble();
            if (altura <= 0) {
                System.out.println("Error: la altura debe ser un número positivo.");
                return;
            }

            double area = (base * altura) / 2;
            System.out.printf("El área del triágulo es: %.2f%n unidades cuadradas", area);

        }
    }
}
