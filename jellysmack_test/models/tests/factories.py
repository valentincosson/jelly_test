import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker_enum import EnumProvider
from jellysmack_test.conftest import TestingSession

from ..comment import CommentModel
from ..episode import EpisodeModel
from ..character import (
    CharacterModel,
    GenderEnum,
    SpeciesEnum,
    StatusEnum,
    CharacterEpisodesModel,
)


def generate_json_factory(factory: SQLAlchemyModelFactory):
    """Build a factory without commiting object and transform it to JSON"""
    stub = factory.stub().__dict__  # Don't commit, just generate it

    # Clean only-db attributes
    keys = ["created_at", "updated_at", "id"]

    for key in keys:
        if key in stub:
            stub.pop(key)
    return stub


class CommentFactory(SQLAlchemyModelFactory):
    class Meta:
        model = CommentModel
        sqlalchemy_session = TestingSession
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: n)
    created_at = factory.Faker("date_object")
    updated_at = factory.SelfAttribute("created_at")
    text = factory.Faker("text")


class EpisodeFactory(SQLAlchemyModelFactory):
    class Meta:
        model = EpisodeModel
        sqlalchemy_session = TestingSession
        sqlalchemy_session_persistence = "commit"

    factory.Faker.add_provider(EnumProvider)

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    air_date = factory.Faker("date_object")
    episode = factory.Faker("pyint")
    season = factory.Faker("pyint")


class CharacterFactory(SQLAlchemyModelFactory):
    class Meta:
        model = CharacterModel
        sqlalchemy_session = TestingSession
        sqlalchemy_session_persistence = "commit"

    factory.Faker.add_provider(EnumProvider)

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    status = factory.Faker("enum", enum_cls=StatusEnum)
    species = factory.Faker("enum", enum_cls=SpeciesEnum)
    type = factory.Faker("text")
    gender = factory.Faker("enum", enum_cls=GenderEnum)


class CharacterWithEpisodesFactory(CharacterFactory):
    episodes = factory.RelatedFactoryList(
        "jellysmack_test.models.tests.factories.CharacterEpisodesFactory",
        "character",
    )


class EpisodeWithCharactersFactory(EpisodeFactory):
    characters = factory.RelatedFactoryList(
        "jellysmack_test.models.tests.factories.CharacterEpisodesFactory",
        factory_related_name="episode",
    )


class CommentOnEpisodeFactory(CommentFactory):
    episode = factory.SubFactory(EpisodeFactory)


class CommentOnCharacterFactory(CommentFactory):
    character = factory.SubFactory(CharacterFactory)


class CommentOnCharacterInAnEpisodeFactory(CommentFactory):
    character = factory.SubFactory(CharacterWithEpisodesFactory)

    @factory.post_generation
    def add_episode(self, create, _):
        if not create:
            return
        self.episode = self.character.episodes[0].episode


class CharacterEpisodesFactory(SQLAlchemyModelFactory):
    class Meta:
        model = CharacterEpisodesModel
        sqlalchemy_session = TestingSession
        sqlalchemy_session_persistence = "commit"

    episode = factory.SubFactory(EpisodeFactory)
    character = factory.SubFactory(CharacterFactory)
