package modelos;

public class CajaDeAhorro extends Cuenta {
    private double tasaInteres;

    public CajaDeAhorro(String numeroCuenta, double saldoInicial, Cliente titular) {
        super(numeroCuenta, saldoInicial, titular);
        this.tasaInteres = 0.05 // Tasa anual por defecto
        ;
    }

    // Calcula y acredita los intereses correspondientes al saldo actual
    public double acreditarIntereses() {
        double interes = getSaldo() * tasaInteres;
        setSaldo(getSaldo() + interes);
        registrarMovimiento(Movimiento.Tipo.DEPOSITO, interes,
                String.format("Acreditación de intereses (%.1f%% anual)", tasaInteres * 100));
        return interes;
    }

    @Override
    public String getTipoCuenta() {
        return "Caja de Ahorro";
    }

    public double getTasaInteres() {
        return tasaInteres;
    }

    public void setTasaInteres(double tasaInteres) {
        if (tasaInteres >= 0 && tasaInteres <= 1) {
            this.tasaInteres = tasaInteres;
        }
    }

    @Override
    public String toString() {
        return super.toString() + String.format(" | Tasa: %.1f%%", tasaInteres * 100);
    }
}
