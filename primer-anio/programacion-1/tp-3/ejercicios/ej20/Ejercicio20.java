package com.example;

import java.util.Scanner;

public class Ejercicio20 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {

            System.out.print("Ingrese el número desde el cual quieres comenzar a contar: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double n = scanner.nextDouble();

            System.out.print("Ingrese el número hasta el cual quieras contar: ");
            if (!scanner.hasNextDouble()) {
                System.out.println("Error: debe ingresar un número válido.");
                return;
            }
            double p = scanner.nextDouble();

            while (n <= p) {
                System.out.println(n);
                n++;
            }
        }
    }
}
