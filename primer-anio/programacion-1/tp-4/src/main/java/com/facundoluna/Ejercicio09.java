package com.facundoluna;

public class Ejercicio09 {
    public static void main(String[] args) {
        Ejercicio08 ej08 =  new Ejercicio08();

        Profesor[] profesores = ej08.cargarProfesores();
        
        System.out.println("=== EJERCICIO 9 ===\n");
        for (Profesor profesor : profesores) {
            if (profesor.CargaHoraria > 10) {
                System.out.println(profesor.info() + ", Materia: " + profesor.Materia + ", Carga Horaria: " + profesor.CargaHoraria + "hs");
            }
        }
    }
}
