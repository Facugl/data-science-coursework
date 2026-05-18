package com.facundoluna;
 
import java.util.Scanner;
 
public class Ejercicio10 {
    public static void main(String[] args) {
 
        Scanner scanner = new Scanner(System.in);
 
        System.out.println("=== Adivina el numero ===\n");
        System.out.println("Pense un numero entre 1 y 100. Podes adivinarlo?\n");
 
        int numeroSecreto = 42;
        int intentos = 0;
        int maxIntentos = 7;
        boolean adivinado = false;
 
        while (intentos < maxIntentos && !adivinado) {
 
            System.out.print("Intento " + (intentos + 1) + "/" 
                             + maxIntentos + " -> Tu numero: ");
 
            // hasNextInt() verifica que el token sea un entero antes de leerlo
            if (!scanner.hasNextInt()) {
                System.out.println("Ingresa un numero valido.");
                scanner.nextLine(); // descarta la entrada invalida
                continue;
            }
 
            int intento = scanner.nextInt();
            intentos++;
 
            if (intento < numeroSecreto) {
                System.out.println("Muy bajo.\n");
            } else if (intento > numeroSecreto) {
                System.out.println("Muy alto.\n");
            } else {
                adivinado = true;
            }
        }
 
        if (adivinado) {
            System.out.println("Correcto! Lo adivinaste en " 
                               + intentos + " intentos.");
        } else {
            System.out.println("Te quedaste sin intentos. "
                               + "El numero era " + numeroSecreto + ".");
        }
 
        // Se cierra el Scanner al finalizar, como indica la documentacion
        scanner.close();
    }
}