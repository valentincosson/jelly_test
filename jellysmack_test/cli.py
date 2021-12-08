import typer
import json
import uvicorn
from sqlalchemy.orm.session import Session
from datetime import datetime

from .fixtures import EPISODES_PATH, CHARACTERS_PATH
from .db import Base, engine, create_db_and_tables
from .models.character import CharacterEpisodesModel, CharacterModel
from .models.episode import EpisodeModel
from .settings import SERVER_PORT, SERVER_HOST, SERVER_LOG_LEVEL, SERVER_RELOAD

cli = typer.Typer(name="jellysmack_test API")


@cli.command()
def run(
    port: int = SERVER_PORT,
    host: str = SERVER_HOST,
    log_level: str = SERVER_LOG_LEVEL,
    reload: bool = SERVER_RELOAD,
):
    """Run the API server."""
    uvicorn.run(
        "jellysmack_test.app:app",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
    )


@cli.command()
def init_db():
    """Init database with fixtures data."""
    print(f"-- Launch Import -- ")
    create_db_and_tables(engine)

    # Get all episodes and characters from files
    episodes = _get_fixture(EPISODES_PATH)
    characters = _get_fixture(CHARACTERS_PATH)

    total_episodes = len(episodes)
    total_characters = len(characters)

    with Session(engine) as session:
        created_episodes = {}
        for index, data in enumerate(episodes):
            print(f"Episode {index + 1}/{total_episodes}")

            air_date = datetime.strptime(data["air_date"], "%B %d, %Y")
            season, episode = data["episode"].replace("S", "").split("E")

            # Create each episode and add it to created_episodes dict for reusing it later
            entry = EpisodeModel(
                id=data["id"],
                name=data["name"],
                air_date=air_date,
                episode=episode,
                season=season,
            )
            created_episodes[entry.id] = entry
            session.add(entry)
        session.commit()

        for index, data in enumerate(characters):
            print(f"Character {index + 1}/{total_characters}")

            entry = CharacterModel(
                id=data["id"],
                name=data["name"],
                status=data.get("status", "").lower(),
                species=data.get("species", "").replace(" ", "_").lower(),
                type=data.get("type"),
                gender=data.get("gender", "").lower(),
            )

            # Get all created episodes (EpisodeModel) associated with this character
            associated_episodes = [created_episodes[ep] for ep in data["episode"]]

            for episode in associated_episodes:
                association = CharacterEpisodesModel()
                association.episode = episode
                entry.episodes.append(association)

            session.add(entry)

        # bulk commit
        session.commit()


def _get_fixture(path):
    with open(path) as f:
        return json.load(f)


@cli.command()
def reset_db(
    drop: bool = typer.Option(
        True,
        help="Allows you to specify if you do not want to delete the database and only delete its contents.",
    )
):
    """Reset the database."""
    print(f"-- Reset Database -- ")

    create_db_and_tables(engine)

    with Session(engine) as session:
        for table in reversed(Base.metadata.sorted_tables):
            if drop:
                print(f"Drop table {table}")
                table.drop(engine)
            else:
                print(f"Clear table {table}")
                session.execute(table.delete())
        session.commit()
