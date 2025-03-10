from flask_restx import fields
from .extensions import api

article_model = api.model("Article",{
                        "id": fields.Integer ,
                        "title": fields.String ,
                        "content": fields.String
                        })

commentaire_model = api.model("Comment", {
                            "id": fields.Integer,
                            "title": fields.String,
                            "articles": fields.List(fields.Nested(article_model))
                            })

article_input_model = api.model("ArticleInput" ,{
                                "title": fields.String ,
                                "content": fields.String
                                })

commentaire_input_model = api.model("CommentInput", {
                            "content": fields.String,
                            "article": fields.Integer
                            })