from flask_restx import Resource, Namespace, abort
from .models import Article, Comment 
from .api_models import article_model, commentaire_model, article_input_model, commentaire_input_model

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self) :
        return {"hello": "restx"}
    
@ns.route("/articles")
class ArticleCollection(Resource):
    @ns.marshal_list_with(article_model)
    def get(self) :
        return Article.get_all_articles()
    
    @ns.expect(article_input_model)
    @ns.marshal_with(article_model)
    def post(self) :
        article = Article.create_article(title = ns.payload["title"] , content = ns.payload["content"])
        return article, 201
    
@ns.route("/comments")
class CommentairesCollection(Resource):
    @ns.marshal_list_with(commentaire_model)
    def get(self):
        return Comment.get_all_comments()
    
    @ns.expect(commentaire_input_model)
    @ns.marshal_with(commentaire_model)
    @ns.response(404 , 'Article not found for comment')
    def post(self) :
        comment = Comment.create_comment(content = ns.payload["content"] , id_article = ns.payload["article"])
        if comment is None:
            abort(404,"Article not found for comment")
        return comment, 201
    
@ns.route("/articles/<int:id>")
@ns.response(404 , 'Article not found')
class ArticleItem(Resource) :
    @ns.marshal_with(article_model)
    def get(self, id) :
        article = Article.get_article(id)
        if article is None :
            abort(404,"Article not found")
        return article
    
    
    def delete(self, id) :
        Article.delete_article(id)
        return {} , 204
    
@ns.route("/comments/<int:id>")
@ns.response(404 , 'Comment not found')
class CommentItem(Resource) :
    @ns.marshal_with(commentaire_model)
    def get(self, id) :
        comment = Comment.get_comment(id)
        if comment is None :
            abort(404,"Comment not found")
        return comment
    
    def delete(self, id) :
        Comment.delete_article(id)
        return {} , 204