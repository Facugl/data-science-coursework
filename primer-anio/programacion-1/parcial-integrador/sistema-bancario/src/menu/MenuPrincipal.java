package menu;

import java.util.Scanner;

import servicio.BancoService;
import utilidades.Consola;

public class MenuPrincipal {
    private final BancoService bancoService;
    private final Scanner scanner;

    public MenuPrincipal() {
        this.bancoService = new BancoService();
        this.scanner = new Scanner(System.in);
        cargarDatosDemo(); // Para poder hacer pruebas
    }

    // Inicia el ciclo principal del menú
    public void iniciar() {
        Consola.separador();
        System.out.println("BIENVENIDO AL SISTEMA BANCARIO");
        System.out.println("Desarrollado por: Facundo Luna  |  Programacion I --- 2026");
        Consola.separador();
        System.out.println();
        System.out.println("Este sistema permite gestionar clientes y cuentas bancarias.");
        System.out.println("Desde el menú principal podrá: registrar clientes, abrir cuentas,");
        System.out.println("realizar operaciones bancarias y consultar reportes e historial.");
        System.out.println();
        Consola.separador();
        int opcion;

        do {
            mostrarMenuPrincipal();
            opcion = Consola.leerEntero(scanner, "Seleccione una opción");

            switch (opcion) {
                case 1 -> menuClientes();
                case 2 -> menuCuentas();
                case 3 -> menuOperaciones();
                case 4 -> menuReportes();
                case 0 -> Consola.info("Cerrando sistema. Hasta pronto!");
                default -> Consola.error("Opción inválida. Intente nuevamente...");
            }
        } while (opcion != 0);

        scanner.close(); // Cerramos el Scaner para optimizar
    }

    private void mostrarMenuPrincipal() {
        Consola.separador();
        System.out.println("MENÚ PRINCIPAL");
        Consola.separador();
        System.out.println("1. Gestión de Clientes");
        System.out.println("2. Gestión de Cuentas");
        System.out.println("3. Operaciones Bancarias");
        System.out.println("4. Reportes e Historial");
        System.out.println("0. Salir");
        Consola.separador();
    }

    private void menuClientes() {
        int opcion;
        do {
            Consola.separador();
            System.out.println("GESTIÓN DE CLIENTES");
            Consola.separador();
            System.out.println("1. Registrar nuevo cliente");
            System.out.println("2. Listar todos los clientes");
            System.out.println("3. Buscar cliente por DNI");
            System.out.println("0. Volver al menú principal");
            Consola.separador();

            opcion = Consola.leerEntero(scanner, "Seleccione una opción");

            switch (opcion) {
                case 1 -> registrarCliente();
                case 2 -> bancoService.listarClientes();
                case 3 -> buscarCliente();
                case 0 -> Consola.info("Volviendo al menú principal...");
                default -> Consola.error("Opción inválida.");
            }
        } while (opcion != 0);
    }

    private void menuCuentas() {
        int opcion;
        do {
            Consola.separador();
            System.out.println("GESTIÓN DE CUENTAS");
            Consola.separador();
            System.out.println("1. Abrir Caja de Ahorro");
            System.out.println("2. Abrir Cuenta Corriente");
            System.out.println("3. Ver cuentas de un cliente");
            System.out.println("0. Volver al menú principal");
            Consola.separador();

            opcion = Consola.leerEntero(scanner, "Seleccione una opción");

            switch (opcion) {
                case 1 -> abrirCajaDeAhorro();
                case 2 -> abrirCuentaCorriente();
                case 3 -> verCuentasCliente();
                case 0 -> Consola.info("Volviendo al menú principal...");
                default -> Consola.error("Opción inválida.");
            }
        } while (opcion != 0);
    }

    private void menuOperaciones() {
        int opcion;
        do {
            Consola.separador();
            System.out.println("OPERACIONES BANCARIAS");
            Consola.separador();
            System.out.println("1. Depositar");
            System.out.println("2. Extraer");
            System.out.println("3. Transferir entre cuentas");
            System.out.println("0. Volver al menú principal");
            Consola.separador();

            opcion = Consola.leerEntero(scanner, "Seleccione una opción");

            switch (opcion) {
                case 1 -> depositar();
                case 2 -> extraer();
                case 3 -> transferir();
                case 0 -> Consola.info("Volviendo al menú principal...");
                default -> Consola.error("Opción inválida.");
            }
        } while (opcion != 0);
    }

    private void menuReportes() {
        int opcion;
        do {
            Consola.separador();
            System.out.println("REPORTES E HISTORIAL");
            Consola.separador();
            System.out.println("1. Ver historial de una cuenta");
            System.out.println("2. Ver saldo de una cuenta");
            System.out.println("3. Resumen general del banco");
            System.out.println("0. Volver al menú principal");
            Consola.separador();

            opcion = Consola.leerEntero(scanner, "Seleccione una opción");

            switch (opcion) {
                case 1 -> verHistorial();
                case 2 -> verSaldo();
                case 3 -> bancoService.resumenGeneral();
                case 0 -> Consola.info("Volviendo al menú principal...");
                default -> Consola.error("Opción inválida.");
            }
        } while (opcion != 0);
    }

    private void registrarCliente() {
        Consola.subtitulo("Registrar Nuevo Cliente");
        System.out.print("Nombre: ");
        String nombre = scanner.nextLine();
        System.out.print("Apellido: ");
        String apellido = scanner.nextLine();
        System.out.print("DNI: ");
        String dni = scanner.nextLine();
        System.out.print("Email: ");
        String email = scanner.nextLine();

        bancoService.registrarCliente(nombre, apellido, dni, email);
    }

    private void buscarCliente() {
        Consola.subtitulo("Buscar Cliente por DNI");
        System.out.print("Ingrese DNI: ");
        String dni = scanner.nextLine();
        bancoService.buscarClientePorDni(dni);
    }

    private void abrirCajaDeAhorro() {
        Consola.subtitulo("Abrir Caja de Ahorro");
        System.out.print("DNI del cliente: ");
        String dni = scanner.nextLine();
        double saldoInicial = Consola.leerDouble(scanner, "Saldo inicial");
        bancoService.abrirCajaDeAhorro(dni, saldoInicial);
    }

    private void abrirCuentaCorriente() {
        Consola.subtitulo("Abrir Cuenta Corriente");
        System.out.print("DNI del cliente: ");
        String dni = scanner.nextLine();
        double saldoInicial = Consola.leerDouble(scanner, "Saldo inicial");
        double limiteDescubierto = Consola.leerDouble(scanner, "Límite de descubierto");
        bancoService.abrirCuentaCorriente(dni, saldoInicial, limiteDescubierto);
    }

    private void verCuentasCliente() {
        Consola.subtitulo("Cuentas del Cliente");
        System.out.print("DNI del cliente: ");
        String dni = scanner.nextLine();
        bancoService.verCuentasDeCliente(dni);
    }

    private void depositar() {
        Consola.subtitulo("Depósito");
        System.out.print("Número de cuenta: ");
        String nroCuenta = scanner.nextLine();
        double monto = Consola.leerDouble(scanner, "Monto a depositar");
        bancoService.depositar(nroCuenta, monto);
    }

    private void extraer() {
        Consola.subtitulo("Extracción");
        System.out.print("Número de cuenta: ");
        String nroCuenta = scanner.nextLine();
        double monto = Consola.leerDouble(scanner, "Monto a extraer");
        bancoService.extraer(nroCuenta, monto);
    }

    private void transferir() {
        Consola.subtitulo("Transferencia");
        System.out.print("Cuenta origen : ");
        String origen = scanner.nextLine();
        System.out.print("Cuenta destino: ");
        String destino = scanner.nextLine();
        double monto = Consola.leerDouble(scanner, "Monto a transferir");
        bancoService.transferir(origen, destino, monto);
    }

    private void verHistorial() {
        Consola.subtitulo("Historial de Movimientos");
        System.out.print("Número de cuenta: ");
        String nroCuenta = scanner.nextLine();
        bancoService.verHistorial(nroCuenta);
    }

    private void verSaldo() {
        Consola.subtitulo("Consulta de Saldo");
        System.out.print("Número de cuenta: ");
        String nroCuenta = scanner.nextLine();
        bancoService.verSaldo(nroCuenta);
    }

    private void cargarDatosDemo() {
        bancoService.registrarCliente("Juan", "García", "12345678", "juan@email.com");
        bancoService.registrarCliente("María", "López", "87654321", "maria@email.com");
        bancoService.abrirCajaDeAhorro("12345678", 5000.0);
        bancoService.abrirCuentaCorriente("87654321", 2000.0, 10000.0);
        Consola.info("Datos de prueba cargados correctamente.");
    }
}
