package com.example;

import java.util.Scanner;

/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 5
 * Solicitar al usuario el ingreso de la nota del Examen. Luego mostrar 'Promocionado' (7 a 10),
 * 'Regular' (4 a 6) o 'Libre' (0 a 3) según la nota ingresada.
 * ==================================================
 */
public class Ejercicio05 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {

            System.out.print("Ingrese la calificación del examen: ");
            if (!scanner.hasNextInt()) {
                System.out.println("Error: el tipo de dato ingresado no es válido.");
                return;
            }

            int calificacion = scanner.nextInt();

            if (calificacion < 0 || calificacion > 10) {
                System.out.println("Error: calificacion no válida.");
                return;
            }

            if (calificacion >= 7 && calificacion <= 10) {
                System.out.println("Promocionado");
            } else if (calificacion >= 4 && calificacion <= 6) {
                System.out.println("Regular");
            } else {
                System.out.println("Libre");
            }
        }
    }
}