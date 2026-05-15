package com.example;

import java.util.Scanner;

public class Ejercicio08 {
public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingrese un número entero: ");
            if (!scanner.hasNextInt()) {
                System.out.println("Error: el numero ingresado no es válido.");
                return;
            }
            int number = scanner.nextInt();
            
            if (number % 2 == 0) {
                System.out.println(number + " es par.");
            } else {
                System.out.println(number + " no es par.");
            }
        }
    }
}
