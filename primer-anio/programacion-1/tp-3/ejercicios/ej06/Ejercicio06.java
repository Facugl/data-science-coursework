/*
 * UCASAL - PROGRAMACION I
 * Autor: Luna Facundo
 * ==========================
 * EJERCICIO 6
 * Solicitar al usuario los datos de inicio de sesión, como lo son Nombre de Usuario y Contraseña.
 * Luego validar los datos ingresados.
 * - Si el nombre es 'Franco' y la contraseña '2022', mostrar 'Bienvenido Franco!
 * Inicio de sesión válido!''.
 * - Si alguno de los datos es incorrecto, mostrar el mensaje que corresponda: 'Nombre
 * de usuario incorrecto, no se puede iniciar sesión!' o 'Contraseña incorrecta, no se
 * puede iniciar sesión!'.
 * - Si ambos datos sin incorrectos, mostrar el mensaje 'Usuario totalmente
 * desconocido! Fuera hacker!!''.
 * ==================================================
 */

package com.example;

import java.util.Scanner;

public class Ejercicio06 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingrese su nombre de usuario: ");
            String userName = scanner.nextLine();
            if (userName.isBlank()) {
                System.out.println("Error: el nombre de usuario no puede estar vacío.");
                return;
            }

            System.out.print("Ingrese su contraseña: ");
            String password = scanner.nextLine();
            if (password.isBlank()) {
                System.out.println("Error: la contraseña no puede estar vacía.");
                return;
            }

            String userNameFromDB = "Franco"; // Esto vendría desde una Base de Datos
            String passwordFromDB = "2022"; // De igual manera, esto estaría encriptado en la DB

            if (userName.equals(userNameFromDB)) {
                if (password.equals(passwordFromDB)) {
                    System.out.println("Bienvenido Franco! Inicio de sesión válido!");
                } else {
                    System.out.println("Contraseña incorrecta no se puede iniciar sesion!");
                }
            } else {
                if (password.equals(passwordFromDB)) {
                    System.out.println("Nombre de usuario incorrecto, no se puede iniciar sesión!");
                } else {
                    System.out.println("Usuario totalmente desconocido! Fuera hacker!!");
                }
            }
        }
    }
}
