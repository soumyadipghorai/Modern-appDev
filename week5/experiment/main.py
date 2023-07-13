from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey , select 
from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()

class User(Base) : 
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement = True, primary_key = True)
    user_name = Column(String, unique = True)
    email = Column(String, unique = True)

class Article(Base) : 
    __tablename__ = 'article'
    article_id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String)
    content = Column(String)
    authors = relationship('User', secondary = 'article_authors')

class ArticleAuthors(Base) : 
    __tablename__ = 'article_authors'
    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key = True, nullable = False)
    article_id = Column(Integer, ForeignKey('article.article_id'), primary_key = True, nullable = False)

engine = create_engine('sqlite:///./testdb.sqlite3')

if __name__ == '__main__' : 
    stmt = select(User)
    print('--------- QUERY ---------- ')
    print(stmt)

    with engine.connect() as conn : 
        print('--------- RESULT ---------- ')
        for row in conn.execute(stmt) :
            print(row)

    #? start session 
    with Session(engine) as session : 
        articles = session.query(Article).filter(Article.article_id == 2).all()
        for article in articles : 
            print('title : {}'.format(article.title)) 
            # authors is a relationship in article table 
            for author in article.authors : 
                print('author : {}'.format(author.user_name))


    # ! approach 1
    with Session(engine, autoflush= False) as session :
        session.begin()
        try : 
            article = Article(title = 'new article', content = 'new article content')
            session.add(article)
            session.flush() # sending it to the database 

            print('------------- GET ARTICLE ID -----------')
            print(article.article_id)

            article_authors = ArticleAuthors(user_id = 1, article_id  = article.article_id)
            session.add(article_authors) # sends to article_authors

        except : 
            print('rolling back')
            session.rollback()
            raise 

        else : 
            print('commit')
            session.commit()

    # ! approach 2 
    with Session(engine, autoflush= False) as session :
        session.begin()
        try : 
            author1 = session.query(User).filter(User.user_name == 'ghorai').one()
            author2 = session.query(User).filter(User.user_name == 'soumyadip').one()
            
            article = Article(title = '2 using relationship', content = '2 new content')
            
            article.authors.append(author1)
            article.authors.append(author2)
            
            session.add(article)
        
        except : 
            print('exception, rolling back')
            session.rollback()
            raise 
        else : 
            print('no exception, hence commi')
            session.commit()