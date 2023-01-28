# This is a file for instance definition like group member and publications
class GroupMember:
    def __init__(self, name, position, bio):
        self.name = name
        self.position = position
        self.bio = bio


class Publication:
    def __init__(self, title, journal, doi):
        self.title = title
        self.journal = journal
        self.doi = doi

