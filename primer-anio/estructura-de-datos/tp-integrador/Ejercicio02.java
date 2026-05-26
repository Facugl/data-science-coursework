import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Ejercicio02 {
    public static void main(String[] args) {
        // lista hardcodeada por simplicidad
        Object[] list = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        
        for (Object elemento : list) {
            // no reservo memoria si hay un elemento inválido
            if (!(elemento instanceof Integer)) {
                System.out.println("Error: '" + elemento + "' no es un número entero.");
                return;
            }
        }

        Integer suma = 0;
        // tipo Deque (interfaz) para no acoplar el código a una implementación
        Deque<Integer> pila = new ArrayDeque<>();
        Deque<Integer> cola = new ArrayDeque<>();

        for (Object elemento : list) {
            Integer numero = (Integer) elemento;
            (numero % 2 == 0 ? pila : cola).add(numero);
        }

        System.out.println("item a)");
        System.out.println("Lista original: " + Arrays.toString(list));
        System.out.println("Pila Auxiliar (pares):   " + pila);
        System.out.println("Cola Auxiliar (impares): " + cola);

        for (Integer par : pila) {
            suma += par; // acumulo para luego dividir por el tamaño de la pila
        }

        System.out.println("item b)");
        System.out.println("El Promedio de la Pila Auxiliar es: "
                + (suma / (double) pila.size()));
    }
}