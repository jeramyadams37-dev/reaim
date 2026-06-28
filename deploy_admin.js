const admin = require('firebase-admin');
const serviceAccount = require('./serviceAccountKey.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

console.log("Authentication successful via Admin SDK.");
console.log("Project ID: " + admin.app().options.credential.projectId);
// We can now interact with your Database/Storage directly.
