/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 13
 *  Mostrar la tabla de multiplicar del 6 (Ej. 6x1=6; 6x2=12; 6x3=18, etc.)
 * ==================================================
 */

package com.example;

public class Ejercicio13 {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            System.out.printf("6 x %d = %d%n", i, 6 * i);
        }
    }
}
