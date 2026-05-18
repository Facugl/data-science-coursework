package com.facundoluna;

public class PersonaConMetodos {
    private int IdPersona;
    private int Dni;
    private String Apellido;
    private String Nombre;
    private int Edad;
    private String Genero;
    private double Peso;
    private double Altura;
    private String Domicilio;

    public PersonaConMetodos(int idPersona, int dni, String apellido, String nombre, int edad, String genero, double peso,
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

    public String info() {
        return "Nombre: " + Nombre + " " + Apellido + ", DNI: " + Dni + ", Dirección: " + Domicilio;
    }

    public String IMC() {
        double IMC = Peso / (Altura*Altura);
        if (IMC > 25) {
            return "Sobrepeso.";
        } else if (IMC >= 20 && IMC <= 25) {
            return "Está en su peso ideal.";
        } else {
            return "Debajo de su peso ideal.";
        }
    }

    public Boolean esMayorDeEdad() {
        return Edad >= 18 ? true : false;
    }

}
