/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 12
 *  Mostrar los números impares del 60 al 30 en forma descendente.
 * ==================================================
 */

package com.example;

public class Ejercicio12 {
public static void main(String[] args) {
        for (int i = 60; i >=30; i--) {
            if (i % 2 != 0) {
                System.out.println(i);
            }
        }
    }
}
