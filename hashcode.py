class Photo:
    def __init__(self, id, orientation, n, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags
        self.n =n


class Slide:
    # tags = []

    def __init__(self, photos):
        self.photos = photos
        self.tags = self.set_tags()
        self.get_no = self.get_no()

    def set_tags(self):
        tags = []
        for i in self.photos:
            for tag in i.tags:
                if tag not in tags:
                    tags.append(tag)
        return tags
        # self.tags = list(set(self.tags))

    def get_no(self):
        return len(self.tags)

    def add_photo(self, photo):
        self.photos.append(photo)


class SlideShow:
    def __init__(self, score, slides):
        self.score = score
        self.slides = slides

    def add_slide(self, slide):
        self.slides.append(slide)

    def calc_score(self):
        interest_factors = []
        slides = self.slides
        for i in range(len(slides) - 1):
            interest_factors.append(calc_interest_factor(slides[i], slides[i + 1]))
        self.score = sum(interest_factors)


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


def readFile(filename):
    file = open(filename, "r")
    firstLine = True
    number_of_images = 0
    c = 0
    photos = []
    for line in file:
        if firstLine:
            number_of_images = (int)
            line
            firstLine = False
        else:
            # print(line)
            image = line.split()
            photo = Photo(c, image[0], image[1], image[2:])
            photos.append(photo)

            c += 1
    file.close()
    return photos


def writeFile(filename, slideShow):
    file = open(filename, "w")
    slides = slideShow.slides
    n = len(slides)
    file.write(str(n))
    file.write("\n")
    for slide in slides:
        for image in slide.photos:
            file.write(str(image.id) + " ")
        file.write("\n")
    file.close()


def create_sub(filename):
    all_photos = readFile(filename)
    sorted_photos = sorted(all_photos, key=lambda x: x.n, reverse=False)
    slide_show = create_slide_show(sorted_photos)
    slide_show.slides.sort(key=lambda x: x.get_no, reverse=True)
    # slide_show.slides = sorted_photos
    writeFile("submission" + filename, slide_show)
    slide_show.calc_score()
    print("score for " + filename + ": " + str(slide_show.score))


def calc_interest_factor(slideA, slideB):
    A = set(slideA.tags)
    B = set(slideB.tags)
    common = len(A.intersection(B))
    Acomp = len(A.difference(B))
    Bcomp = len(B.difference(A))
    return min([common, Acomp, Bcomp])


create_sub('a_example.txt')
create_sub('b_lovely_landscapes.txt')
create_sub('c_memorable_moments.txt')
create_sub('d_pet_pictures.txt')
create_sub('e_shiny_selfies.txt')


