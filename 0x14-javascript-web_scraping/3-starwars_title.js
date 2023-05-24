#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});

