#!/usr/bin/node
const request = require('request');
const fs = require('fs');
if (process.argv[2] && process.argv[3]) {
  function Request (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      }
      );
    }
    );
  }

  Request(process.argv[2])
    .then((response) => {
      fs.writeFile(process.argv[3], response, (err) => {
        if (err) {
          console.error(err);
        }
      }
      );
    }
    )
    .catch((error) => console.error(error));
}
