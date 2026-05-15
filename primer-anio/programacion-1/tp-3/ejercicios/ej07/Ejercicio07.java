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
