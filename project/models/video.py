
class Video:

    def __init__(self, id, url, title, publication_date, views):
        self.id = id
        self.url = url
        self.title = title
        self.publication_date = publication_date
        self.views = views

    def get_video_details(self):
        return f'{self.id}, {self.title}, {self.url}, {self.publication_date}, {self.views}'