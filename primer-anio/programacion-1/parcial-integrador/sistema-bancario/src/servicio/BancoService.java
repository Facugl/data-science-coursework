package servicio;

import java.util.Optional;

import modelos.Banco;
import modelos.CajaDeAhorro;
import modelos.Cliente;
import modelos.Cuenta;
import modelos.CuentaCorriente;
import utilidades.Consola;

// Esta clase es intermediaria entre el menú y el modelo
public class BancoService {
    private final Banco banco;

    public BancoService() {
        this.banco = new Banco("Banco Universitario S.A.", "0000003100073007020183");
    }

    // Registra un nuevo cliente en el sistema
    public void registrarCliente(String nombre, String apellido, String dni, String email) {
        Cliente cliente = new Cliente(nombre, apellido, dni, email);

        if (banco.registrarCliente(cliente)) {
            Consola.exito("Cliente registrado: " + cliente.getNombreCompleto());
        } else {
            Consola.error("Ya existe un cliente con DNI: " + dni);
        }
    }

    // Listamos todos los clientes registrados en el banco
    public void listarClientes() {
        Consola.subtitulo("Clientes Registrados");
        if (banco.getClientes().isEmpty()) {
            Consola.info("No hay clientes registrados.");
            return;
        }

        banco.getClientes().forEach(System.out::println);

        Consola.info("Total: " + banco.totalClientes() + " cliente(s).");
    }

    // Busca y muestra un cliente por su DNI
    public void buscarClientePorDni(String dni) {
        banco.buscarClientePorDni(dni).ifPresentOrElse(
                cliente -> {
                    System.out.println(cliente);
                    cliente.getCuentas().forEach(System.out::println);
                },
                () -> Consola.error("No se encontró cliente con DNI: " + dni));
    }

    // Abre una Caja de Ahorro para el cliente con el DNI que se pasa
    public void abrirCajaDeAhorro(String dni, double saldoInicial) {
        Optional<Cliente> clienteOptional = banco.buscarClientePorDni(dni);

        if (clienteOptional.isEmpty()) {
            Consola.error("No existe cliente con DNI: " + dni);
            return;
        }

        String numeroDeCuenta = banco.generarNumeroCuenta();
        CajaDeAhorro cuenta = new CajaDeAhorro(numeroDeCuenta, saldoInicial, clienteOptional.get());
        banco.registrarCuenta(cuenta);

        Consola.exito("Caja de Ahorro abierta. Número: " + numeroDeCuenta);
    }

    // Abre una Cuenta Corriente para el cliente con el DNI que se pasa
    public void abrirCuentaCorriente(String dni, double saldoInicial, double limiteDescubierto) {
        Optional<Cliente> clienteOptional = banco.buscarClientePorDni(dni);

        if (clienteOptional.isEmpty()) {
            Consola.error("No existe cliente con DNI: " + dni);
            return;
        }

        String numeroDeCuenta = banco.generarNumeroCuenta();
        CuentaCorriente cuenta = new CuentaCorriente(numeroDeCuenta, saldoInicial,
                clienteOptional.get(), limiteDescubierto);
        banco.registrarCuenta(cuenta);

        Consola.exito("Cuenta Corriente abierta. Número: " + numeroDeCuenta
                + " | Descubierto: $" + limiteDescubierto);
    }

    // Muestra todas las cuentas de un cliente si es que este existe
    public void verCuentasDeCliente(String dni) {
        banco.buscarClientePorDni(dni).ifPresentOrElse(
                cliente -> {
                    if (cliente.getCuentas().isEmpty()) {
                        Consola.info("El cliente no tiene cuentas.");
                    } else {
                        cliente.getCuentas().forEach(System.out::println);
                    }
                },
                () -> Consola.error("No existe cliente con DNI: " + dni));
    }

    // Deposita un monto en una cuenta
    public void depositar(String numeroDeCuenta, double monto) {
        banco.buscarCuenta(numeroDeCuenta).ifPresentOrElse(
                cuenta -> {
                    if (cuenta.depositar(monto)) {
                        Consola.exito(String.format("Depósito exitoso: $%.2f en cuenta %s", monto, numeroDeCuenta));
                        Consola.info("Nuevo saldo: $" + cuenta.getSaldo());
                    } else {
                        Consola.error("Monto inválido para depósito.");
                    }
                },
                () -> Consola.error("No existe la cuenta: " + numeroDeCuenta));
    }

    // Extrae un monto de una cuenta
    public void extraer(String numeroDeCuenta, double monto) {
        banco.buscarCuenta(numeroDeCuenta).ifPresentOrElse(
                cuenta -> {
                    if (cuenta.extraer(monto)) {
                        Consola.exito(String.format("Extracción exitosa: $%.2f de cuenta %s", monto, numeroDeCuenta));
                        Consola.info("Nuevo saldo: $" + cuenta.getSaldo());
                    } else {
                        Consola.error("Fondos insuficientes o monto inválido.");
                    }
                },
                () -> Consola.error("No existe la cuenta: " + numeroDeCuenta));
    }

    public void transferir(String numeroDeOrigen, String numeroDeDestino, double monto) {
        Optional<Cuenta> origenOptional = banco.buscarCuenta(numeroDeOrigen);
        Optional<Cuenta> destinoOptional = banco.buscarCuenta(numeroDeDestino);

        if (origenOptional.isEmpty()) {
            Consola.error("No existe la cuenta origen: " + numeroDeOrigen);
            return;
        }

        if (destinoOptional.isEmpty()) {
            Consola.error("No existe la cuenta destino: " + numeroDeDestino);
            return;
        }

        Cuenta origen = origenOptional.get();
        Cuenta destino = destinoOptional.get();

        if (!origen.extraer(monto)) {
            Consola.error("Fondos insuficientes en la cuenta origen.");
            return;
        }

        destino.depositar(monto);

        Consola.exito(String.format("Transferencia exitosa: $%.2f de %s a %s", monto, numeroDeOrigen, numeroDeDestino));
    }

    // Muestra el historial completo de los movimientos de una cuenta
    public void verHistorial(String numeroDeCuenta) {
        banco.buscarCuenta(numeroDeCuenta).ifPresentOrElse(
                cuenta -> {
                    Consola.subtitulo("Historial - Cuenta " + numeroDeCuenta);
                    System.out.println(cuenta);

                    if (cuenta.getHistorialMovimientos().isEmpty()) {
                        Consola.info("Sin movimientos registrados.");
                    } else {
                        cuenta.getHistorialMovimientos().forEach(System.out::println);
                    }
                },
                () -> Consola.error("No existe la cuenta: " + numeroDeCuenta));
    }

    public void verSaldo(String numeroDeCuenta) {
        banco.buscarCuenta(numeroDeCuenta).ifPresentOrElse(
                cuenta -> Consola.info(String.format("Saldo de cuenta %s: $%.2f", numeroDeCuenta, cuenta.getSaldo())),
                () -> Consola.error("No existe la cuenta: " + numeroDeCuenta));
    }

    // Muestra un resumen general del banco
    public void resumenGeneral() {
        Consola.titulo("RESUMEN GENERAL DEL BANCO");
        System.out.println("  " + banco);
        Consola.separador();

        double totalActivos = banco.getCuentas().stream()
                .mapToDouble(Cuenta::getSaldo)
                .sum();

        System.out.printf("  Total de activos en el sistema: $%.2f%n", totalActivos);
        System.out.printf("  Promedio de saldo por cuenta:   $%.2f%n",
                banco.totalCuentas() > 0 ? totalActivos / banco.totalCuentas() : 0);
        Consola.separador();
    }
}
