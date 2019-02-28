class Photo:
    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags


class Slide:
    tags = []
    photos = []

    def __init__(self, photos):
        self.photos = photos

    def add_photo(self, photo):
        self.photos.append(photo)

    def find_tags(self):
        for i in self.photos:
            for tag in i.tags:
                if tag not in self.tags:
                    self.tags.append(tag)
        self.tags = list(set(self.tags))


class SlideShow:
    def __init__(self, score, slides):
        self.score = score
        self.slides = slides

    def add_slide(self, slide):
        self.slides.append(slide)


def create_slide_show(all_photos):
    slide_show = SlideShow(0, [])
    vertical = []
    for photo in all_photos:
        if photo.orientation == 'H':
            new_slide = Slide([photo])
            slide_show.add_slide(new_slide)
        elif len(vertical) == 1 and photo.orientation == 'V':
            photo_list = [photo, vertical.pop()]
            new_slide = Slide(photo_list)
            slide_show.add_slide(new_slide)
        else:
            vertical.append(photo)
    return slide_show
