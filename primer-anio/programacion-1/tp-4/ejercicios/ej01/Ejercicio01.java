package com.facundoluna;

public class Ejercicio01 {
    private int IdPersona;
    private int Dni;
    private String Apellido;
    private String Nombre;
    private int Edad;
    private String Genero;
    private double Peso;
    private double Altura;
    private String Domicilio;

    public Ejercicio01(int idPersona, int dni, String apellido, String nombre, int edad, String genero, double peso,
            double altura, String domicilio) {
        IdPersona = idPersona;
        Dni = dni;
        Apellido = apellido;
        Nombre = nombre;
        Edad = edad;
        Genero = genero;
        Peso = peso;
        Altura = altura;
        Domicilio = domicilio;
    }

    @Override
    public String toString() {
        return "\n--- Persona #" + IdPersona + " ---\n" +
                "DNI: " + Dni + "\n" +
                "Nombre: " + Nombre + " " + Apellido + "\n" +
                "Edad: " + Edad + " años | Género: " + Genero + "\n" +
                "Peso: " + Peso + " kg | Altura: " + Altura + " m\n" +
                "Domicilio: " + Domicilio + "\n";
    }

}
