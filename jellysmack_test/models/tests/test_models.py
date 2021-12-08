from jellysmack_test.conftest import BaseTestCase

from .factories import (
    CharacterModelFactory,
    EpisodeModelFactory,
)

from ..episode import EpisodeModel
from ..character import CharacterModel


class TestEpisodeModel(BaseTestCase):
    def test_object_creation(self):
        episode1 = EpisodeModelFactory(id=1)
        episode2 = EpisodeModelFactory(id=5)

        episodes = EpisodeModel.fetch_all(self.session)

        self.assertIsNotNone(EpisodeModel.fetch_by_id(self.session, episode1.id))
        self.assertIsNotNone(EpisodeModel.fetch_by_id(self.session, episode2.id))
        self.assertEqual(len(episodes), 2)


class TestCharacterModel(BaseTestCase):
    def test_object_creation(self):
        character1 = CharacterModelFactory(id=9)
        character2 = CharacterModelFactory(id=16)

        characters = CharacterModel.fetch_all(self.session)

        self.assertIsNotNone(CharacterModel.fetch_by_id(self.session, character1.id))
        self.assertIsNotNone(CharacterModel.fetch_by_id(self.session, character2.id))
        self.assertEqual(len(characters), 2)
