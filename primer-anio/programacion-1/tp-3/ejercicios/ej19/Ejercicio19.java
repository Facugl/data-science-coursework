/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 19
 * Mostrar la tabla de multiplicar del 6 (Ej. 6x1=6; 6x2=12; 6x3=18, etc.)
 * ==================================================
 */

package com.example;

public class Ejercicio19 {
    public static void main(String[] args) {
        int i = 1;
        while (i <= 10) {
            System.out.println("6 x " + i + " = " + 6 * i);
            i++;
        }
    }
}
