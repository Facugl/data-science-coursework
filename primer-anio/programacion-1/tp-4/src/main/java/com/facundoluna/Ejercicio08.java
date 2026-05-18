package com.facundoluna;

public class Ejercicio08 {
    public Profesor[] cargarProfesores() {
        Profesor[] profesores = new Profesor[10]; // Para tener dimension fija

        profesores[0] = new Profesor(1, 28456789, "García", "Martín", 45, "Masculino", 78.5, 1.75,
                "Av. Corrientes 1234, CABA", "Matemática", 20);
        profesores[1] = new Profesor(2, 31245678, "López", "Verónica", 38, "Femenino", 62.0, 1.63,
                "Calle San Martín 456, Rosario", "Lengua", 18);
        profesores[2] = new Profesor(3, 25678901, "Romero", "Alejandro", 52, "Masculino", 90.3, 1.80,
                "Belgrano 789, Córdoba", "Historia", 24);
        profesores[3] = new Profesor(4, 34567890, "Fernández", "Laura", 29, "Femenino", 55.8, 1.58,
                "Mitre 321, Mendoza", "Biología", 16);
        profesores[4] = new Profesor(5, 27890123, "Torres", "Ricardo", 47, "Masculino", 83.2, 1.72,
                "Rivadavia 654, Mar del Plata", "Física", 22);
        profesores[5] = new Profesor(6, 36789012, "Gómez", "Sofía", 33, "Femenino", 68.4, 1.67,
                "Sarmiento 987, Tucumán", "Química", 20);
        profesores[6] = new Profesor(7, 23456789, "Díaz", "Pablo", 55, "Masculino", 74.0, 1.68,
                "Pueyrredón 147, La Plata", "Educación Física", 30);
        profesores[7] = new Profesor(8, 39012345, "Ruiz", "Camila", 26, "Femenino", 57.5, 1.61,
                "Independencia 258, Salta", "Inglés", 12);
        profesores[8] = new Profesor(9, 29345678, "Moreno", "Diego", 41, "Masculino", 88.6, 1.78,
                "Libertad 369, Paraná", "Geografía", 18);
        profesores[9] = new Profesor(10, 32456789, "Perez", "Natalia", 36, "Femenino", 60.1, 1.65,
                "Colón 741, Santiago del Estero", "Tecnología", 14);

        return profesores;
    }
}
