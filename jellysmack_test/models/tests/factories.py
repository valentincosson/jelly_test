import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker_enum import EnumProvider
from jellysmack_test.conftest import TestingSession

from ..character import (
    CharacterModel,
    GenderEnum,
    SpeciesEnum,
    StatusEnum,
    CharacterEpisodesModel,
)
from ..episode import EpisodeModel


class EpisodeModelFactory(SQLAlchemyModelFactory):
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


class CharacterModelFactory(SQLAlchemyModelFactory):
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


class CharacterModelWithEpisodesFactory(CharacterModelFactory):
    episodes = factory.RelatedFactoryList(
        "jellysmack_test.models.tests.factories.CharacterEpisodesModelFactory",
        "character",
    )


class EpisodeModelWithCharactersFactory(EpisodeModelFactory):
    characters = factory.RelatedFactoryList(
        "jellysmack_test.models.tests.factories.CharacterEpisodesModelFactory",
        factory_related_name="episode",
    )


class CharacterEpisodesModelFactory(SQLAlchemyModelFactory):
    class Meta:
        model = CharacterEpisodesModel
        sqlalchemy_session = TestingSession
        sqlalchemy_session_persistence = "commit"

    episode = factory.SubFactory(EpisodeModelFactory)
    character = factory.SubFactory(CharacterModelFactory)
