import laposte, unittest, laposte.LaPosteExeptions

class Tests(unittest.TestCase):
    def setUp(self):
        self.package_1 = laposte.Suivi()
        self.package_1.connect("okapi_key sandox")
        self.package_1.suivi("LU680211095FR")
        
        self.package_2 = laposte.Suivi()
        self.package_2.connect("okapi_key sandox")
        
        self.package_3 = laposteSuivi()
        self.package_3.connect("okapi_key sandbox")
        self.package_3.suivi("CB662173705US")
        self.package_3.reset()
        
        self.package_4 = laposte.Suivi()
        self.package_4.connect("okapi_key sandbox")
        self.package_4.suivi("CB662173705US")
        self.package_4.reset(client=True)
        
    def test_suivi(self):
        self.assertEqual(self.package_1.return_code, 200)
        self.assertEqual(self.package_1.scope, "open")
        self.assertEqual(self.package_1.holder, 1)
        self.assertEqual(self.package_1.id_ship, "LU680211095FR")
        self.assertEqual(self.package_1.product, "Courrier international")
        self.assertEqual(self.package_1.is_final, False)
        self.assertEqual(self.package_1.entry_date, None)
        self.assertEqual(self.package_1.event, [{'code': 'DR1', 'label': 'La Poste est prête à prendre en charge votre envoi. Dès qu’il nous sera confié, vous pourrez suivre son trajet ici.', 'date': '2021-11-27T10:10:00+01:00'}])
        self.assertEqual(self.package_1.timeline, [{'shortLabel': "Votre envoi est trop récent, son suivi n'est pas encore disponible sur notre site. Nous vous invitons à réessayer ultérieurement.", 'id': 1, 'country': '', 'status': False, 'type': 1}, {'shortLabel': '', 'longLabel': '', 'id': 2, 'country': '', 'status': False, 'type': 1}, {'shortLabel': '', 'longLabel': '', 'id': 3, 'country': '', 'status': False, 'type': 1}, {'shortLabel': '', 'longLabel': '', 'id': 4, 'country': '', 'status': False, 'type': 1}, {'shortLabel': '', 'longLabel': '', 'id': 5, 'country': '', 'status': False, 'type': 1}])
        self.assertEqual(self.package_1.context_data, {'deliveryChoice': {'deliveryChoice': 0}, 'originCountry': 'FR', 'arrivalCountry': 'CN'})
        self.assertEqual(self.package_1.data, {'lang': 'fr_FR', 'scope': 'open', 'returnCode': 200, 'shipment': {'idShip': 'LU680211095FR', 'holder': 1, 'product': 'Courrier international', 'isFinal': False, 'timeline': [{'shortLabel': "Votre envoi est trop récent, son suivi n'est pas encore disponible sur notre site. Nous vous invitons à réessayer ultérieurement.", 'id': 1, 'country': '', 'status': False, 'type': 1}, {'shortLabel': '', 'longLabel': '', 'id': 2, 'country': '', 'status': False, 'type': 1}, {'shortLabel': '', 'longLabel': '', 'id': 3, 'country': '', 'status': False, 'type': 1}, {'shortLabel': '', 'longLabel': '', 'id': 4, 'country': '', 'status': False, 'type': 1}, {'shortLabel': '', 'longLabel': '', 'id': 5, 'country': '', 'status': False, 'type': 1}], 'event': [{'code': 'DR1', 'label': 'La Poste est prête à prendre en charge votre envoi. Dès qu’il nous sera confié, vous pourrez suivre son trajet ici.', 'date': '2021-11-27T10:10:00+01:00'}], 'contextData': {'deliveryChoice': {'deliveryChoice': 0}, 'originCountry': 'FR', 'arrivalCountry': 'CN'}, 'url': 'https://www.laposte.fr/outils/suivre-vos-envois?code=LU680211095FR'}})

    def test_error(self):
        with self.assertRaises(la_poste_exeptions.ResourceNotFoundExeption):
            self.package_2.suivi("RB658828494MQ")
            
    def test_reset(self):
        self.assertEqual(self.package_3.data.__str__(), la_poste_exeptions.InvalidNumberExeption().__str__())
    
    def test_reset_and_client(self):
        self.assertEqual(self.package_4.data.__str__(), la_poste_exeptions.UnauthorizedExeption().__str__())

if __name__ == "__main__":
    unittest.main()