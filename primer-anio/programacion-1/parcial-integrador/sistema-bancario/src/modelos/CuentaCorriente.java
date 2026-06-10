package modelos;

public class CuentaCorriente extends Cuenta {
    // El saldo puede bajar hasta: -limiteDescubierto
    private double limiteDescubierto;

    public CuentaCorriente(String numeroCuenta, double saldoInicial, Cliente titular, double limiteDescubierto) {
        super(numeroCuenta, saldoInicial, titular);
        this.limiteDescubierto = limiteDescubierto;
    }

    // Acá empleamos polimorfismo al sobreescribir extraer()
    @Override
    public boolean extraer(double monto) {
        if (monto <= 0) {
            return false;
        }

        double saldoDisponible = getSaldo() + limiteDescubierto;

        if (monto > saldoDisponible) {
            return false; // supera el límite de descubierto
        }

        setSaldo(getSaldo() - monto);

        String descripcion = getSaldo() < 0
                ? String.format("Extracción en descubierto (límite: $%.2f)", limiteDescubierto)
                : "Extracción en efectivo";

        registrarMovimiento(Movimiento.Tipo.EXTRACCION, monto, descripcion);
        return true;
    }

    // Verifica si la cuenta se encuentra actualmente en descubierto
    public boolean estaEnDescubierto() {
        return getSaldo() < 0;
    }

    // Calcula el monto disponible para extraer (saldo + descubierto)
    public double getMontoDisponible() {
        return getSaldo() + limiteDescubierto;
    }

    @Override
    public String getTipoCuenta() {
        return "Cuenta Corriente";
    }

    public double getLimiteDescubierto() {
        return limiteDescubierto;
    }

    public void setLimiteDescubierto(double limiteDescubierto) {
        if (limiteDescubierto >= 0) {
            this.limiteDescubierto = limiteDescubierto;
        }
    }

    @Override
    public String toString() {
        String estado = estaEnDescubierto() ? " [EN DESCUBIERTO]" : "";
        return super.toString()
                + String.format(" | Descubierto: $%.2f%s", limiteDescubierto, estado);
    }
}
