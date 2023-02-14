from models.movie import Movie as MovieModel
from schemas.movie import Movie

class Movieservices:
    def __init__(self,db) -> None:
        self.db = db
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self,id):
       result = self.db.query(MovieModel).filter(MovieModel.id == id).all()
       return result
    def get_movie_by_category(self,category):
       result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
       return result
    
    def add_movie(self,movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self,id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()  
        self.db.commit()
        return 
        
