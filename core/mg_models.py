from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, fields


class City(EmbeddedDocument):
    name = fields.StringField(max_length=20, required=True)
    code = fields.StringField(max_length=20, required=True)


class Viewpoint(EmbeddedDocument):
    name = fields.StringField(max_length=20, required=True)
    location = fields.StringField(max_length=20, required=True)
    early_time = fields.IntField(default=0)
    late_time = fields.IntField(default=24)
    priority = fields.IntField(default=0)


class Journey(Document):
    name = fields.StringField(max_length=20, required=True)
    image = fields.StringField(max_length=100, default="")
    day_number = fields.IntField(requied=True)
    start_day = fields.DateField(required=True)
    end_day = fields.DateField(required=True)
    people_number = fields.IntField(default=0)
    people_type = fields.IntField(default=0)
    travel_mode = fields.IntField(default=0)
    play_time = fields.IntField(default=0)
    cities = fields.ListField(EmbeddedDocumentField(City))
    viewpoints = fields.ListField(fields.EmbeddedDocumentField(Viewpoint))
    routes = fields.ListField(fields.ListField(fields.IntField()))
    public = fields.BooleanField(default=True)
