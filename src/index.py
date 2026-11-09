"""Run a demonstration of the Varasto class."""

from varasto import Varasto


def main():
    """Create sample storages and demonstrate their operations."""
    mehua, olutta = luo_varastot()
    tulosta_luonti(mehua, olutta)
    tulosta_getterit(olutta)
    kasittele_mehua(mehua)
    kasittele_virhetilanteet()
    kasittele_olutta(olutta)
    kasittele_negatiivinen_lisays(mehua)
    kasittele_oluen_tyhjennys(olutta)
    kasittele_mehun_tyhjennys(mehua)


def luo_varastot():
    """Create the storages used in the demonstration."""
    return Varasto(100.0), Varasto(100.0, 20.2)


def tulosta_luonti(mehua, olutta):
    """Print the initial state of the sample storages."""
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def tulosta_getterit(olutta):
    """Print the values available from a storage."""
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def kasittele_mehua(mehua):
    """Demonstrate adding to and removing from a storage."""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def kasittele_virhetilanteet():
    """Demonstrate invalid storage initialization values."""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def kasittele_olutta(olutta):
    """Demonstrate adding more than a storage can hold."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")


def kasittele_negatiivinen_lisays(mehua):
    """Demonstrate that a negative addition is ignored."""
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def kasittele_oluen_tyhjennys(olutta):
    """Demonstrate removing more than the beer storage contains."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def kasittele_mehun_tyhjennys(mehua):
    """Demonstrate rejecting a negative removal amount."""
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
