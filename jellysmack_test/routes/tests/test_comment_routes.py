from jellysmack_test.conftest import BaseApiTestCase

from jellysmack_test.models.tests.factories import (
    CharacterFactory,
    CommentFactory,
    CommentOnCharacterFactory,
    generate_json_factory,
)


class TestCommentRouter(BaseApiTestCase):
    def test_fetch_all_comments(self):
        comment1 = CommentFactory()
        comment2 = CommentFactory()

        resp = self.client.get("/comment/")
        comments = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(comments), 2)
        self.assertEqual(comments[0]["id"], comment1.id)
        self.assertEqual(comments[1]["id"], comment2.id)

    def test_fetch_comment_by_id(self):
        comment1 = CommentFactory.create()
        _ = CommentFactory.create()

        resp = self.client.get("/comment/")
        comments = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(comments), 2)

        resp = self.client.get(f"/comment/{comment1.id}")
        comment = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(comment["id"], comment1.id)

    def test_create_comment(self):
        character = CharacterFactory()
        data = generate_json_factory(CommentFactory)  # uncommited
        data["character_id"] = character.id

        resp = self.client.get("/comment/")
        comments = resp.json()
        resp = self.client.get("/character/")
        characters = resp.json()

        self.assertEqual(len(comments), 0)
        self.assertEqual(len(characters), 1)

        resp = self.client.post("/comment/", json=data)
        comment = resp.json()

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(comment["character_id"], character.id)

    def test_update_comment(self):
        comment = CommentOnCharacterFactory(text="comment")
        comment2 = CommentOnCharacterFactory(text="comment2")

        resp_patch = self.client.patch(
            f"/comment/{comment.id}", json={"text": "updated_comment"}
        )
        updated_comment = resp_patch.json()

        resp_get = self.client.get("/comment/")
        comments = resp_get.json()

        self.assertEqual(comment.text, "comment")
        self.assertEqual(comment2.text, "comment2")
        self.assertEqual(resp_patch.status_code, 200)
        self.assertEqual(resp_get.status_code, 200)
        self.assertNotEqual(updated_comment["text"], comment.text)
        self.assertNotEqual(comments[0]["text"], comment.text)
        self.assertEqual(comments[1]["text"], comment2.text)

    def test_update_not_found_comment(self):
        resp = self.client.patch("/comment/12", json={"text": "something"})

        self.assertEqual(resp.status_code, 404)

    def test_delete_comment(self):
        comment = CommentOnCharacterFactory()

        resp = self.client.delete(f"/comment/{comment.id}")

        self.assertEqual(resp.status_code, 204)

    def test_delete_not_found_comment(self):
        resp = self.client.delete(f"/comment/12")

        self.assertEqual(resp.status_code, 404)
