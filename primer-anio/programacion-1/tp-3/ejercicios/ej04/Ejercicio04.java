/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 4
 * Solicitar al usuario el ingreso de su edad.
 * Luego mostrar por pantalla: 'Eres mayor de edad' o 'No eres mayor de edad' según la edad ingresada
 * (18 años cumplidos para ser mayor de edad) 
 * ==================================================
 */

package com.example;

import java.util.Scanner;

public class Ejercicio04 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingrese su edad: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: el tipo de dato ingresado no es válido.");
                return;
            }

            int edad = scanner.nextInt();
            if (edad <= 0) {
                System.out.println("Error: la edad debe ser un número positivo.");
                return;
            }

            System.out.print(edad >= 18 ? "Eres mayor de edad." : "No eres mayor de edad.");
        }
    }
}
