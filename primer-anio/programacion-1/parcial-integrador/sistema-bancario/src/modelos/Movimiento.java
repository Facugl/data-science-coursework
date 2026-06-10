package modelos;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Movimiento {
    public enum Tipo {
        DEPOSITO("Depósito"),
        EXTRACCION("Extracción"),
        TRANSFERENCIA_ENTRADA("Transferencia entrada"),
        TRANSFERENCIA_SALIDA("Transferencia salida");

        private final String descripcion;

        Tipo(String descripcion) {
            this.descripcion = descripcion;
        }

        public String getDescripcion() {
            return descripcion;
        }
    }

    private final Tipo tipo;
    private final double monto;
    private final LocalDateTime fecha;
    private final double saldoResultante;
    private final String descripcion;
    private static final DateTimeFormatter FORMATO_FECHA = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");

    public Movimiento(Tipo tipo, double monto, double saldoResultante, String descripcion) {
        this.tipo = tipo;
        this.monto = monto;
        this.fecha = LocalDateTime.now();
        this.saldoResultante = saldoResultante;
        this.descripcion = descripcion;
    }

    public Tipo getTipo() {
        return tipo;
    }

    public double getMonto() {
        return monto;
    }

    public LocalDateTime getFecha() {
        return fecha;
    }

    public double getSaldoResultante() {
        return saldoResultante;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public static DateTimeFormatter getFormatoFecha() {
        return FORMATO_FECHA;
    }

    @Override
    public String toString() {
        return String.format("  [%s] %-25s | Monto: $%10.2f | Saldo: $%10.2f | %s",
                fecha.format(FORMATO_FECHA),
                tipo.getDescripcion(),
                monto,
                saldoResultante,
                descripcion);
    }
}
