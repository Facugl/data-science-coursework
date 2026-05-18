package com.facundoluna;

import java.util.List;

public class Ejercicio04 {
    public static void main(String[] args) {
        Ejercicio03 ej03 =  new Ejercicio03();

        List<Persona> personas = ej03.cargarPersonas();
        
        System.out.println("=== EJERCICIO 4 ===\n");
        personas.forEach(System.out::println);
    }

}
