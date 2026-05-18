/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 14
 *  Mostrar los múltiplos de 5 desde el 1 al 100. (usar mod)
 * ==================================================
 */

package com.example;

public class Ejercicio14 {
    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            if (i % 5 == 0) {
                System.out.println(i);
            }
        }
    }
}
