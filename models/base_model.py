import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    from models import storage

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()
                if 'updated_at' in kwargs:
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        if __name__ == '__main__':
            storage.new(self)
            storage.save()
        else:
            from models import storage
            storage.new(self)
            storage.save()

    def to_dict(self):
        """Converts instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        if 'created_at' in dictionary:
            dictionary['created_at'] = self.created_at.isoformat()
        if 'updated_at' in dictionary:
            dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary
