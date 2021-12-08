from jellysmack_test.conftest import BaseApiTestCase

from jellysmack_test.models.tests.factories import (
    CharacterFactory,
)


class TestCharacterRouter(BaseApiTestCase):
    def test_fetch_all_characters(self):
        character1 = CharacterFactory()
        character2 = CharacterFactory()

        resp = self.client.get("/character/")
        characters = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(characters), 2)
        self.assertEqual(characters[0]["id"], character1.id)
        self.assertEqual(characters[1]["id"], character2.id)

    def test_fetch_character_by_id(self):
        character1 = CharacterFactory.create()
        _ = CharacterFactory.create()

        resp = self.client.get("/character/")
        characters = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(characters), 2)

        resp = self.client.get(f"/character/{character1.id}")
        character = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(character["id"], character1.id)

    def test_pagination_characters(self):
        count = 0
        while count < 10:
            CharacterFactory()
            count += 1

        resp = self.client.get("/character/?offset=0&limit=5")
        first_page_characters = resp.json()
        first_page_ids = [obj["id"] for obj in first_page_characters]

        resp = self.client.get("/character/?offset=5&limit=5")
        scnd_page_characters = resp.json()
        scnd_page_ids = [obj["id"] for obj in scnd_page_characters]

        self.assertEqual(len(first_page_characters), 5)
        self.assertEqual(len(scnd_page_characters), 5)
        self.assertNotEqual(first_page_ids, scnd_page_ids)

    def test_filters_characters(self):
        count = 0
        while count < 2:
            CharacterFactory(status="Dead", species="Robot")
            count += 1

        count = 0
        while count < 2:
            CharacterFactory(status="Alive", species="Human")
            count += 1

        count = 0
        while count < 2:
            CharacterFactory(status="Dead", species="Human")
            count += 1

        resp = self.client.get("/character/?status=Dead&species=Human")
        characters = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(characters), 2)
