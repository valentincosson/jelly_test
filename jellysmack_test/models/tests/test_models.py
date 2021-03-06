from jellysmack_test.conftest import BaseTestCase

from .factories import (
    CharacterFactory,
    CommentFactory,
    CommentOnCharacterFactory,
    CommentOnCharacterInAnEpisodeFactory,
    CommentOnEpisodeFactory,
    EpisodeFactory,
)

from ..episode import EpisodeModel
from ..character import CharacterModel
from ..comment import CommentModel


class TestEpisodeModel(BaseTestCase):
    def test_object_creation(self):
        episode1 = EpisodeFactory(id=1)
        episode2 = EpisodeFactory(id=5)

        episodes = EpisodeModel.fetch_all(self.session)

        self.assertIsNotNone(EpisodeModel.fetch_by_id(self.session, episode1.id))
        self.assertIsNotNone(EpisodeModel.fetch_by_id(self.session, episode2.id))
        self.assertEqual(len(episodes), 2)


class TestCharacterModel(BaseTestCase):
    def test_object_creation(self):
        character1 = CharacterFactory(id=9)
        character2 = CharacterFactory(id=16)

        characters = CharacterModel.fetch_all(self.session)

        self.assertIsNotNone(CharacterModel.fetch_by_id(self.session, character1.id))
        self.assertIsNotNone(CharacterModel.fetch_by_id(self.session, character2.id))
        self.assertEqual(len(characters), 2)

    def test_fetch_characters_with_pagination(self):
        count = 0
        while count < 10:
            CharacterFactory()
            count += 1

        first_page_characters = CharacterModel.fetch_all(
            self.session, offset=0, limit=5
        )
        first_page_ids = [obj.id for obj in first_page_characters]
        scnd_page_characters = CharacterModel.fetch_all(self.session, offset=5, limit=5)
        scnd_page_ids = [obj.id for obj in scnd_page_characters]

        self.assertEqual(len(first_page_characters), 5)
        self.assertEqual(len(scnd_page_characters), 5)
        self.assertNotEqual(first_page_ids, scnd_page_ids)


class TestCommentModel(BaseTestCase):
    def test_object_creation(self):
        comment1 = CommentFactory(id=8)
        comment2 = CommentFactory(id=10)

        comments = CommentModel.fetch_all(self.session)

        self.assertIsNotNone(CommentModel.fetch_by_id(self.session, comment1.id))
        self.assertIsNotNone(CommentModel.fetch_by_id(self.session, comment2.id))
        self.assertEqual(len(comments), 2)

    def test_comment_on_episode(self):
        comment = CommentOnEpisodeFactory()

        obj = CommentModel.fetch_by_id(self.session, comment.id)

        self.assertEqual(obj.text, comment.text)
        self.assertEqual(obj.episode, comment.episode)
        self.assertEqual(obj.episode.comments[0].text, comment.text)

    def test_comment_on_character(self):
        comment = CommentOnCharacterFactory()

        obj = CommentModel.fetch_by_id(self.session, comment.id)

        self.assertEqual(obj.text, comment.text)
        self.assertEqual(obj.character, comment.character)
        self.assertEqual(obj.character.comments[0].text, comment.text)

    def test_comment_on_a_character_in_an_episode(self):
        comment = CommentOnCharacterInAnEpisodeFactory()

        obj = CommentModel.fetch_by_id(self.session, comment.id)

        self.assertEqual(obj.text, comment.text)
        self.assertEqual(obj.character, comment.character)
        self.assertEqual(obj.episode, comment.episode)
        self.assertEqual(obj.episode.characters[0].character.id, comment.character.id)
        self.assertEqual(obj.character.comments[0].text, comment.text)
        self.assertEqual(obj.episode.comments[0].text, comment.text)

    def test_fetch_comments_with_pagination(self):
        count = 0
        while count < 10:
            CommentFactory()
            count += 1

        first_page_comments = CommentModel.fetch_all(self.session, offset=0, limit=5)
        first_page_ids = [obj.id for obj in first_page_comments]
        scnd_page_comments = CommentModel.fetch_all(self.session, offset=5, limit=5)
        scnd_page_ids = [obj.id for obj in scnd_page_comments]

        self.assertEqual(len(first_page_comments), 5)
        self.assertEqual(len(scnd_page_comments), 5)
        self.assertNotEqual(first_page_ids, scnd_page_ids)
