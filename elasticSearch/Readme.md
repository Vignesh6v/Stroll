Structure of the Elasticsearch

User
=====
```bash
index: user-index, doc_type: user.
```
{
  id: String,
  firstName: String,
  lastName: String,
  email: String (index),
  password: String
}


Tour
=====
```bash
index: tour-index, doc_type: tour.
```
{
  id: String (index),
  name: String,
  createdBy: String,
  category: String,
  time: String,
  distance: String,
  stops: String
}

```bash
index: tourname-index, doc_type: tour.
```
{
  id: String,
  name: String (index),
  createdBy: String,
  category: String,
  time: String,
  distance: String,
  stops: String
}

```bash
index: tourcategory-index, doc_type: tour.
```
{
  id: String,
  name: String,
  createdBy: String,
  category: String (index),
  time: String,
  distance: String,
  stops: String
}

Stops
=======
```bash
index: stops-index, doc_type: stops.
```
{
  id: String,
  tourid: String (index),
  sequence: String,
  name: String,
  location: {
    latitude: String,
    longitude: String
    },
  photoId: String,
  description: String
}


Photo
=======
```bash
index: photo-index, doc_type: photo.
```
{
  id: String,
  photoId: String (index),
  userId: String,
  name: String
}


History
=======
```bash
index: history-index, doc_type: history.
```
{
  id: String,
  userId: String (index),
  tourId: String,
  takenOn: String
}
