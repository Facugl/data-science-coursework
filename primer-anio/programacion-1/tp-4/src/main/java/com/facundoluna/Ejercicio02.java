package com.facundoluna;

public class Ejercicio02 {
    public static void main(String[] args) {

        // Creo 5 instancias de la clase Persona
        Persona persona1 = new Persona(1, 11111111, "Pérez", "Juan", 30, "Masculino", 70.5, 1.75, "Calle Falsa 123");
        Persona persona2 = new Persona(2, 22222222, "González", "María", 25, "Femenino", 60.0, 1.65,
                "Av. Siempre Viva 456");
        Persona persona3 = new Persona(3, 33333333, "López", "Carlos", 45, "Masculino", 85.0, 1.80, "Belgrano 789");
        Persona persona4 = new Persona(4, 44444444, "Martínez", "Ana", 28, "Femenino", 55.5, 1.60, "San Martín 321");
        Persona persona5 = new Persona(5, 55555555, "Rodríguez", "Pedro", 35, "Masculino", 78.0, 1.72, "Sarmiento 654");

        // Las muestro por consola
        System.out.println(persona1);
        System.out.println(persona2);
        System.out.println(persona3);
        System.out.println(persona4);
        System.out.println(persona5);
    }
}
