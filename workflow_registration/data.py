from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def obj_to_list(obj, column_names):
    """
    make a object to a list of all its data
    :param obj:
    :param column_names:
    :return:
    """
    return [getattr(obj, field_name, None) for field_name in column_names]


def query_to_list(query, include_field_names = True):
    """
    Turns a query into a list of data values
    :param query:
    :param include_field_names:
    :return:
    """
    column_names = []
    for i, obj in enumerate(query.all()):
        if i == 0:
            column_names = [c.name for c in obj.__table__.columns]
            if include_field_names:
                yield column_names
        yield obj_to_list(obj, column_names)
