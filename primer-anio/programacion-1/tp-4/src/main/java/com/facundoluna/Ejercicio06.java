package com.facundoluna;

import java.util.Scanner;

public class Ejercicio06 {
    public static void main(String[] args) {
        System.out.println("=== EJERCICIO 6 - REGISTRO DE PERSONAS ===\n");

        try (Scanner scanner = new Scanner(System.in)) {
            for (int i = 1; i <= 3; i++) {
                System.out.println("\n--- PERSONA " + i + " ---");

                String dni = Validador.leerTexto(scanner,
                        "Ingrese el DNI: ", "\\d{7,8}");

                String nombre = Validador.leerTexto(scanner,
                        "Ingrese el nombre: ", "[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+");

                String apellido = Validador.leerTexto(scanner,
                        "Ingrese el apellido: ", "[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+");

                int edad = Validador.leerEntero(scanner,
                        "Ingrese la edad: ", 0, 120);

                String genero = Validador.leerTexto(scanner,
                        "Ingrese el género (Masculino/Femenino/Otro): ",
                        "(?i)masculino|femenino|otro");

                double peso = Validador.leerDecimal(scanner,
                        "Ingrese el peso (kg): ", 1.0, 500.0);

                double altura = Validador.leerDecimal(scanner,
                        "Ingrese la altura (metros): ", 0.3, 3.0);

                String domicilio = Validador.leerTexto(scanner,
                        "Ingrese el domicilio: ", ".+");

                PersonaConMetodos persona = new PersonaConMetodos(
                        i,
                        Integer.parseInt(dni),
                        apellido,
                        nombre,
                        edad,
                        genero,
                        peso,
                        altura,
                        domicilio);

                System.out.println("\n" + persona.info());
                System.out.println(persona.esMayorDeEdad() ? "Es mayor de edad." : "No es mayor de edad.");
                System.out.println("IMC: " + persona.IMC());
            }
        }
    }
}