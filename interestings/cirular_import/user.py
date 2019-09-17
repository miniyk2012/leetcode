from typing import List

import comment


class User:

    def __init__(self, user_comment_ids):
        self._user_comment_ids = user_comment_ids

    def get_comments(self) -> List[comment.Comment]:
        return [comment.Comment(comment_id) for comment_id in self._user_comment_ids]
