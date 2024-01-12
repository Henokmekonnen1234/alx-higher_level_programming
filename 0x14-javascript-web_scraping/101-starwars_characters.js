#!/usr/bin/node
const request = require('request');
if (process.argv[2]) {
  function Request (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      }
      );
    }
    );
  }

  const url = 'https://swapi-api.alx-tools.com/api/films/';
  Request(url + process.argv[2])
    .then(response => {
      response.characters.forEach(result => {
        Request(result)
          .then(results => console.log(results.name))
          .catch(error => console.error(error));
      }
      );
    }
    )
    .catch(error => console.error(error));
}
