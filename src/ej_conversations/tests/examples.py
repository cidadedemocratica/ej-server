CATEGORY = {
    "links": {"self": "http://testserver/categories/category/"},
    "name": "Category",
    "slug": "category",
    "image": None,
    "image_caption": "",
}

USER_ROOT = {"url": "http://testserver/users/root/", "username": "root"}

USER = {"url": "http://testserver/users/user/", "username": "user"}

COMMENT = {
    "links": {
        "self": "http://testserver/api/v1/comments/1/"
    },
    "content": "content",
    "status": "approved",
    "rejection_reason": 0,
    "rejection_reason_text": ""
}

CONVERSATION = {
    "links": {
        "self": "http://testserver/api/v1/conversations/1/",
        "vote-dataset": "http://testserver/api/v1/conversations/1/vote-dataset/",
        "user-statistics": "http://testserver/api/v1/conversations/1/user-statistics/",
        "approved-comments": "http://testserver/api/v1/conversations/1/approved-comments/",
        "user-comments": "http://testserver/api/v1/conversations/1/user-comments/",
        "user-pending-comments": "http://testserver/api/v1/conversations/1/user-pending-comments/",
        "random-comment": "http://testserver/api/v1/conversations/1/random-comment/",
        "reports": "http://testserver/api/v1/conversations/1/reports/",
        "clusterization": None,
        "author": "http://testserver/api/v1/users/1/"
    },
    "author": "email@server.com",
    "title": "title",
    "slug": "title",
    "statistics": {
        "comments": {"approved": 0, "rejected": 0, "pending": 0, "total": 0},
        "votes": {"agree": 0, "disagree": 0, "skip": 0, "total": 0},
        "participants": {'commenters': 0, 'voters': 0},
    },
    "text": "test"
}

VOTE = {
    "links": {
        "self": "http://testserver/api/v1/votes/1/",
        "comment": "http://testserver/api/v1/comments/1/"
    },
    "comment": "content",
    "choice": 1
}
