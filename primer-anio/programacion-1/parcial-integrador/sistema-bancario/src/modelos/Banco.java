
package modelos;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class Banco {
    private final String nombre;
    private final String cbu;
    private int contadorCuentas;
    private final List<Cliente> clientes;
    private final List<Cuenta> cuentas;

    public Banco(String nombre, String cbu) {
        this.nombre = nombre;
        this.cbu = cbu;
        this.contadorCuentas = 1000;
        this.clientes = new ArrayList<>();
        this.cuentas = new ArrayList<>();
    }

    // Registra un nuevo cliente si el DNI no existe
    public boolean registrarCliente(Cliente cliente) {
        if (buscarClientePorDni(cliente.getDni()).isPresent()) {
            return false; // ya existe
        }
        clientes.add(cliente);
        return true;
    }

    // Se emplea Optional para el manejo seguro de null
    public Optional<Cliente> buscarClientePorDni(String dni) {
        return clientes.stream()
                .filter(c -> c.getDni().equals(dni))
                .findFirst();
    }

    // Genera un número de cuenta único y secuencial
    public String generarNumeroCuenta() {
        return "CBU-" + (++contadorCuentas);
    }

    // Registra una cuenta en el banco y la asocia al titular
    public void registrarCuenta(Cuenta cuenta) {
        cuentas.add(cuenta);
        cuenta.getTitular().agregarCuenta(cuenta);
    }

    // Con Stream convierto en un flujo de datos y filtro la primera coincidencia
    public Optional<Cuenta> buscarCuenta(String numeroCuenta) {
        return cuentas.stream()
                .filter(c -> c.getNumeroCuenta().equals(numeroCuenta))
                .findFirst();
    }

    public int totalClientes() {
        return clientes.size();
    }

    public int totalCuentas() {
        return cuentas.size();
    }

    public String getNombre() {
        return nombre;
    }

    public String getCbu() {
        return cbu;
    }

    public List<Cliente> getClientes() {
        return clientes;
    }

    public List<Cuenta> getCuentas() {
        return cuentas;
    }

    @Override
    public String toString() {
        return String.format("Banco: %s | CBU: %s | Clientes: %d | Cuentas: %d",
                nombre, cbu, clientes.size(), cuentas.size());
    }
}
