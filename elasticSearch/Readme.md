# Schema for the Elasticsearch

AWS Elasticsearch

User
=====
index: user-index, doc_type: user.

```bash
{
  id: String,
  firstName: String,
  lastName: String,
  email: String (index),
  password: String
}
```

Tour
=====

index: tour-index, doc_type: tour.

```bash
{
  id: String (index),
  name: String,
  createdBy: String,
  category: String,
  time: String,
  distance: String,
  stops: String,
  location: {
    latitude: String,
    longitude: String  
  }
}
```

index: tourloc-index, doc_type: tour.

```bash
{
  id: String,
  name: String,
  createdBy: String,
  category: String,
  time: String,
  distance: String,
  stops: String,
  location: String (index)
}
```

index: tourcategory-index, doc_type: tour.

```bash
{
  id: String,
  name: String,
  createdBy: String,
  category: String (index),
  time: String,
  distance: String,
  stops: String,
  location: {
    latitude: String,
    longitude: String  
  }  
}
```

Stops
=======

index: stops-index, doc_type: stops.

```bash
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
```

Photo
=======

index: photo-index, doc_type: photo.

```bash
{
  id: String,
  photoId: String (index),
  userId: String,
  name: String
}
```

History
=======

index: history-index, doc_type: history.

```bash
{
  id: String,
  userId: String (index),
  tourId: String,
  takenOn: String
}
```
