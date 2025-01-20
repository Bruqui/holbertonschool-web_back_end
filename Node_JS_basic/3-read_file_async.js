const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        console.log('Number of students: 0');
        resolve();
        return;
      }

      const header = lines[0].split(',');
      const studentData = lines.slice(1);
      const fieldCounts = {};
      const fieldStudents = {};

      for (const line of studentData) {
        const record = line.split(',');
        if (record.length === header.length) {
          const firstName = record[0].trim();
          const field = record[3].trim();
          if (!fieldCounts[field]) {
            fieldCounts[field] = 0;
            fieldStudents[field] = [];
          }
          fieldCounts[field] += 1;
          fieldStudents[field].push(firstName);
        }
      }

      const totalStudents = Object.values(fieldCounts).reduce((acc, count) => acc + count, 0);
      console.log(`Number of students: ${totalStudents}`);

      for (const [field, count] of Object.entries(fieldCounts)) {
        const studentList = fieldStudents[field].join(', ');
        console.log(`Number of students in ${field}: ${count}. List: ${studentList}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
