class Subject:
    def __init__(self, name: str, exam_ects: float, prac_ects: float, exam_description: str, prac_description: str, studon_url: str, zoom_url: str, contact: str, further_info: str, ping_tag: str, color: str):
        self.name = name
        self.exam_ects = exam_ects
        self.prac_ects = prac_ects
        self.exam_description = exam_description
        self.prac_description = prac_description
        self.studon_url = studon_url
        self.zoom_url = zoom_url
        self.contact = contact
        self.further_info = further_info
        self.ping_tag = ping_tag
        self.color = color