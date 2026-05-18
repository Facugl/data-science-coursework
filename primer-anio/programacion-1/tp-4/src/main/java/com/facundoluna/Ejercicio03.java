package com.facundoluna;

import java.util.ArrayList;
import java.util.List;

public class Ejercicio03 {
    public List<Persona> cargarPersonas() {
        List<Persona> personas = new ArrayList<>();

        personas.add(new Persona(1, 11111111, "Pérez", "Juan", 30, "Masculino", 70.5, 1.75, "Calle Falsa 123"));
        personas.add(new Persona(2, 22222222, "González", "María", 25, "Femenino", 60.0, 1.65, "Av. Siempre Viva 456"));
        personas.add(new Persona(3, 33333333, "López", "Carlos", 45, "Masculino", 85.0, 1.80, "Belgrano 789"));
        personas.add(new Persona(4, 44444444, "Martínez", "Ana", 28, "Femenino", 55.5, 1.60, "San Martín 321"));
        personas.add(new Persona(5, 55555555, "Rodríguez", "Pedro", 35, "Masculino", 78.0, 1.72, "Sarmiento 654"));
        personas.add(new Persona(6, 66666666, "Fernández", "Laura", 32, "Femenino", 62.5, 1.68, "Mitre 987"));
        personas.add(new Persona(7, 77777777, "García", "Roberto", 50, "Masculino", 90.0, 1.78, "Rivadavia 234"));
        personas.add(new Persona(8, 88888888, "Díaz", "Sofía", 22, "Femenino", 58.0, 1.62, "Córdoba 567"));
        personas.add(new Persona(9, 99999999, "Romero", "Diego", 38, "Masculino", 82.5, 1.76, "Tucumán 890"));
        personas.add(new Persona(10, 10101010, "Torres", "Valentina", 29, "Femenino", 64.0, 1.70, "Santa Fe 432"));

        return personas;
    }
}