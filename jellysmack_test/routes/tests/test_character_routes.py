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
