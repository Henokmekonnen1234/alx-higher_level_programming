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

  Request(process.argv[2])
    .then(response => {
      let count = 0;
      response.results.forEach((result) => {
        result.characters.forEach((value) => {
          if (value.includes(18)) {
            count++;
          }
        }
        );
      }
      );
      console.log(count);
    }
    )
    .catch(error => { console.error(error); });
}
