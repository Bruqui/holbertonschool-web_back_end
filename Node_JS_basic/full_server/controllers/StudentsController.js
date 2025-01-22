import { readDatabase } from '../utils.js';

class StudentsController {
  static async getAllStudents(req, res) {
    const databaseFile = process.argv[2];

    try {
      const students = await readDatabase(databaseFile);
      const responseLines = ['This is the list of our students'];

      Object.keys(students)
        .sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }))
        .forEach((field) => {
          responseLines.push(
            `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`,
          );
        });

      res.status(200).send(responseLines.join('\n'));
    } catch (err) {
      res.status(500).send(err.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const databaseFile = process.argv[2];
    const { major } = req.params;

    if (!['CS', 'SWE'].includes(major)) {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const students = await readDatabase(databaseFile);
      const studentList = students[major] || [];
      res.status(200).send(`List: ${studentList.join(', ')}`);
    } catch (err) {
      res.status(500).send(err.message);
    }
  }
}

export default StudentsController;
