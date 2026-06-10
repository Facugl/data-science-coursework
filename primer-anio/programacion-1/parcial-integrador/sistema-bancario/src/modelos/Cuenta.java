package modelos;

import java.util.ArrayList;
import java.util.List;

public abstract class Cuenta {
    private final String numeroCuenta;
    private double saldo;
    private final Cliente titular;
    private final List<Movimiento> historialMovimientos;

    public Cuenta(String numeroCuenta, double saldoInicial, Cliente titular) {
        this.numeroCuenta = numeroCuenta;
        this.saldo = saldoInicial;
        this.titular = titular;
        this.historialMovimientos = new ArrayList<>();

        // Registro del movimiento inicial de apertura
        if (saldoInicial > 0) {
            registrarMovimiento(Movimiento.Tipo.DEPOSITO, saldoInicial, "Apertura de cuenta");
        }
    }

        public boolean depositar(double monto) {
        if (monto <= 0) {
            return false;
        }
        this.saldo += monto;
        registrarMovimiento(Movimiento.Tipo.DEPOSITO, monto, "Depósito en efectivo");
        return true;
    }

        public boolean extraer(double monto) {
        if (monto <= 0 || monto > this.saldo) {
            return false;
        }
        this.saldo -= monto;
        registrarMovimiento(Movimiento.Tipo.EXTRACCION, monto, "Extracción en efectivo");
        return true;
    }

    // Registra un movimiento en el historial de la cuenta
    protected void registrarMovimiento(Movimiento.Tipo tipo, double monto, String descripcion) {
        Movimiento movimiento = new Movimiento(tipo, monto, this.saldo, descripcion);
        this.historialMovimientos.add(movimiento);
    }

    // Acá usaremos Pliformismo tambien, cada subclase implementa su propia descripción
    public abstract String getTipoCuenta();

    public String getNumeroCuenta() {
        return numeroCuenta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public Cliente getTitular() {
        return titular;
    }

    public List<Movimiento> getHistorialMovimientos() {
        return historialMovimientos;
    }

        @Override
    public String toString() {
        return String.format("  Cuenta %-10s | Tipo: %-18s | Titular: %-20s | Saldo: $%.2f",
                numeroCuenta,
                getTipoCuenta(),
                titular.getNombreCompleto(),
                saldo);
    }
    
}
