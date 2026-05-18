package com.facundoluna;

public class Profesor extends PersonaConMetodos {
    public String Materia;
    public int CargaHoraria;

    public Profesor(int idPersona, int dni, String apellido, String nombre, int edad, String genero, double peso,
            double altura, String domicilio, String materia, int cargaHoraria) {
        super(idPersona, dni, apellido, nombre, edad, genero, peso, altura, domicilio);
        Materia = materia;
        CargaHoraria = cargaHoraria;
    }
}
