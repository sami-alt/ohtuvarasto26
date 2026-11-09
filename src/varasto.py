"""Provide a storage container for tracking available inventory."""


class Varasto:
    """Represent a storage container with a fixed capacity."""

    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = tilavuus if tilavuus > 0.0 else 0.0
        self.saldo = self._alku_saldo(tilavuus, alku_saldo)


    @staticmethod
    def _alku_saldo(tilavuus, alku_saldo):
        """Return the initial balance using the original storage rules."""
        if alku_saldo < 0.0:
            return 0.0
        if alku_saldo <= tilavuus:
            return alku_saldo
        return tilavuus

    # Ominaisuus voidaan laskea ilman erillistä viela_tilaa-kenttää.
    def paljonko_mahtuu(self):
        """Return the remaining capacity of the storage container."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Add as much of the given amount as fits in the container."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Remove and return the requested amount from the container."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
