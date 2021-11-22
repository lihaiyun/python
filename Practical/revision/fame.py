class Fame:
    def __init__(self, admin_no, score):
        self.admin_no = admin_no
        self.score = score

    def __str__(self):
        return f'Admin No: {self.admin_no}, Score: {self.score}'
