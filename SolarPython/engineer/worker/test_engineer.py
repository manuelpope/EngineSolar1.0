from unittest import TestCase

import engineer.servicios.ProviderEquipment
import engineer.worker.Engineering


class TestEngineer(TestCase):
    def test_calcSolarDesign(self):
        eng = engineer.worker.Engineering.Engineer()
        inversor = engineer.servicios.ProviderEquipment.getInverter()
        panel =engineer.servicios.ProviderEquipment.getPanel()
        reg = engineer.servicios.ProviderEquipment.getRegulator()
        qP= eng.solarPanelsCalculation(inversor,panel,reg, 320.0, 320.0)
        assert (qP==1)

        self.fail()
