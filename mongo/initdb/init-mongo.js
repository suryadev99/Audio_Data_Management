/* 
Seed MongoDB Docker Database with following collections
  A. song: Collection of Song documents
  B. podcast: Collection of Podcast documents
  C. audiobook: Collection of Audiobook documents
*/
// db = new Mongo().getDB("Audiobook");
// Seed song Collection
db.song.drop(),
db.song.insert({_id: 100, 
  name: "Qudem Molestiae",
  duration:152,
  uploaded_time: new Date(2020, 10, 11, 12, 13, 14)})
db.song.insertMany([
  {
    _id: 101, 
    name: "Qudem Molestiae",
    duration:152,
    uploaded_time: new Date(2020, 10, 11, 12, 13, 14)
  },
  {
    _id: 102, 
    name: "The Hype",
    duration:187,
    uploaded_time: new Date(2020, 10, 15, 8, 3, 40)
  },
  {
    _id: 103, 
    name: "Quibusdam Autem",
    duration:123,
    uploaded_time: new Date(2020, 10, 20, 2, 1, 15)
  },
  {
    _id: 104, 
    name: "Highway to Hell",
    duration:248,
    uploaded_time: new Date(2020, 10, 21, 20, 50, 54)
  },
  {
    _id: 105, 
    name: "Enim Saepe",
    duration:152,
    uploaded_time: new Date(2020, 10, 26, 16, 6, 32)
  },
])

// Seed podcast Collection
db.podcast.drop(),
db.podcast.insertMany([
  {
    _id: 101, 
    name: "Distinctio laborum",
    duration:3455,
    uploaded_time: new Date(2020, 10, 11, 12, 13, 14),
    host: "Leanne Graham",
    participants: [
      "Romaguera Crona",
      "Clementine Bauch",
      "Douglas Extension",
      "Patricia Lebsack",
      "Sandeepan Sandeepan",
      "Harry Potter",
      "Satyajit Ray"
    ]
  },
  {
    _id: 102, 
    name: "Impedit mollitia quod et dolor",
    duration:1522,
    uploaded_time: new Date(2020, 10, 11, 12, 13, 14),
    host: "Ervin Howell",
    participants: [
      "Douglas Extension",
      "Patricia Lebsack"
    ]
  },
  {
    _id: 103, 
    name: "Flask vs FastAPI",
    duration:1234,
    uploaded_time: new Date(2020, 10, 15, 8, 3, 40),
    host: "Leopoldo Corkery",
    participants: [
      "Mrs. Dennis Schulist",
      "Sandeepan Sandeepan"
    ]
  },
  {
    _id: 104, 
    name: "No Importante!",
    duration:546,
    uploaded_time: new Date(2020, 10, 15, 8, 3, 40),
    host: "Kurtis Weissnat",
    participants: []
  },
  {
    _id: 105, 
    name: "On my audiobook version of South Park",
    duration:1988,
    uploaded_time: new Date(2020, 10, 26, 16, 6, 32),
    host: "Clementine Bauch",
    participants: [
      "Leanne Graham"
    ]
  },
])

// Seed audiobook Collection
db.audiobook.drop(),
db.audiobook.insertMany([
  {
    _id: 101, 
    name: "South Park",
    author: "Clementine Bauch",
    narrator: "Leanne Graham",
    duration:15225,
    uploaded_time: new Date(2020, 7, 20, 2, 1, 15)
  },
  {
    _id: 102, 
    name: "Nostrum expedita",
    author: "Mrs. Dennis Schulist",
    narrator: "Nosy Owl",
    duration:5252,
    uploaded_time: new Date(2020, 8, 20, 2, 1, 15)
  },
  {
    _id: 103, 
    name: "My Life in Hogwarts",
    author: "Harry Potter",
    narrator: "Toby",
    duration:46545,
    uploaded_time: new Date(2020, 9, 21, 12, 13, 14)
  },
  {
    _id: 104, 
    name: "A Book",
    author: "Some Author",
    narrator: "Nobody Will Know",
    duration:6487,
    uploaded_time: new Date(2020, 9, 11, 12, 13, 14)
  },
  {
    _id: 105, 
    name: "Apur Panchali",
    author: "Satyajit Ray",
    narrator: "Utpal Dutta",
    duration: 23698,
    uploaded_time: new Date(2020, 11, 12, 11, 12, 11)
  },
])
