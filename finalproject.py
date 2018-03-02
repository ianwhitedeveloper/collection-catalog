from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbsetup import Base, Collection, CollectionItem
app = Flask(__name__)


engine = create_engine('sqlite:///collectioncatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Fake Collections
# collection = {'name': 'Collection1', 'id': '1'}

# collections = [{'name': 'Collection1', 'id': '1'}, {'name':'Collection2', 'id':'2'},{'name':'Collection3', 'id':'3'}]


# Fake Collection Items
# items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
# item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}
# items = []


@app.route('/collection/JSON')
def collectionsJSON():
    collections = session.query(Collection).all()
    return jsonify(collections=[c.serialize for c in collections])

@app.route('/collection/<int:collection_id>/items/JSON')
def collectionItemsJSON(collection_id):
    collection = session.query(Collection).filter_by(id=collection_id).one()
    items = session.query(CollectionItem).filter_by(
        collection_id=collection_id).all()
    return jsonify(CollectionItems=[i.serialize for i in items])                ###should this be CollectionItem to refer back to class in dbsetup?


@app.route('/collection/<int:collection_id>/items/<int:item_id>/JSON')
def ItemJSON(collection_id, item_id):
    Collection_Item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Collection_Item=Collection_Item.serialize)


# Show all collections
@app.route('/')
@app.route('/collection/')
def showCollections():
    collections = session.query(Collection).all()
    #return "This page will show all my collections"
    return render_template('collections.html', collections=collections)


# Create a new collection
@app.route('/collection/new/', methods=['GET', 'POST'])
def newCollection():
    if request.method == 'POST':
        newCollection = Collection(name=request.form['name'])
        session.add(newCollection)
        session.commit()
        return redirect(url_for('showCollections'))
    else:
        return render_template('newCollection.html')
        #return "This page will be for making a new collection"


# Edit a collection

@app.route('/collection/<int:collection_id>/edit/', methods=['GET', 'POST'])
def editCollection(collection_id):
    editedCollection = session.query(
        Collection).filter_by(id=collection_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCollection.name = request.form['name']
            return redirect(url_for('showCollections'))
    else:
        return render_template('editCollection.html',
                                collection=editedCollection)
        #return 'This page will be for editing collection %s' % collection_id


# Delete a collection

@app.route('/collection/<int:collection_id>/delete/', methods=['GET', 'POST'])
def deleteCollection(collection_id):
    collectionToDelete = session.query(
        Collection).filter_by(id=collection_id).one()
    if request.method == 'POST':
        session.delete(collectionToDelete)
        session.commit()
        return redirect(
            url_for('showCollections', collection_id=collection_id))
    else:
        return render_template('deleteCollection.html',
                                collection=collectionToDelete)
        #return 'This page will be for deleting collection %s' % collection_id


# Show collection items

@app.route('/collection/<int:collection_id>/')
@app.route('/collection/<int:collection_id>/items/')
def showItems(collection_id):
    collection = session.query(Collection).filter_by(id=collection_id).one()
    items = session.query(CollectionItem).filter_by(
        collection_id=collection_id).all()
    return render_template('collectionItems.html',
                            items=items, collection=collection)
    #return 'This page is the list of items for collection %s' % collection_id


# Create a new collection item

@app.route(
    '/collection/<int:collection_id>/items/new/', methods=['GET', 'POST'])
def newCollectionItem(collection_id):
    if request.method == 'POST':
        newItem = CollectionItem(name=request.form['name'],
                                description=request.form['description'],
                                price=request.form['price'],
                                category=request.form['category'],
                                collection_id=collection_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showItems', collection_id=collection_id))
    else:
        return render_template('newCollectionItem.html',
                                collection_id=collection_id)
        return render_template('newCollectionItem.html', collection=collection) ## is this a duplicate??
        #return 'This page is for making a new menu item for collection %s' % collection_id


# Edit a collection item

@app.route('/collection/<int:collection_id>/items/<int:item>/edit',
           methods=['GET', 'POST'])
def editCollectionItem(collection_id, item_id):
    editedCollectionItem = session.query(CollectionItem).filter_by(id=item).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCollectionItem.name = request.form['name']
        if request.form['description']:
            editedCollectionItem.description = request.form['name']
        if request.form['price']:
            editedCollectionItem.price = request.form['price']
        if request.form['category']:
            editedCollectionItem.category = request.form['category']
        session.add(editedCollectionItem)
        session.commit()
        return redirect(url_for('showItems', collection_id=collection_id))
    else:
        return render_template('editCollectionItem.html',
                                collection_id=collection_id,
                                item_id=item_id,
                                item=editedCollectionItem)
        #return 'This page is for editing collection item %s' % item_id


# Delete a collection item

@app.route('/collection/<int:collection_id>/items/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteCollectionItem(collection_id, item_id):
    itemToDelete = session.query(CollectionItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showItems', collection_id=collection_id))
    else:
        #return render_template('deleteCollectionItem.html', item=itemToDelete)
        return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
