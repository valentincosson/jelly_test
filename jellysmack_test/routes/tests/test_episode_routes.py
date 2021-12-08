from jellysmack_test.conftest import BaseApiTestCase

from jellysmack_test.models.tests.factories import (
    EpisodeFactory,
)


class TestEpisodeRouter(BaseApiTestCase):
    def test_fetch_all_episodes(self):
        episode1 = EpisodeFactory()
        episode2 = EpisodeFactory()

        resp = self.client.get("/episode/")
        episodes = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(episodes), 2)
        self.assertEqual(episodes[0]["id"], episode1.id)
        self.assertEqual(episodes[1]["id"], episode2.id)

    def test_fetch_episode_by_id(self):
        episode1 = EpisodeFactory.create()
        _ = EpisodeFactory.create()

        resp = self.client.get("/episode/")
        episodes = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(episodes), 2)

        resp = self.client.get(f"/episode/{episode1.id}")
        episode = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(episode["id"], episode1.id)
