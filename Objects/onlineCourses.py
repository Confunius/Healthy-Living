class onlineCourse:
    def __init__(self, courseId, videos, createdBy, price, studentPurchaseList, refundDescription, courseContent, requirements, description, courseForWho, instructor):
        self.courseId = courseId
        self.videos = videos
        self.createdBy = createdBy
        self.price = price
        self.studentPurchaseList = studentPurchaseList if studentPurchaseList else []
        self.refundDescription = refundDescription
        self.courseContent = courseContent
        self.requirements = requirements
        self.description = description
        self.courseForWho = courseForWho
        self.instructor = instructor

    def to_dict(self):
        return {
            'courseId': self.courseId,
            'videos': self.videos,
            'createdBy': self.createdBy,
            'price': self.price,
            'studentPurchaseList': self.studentPurchaseList,
            'refundDescription': self.refundDescription,
            'courseContent': self.courseContent,
            'requirements': self.requirements,
            'description': self.description,
            'courseForWho': self.courseForWho,
            'instructor': self.instructor
        }
        
        