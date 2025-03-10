from .extensions import db

class Article (db.Model) :
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(500))
    comments = db.relationship("Comment",back_populates="article")

    @staticmethod
    def get_all_articles() :
        return Article.query.all()
    
    @staticmethod
    def create_article(title, content) :
        article = Article(title = title, content = content)
        db.session.add(article)
        db.session.commit()
        return article
    
    @staticmethod
    def get_article(id):
        return Article.query.get(id)
    
    @staticmethod
    def delete_article(id):
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()

class Comment(db. Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db. Column (db.String(100))
    article_id = db.Column(db.ForeignKey("article.id"))
    article = db.relationship("Article",back_populates="comments")

    @staticmethod
    def get_all_comments():
        return Comment.query.all()
    
    @staticmethod
    def get_comment(id):
        return Comment.query.get(id)
    
    @staticmethod
    def create_comment(content, id_article):
        result_art = Article.get_article(id_article)
        if result_art is None:
            return None
        else:
            comment = Comment(content=content, article_id=id_article)
            db.session.add(comment)
            db.session.commit()
            return Comment.get_comment(comment.id)
        
    @staticmethod
    def delete_comment(id):
        comment = Comment.query.get(id)
        db.session.delete(comment)
        db.session.commit()
