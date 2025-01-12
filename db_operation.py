def get_all(model, db):
    Session = db.session()
    records = Session.query(model).all()
    return records

def get_product_by_id(model, db, id):
    product = db.session.query(model).filter_by(id=id).first()
    return product

def get_category_by_id(model, db, id):
    category = db.session.query(model).filter_by(id=id).first()
    return category

def get_user_by_id(model, db, id):
    user = db.session.query(model).filter_by(id=id).first()
    return user

def get_profil_by_id(model, db, id):
    user = db.session.query(model).filter_by(id=id).first()
    return user