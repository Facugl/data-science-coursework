/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 7
 * Escribir un programa que solicite un número, luego le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final por pantalla.
 * ==================================================
 */

package com.example;

import java.util.Scanner;

public class Ejercicio07 {
public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingrese un número: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: el dato ingresado no es válido.");
                return;
            }
            Double number = scanner.nextDouble();
            
            System.out.println("El número resultante luego de restar el 15% es: " + (0.85 * number));
        }
    }
}
